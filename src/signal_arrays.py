from PySide6 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg

import numpy as np
from scipy.signal import spectrogram
from scipy.integrate import cumulative_trapezoid
from auxfiles.signal_names import LAYOUT_SIZE
from lib import TJII_data_acquisition as da

from .qt_workers import Worker
from .window_info import WindowInfo
from .plotting import PEN_BLACK, COLORMAP


class SignalArray:
    def __init__(
        self,
        shot,
        names,
        fig: pg.GraphicsLayoutWidget,
        threadpool: QtCore.QThreadPool,
        info: WindowInfo,
    ):
        self.shot = shot
        self.signals = {name: Signal(shot, name) for name in names}
        self.fig = fig
        self.ax = {}
        self.threadpool = threadpool
        self.info = info

    def read_seq(self):
        for name, signal in self.signals.items():
            signal.read_data()

    def read_parallel(self, printer):
        workers = []
        for name, signal in self.signals.items():
            workers.append(Worker(signal.read_data, printer))
            self.threadpool.start(workers[-1])
        self.threadpool.waitForDone()
        printer("Done")

    def make_axes(self, signals, sharex=False, sharey=False):
        numx, numy = LAYOUT_SIZE.get(len(signals), (1, len(signals)))
        self.fig.clear()
        self.ax = {}
        for i in range(numy):
            for j in range(numx):
                self.ax[(i, j)] = self.fig.addPlot(i, j)
                if sharex is True:
                    self.ax[(i, j)].setXLink(self.ax[(0, 0)])
                if sharey is True:
                    self.ax[(i, j)].setYLink(self.ax[(0, 0)])
                self.ax[(i, j)].setDefaultPadding(0.0)
                self.ax[(i, j)].enableAutoRange(enable=True)
                self.ax[(i, j)].getAxis("left").setWidth(40)
                self.ax[(i, j)].getAxis("right").setWidth(0)
                self.ax[(i, j)].getAxis("bottom").setHeight(15)
                self.ax[(i, j)].getAxis("top").setHeight(0)

    def make_spectrograms(self, tlim, printer=print):
        workers = {}
        for signal, pltidx in zip(self.signals.values(), self.ax):
            workers[pltidx] = Worker(
                signal.spectrogram,
                tlim=tlim,
            )
            self.threadpool.start(workers[pltidx])
        self.threadpool.waitForDone()

    def plot_spectrograms(self, tlim):
        self.make_axes(self.signals, sharex=True, sharey=True)
        for sig_key, iax in zip(self.signals, self.ax):
            self.signals[sig_key].plot_spec(self.ax[iax], COLORMAP, tlim)

    def plot_signals(self):
        self.make_axes(self.signals, sharex=True, sharey=False)
        for sig_key, pltidx in zip(self.signals, self.ax):
            self.signals[sig_key].plot(
                self.ax[pltidx],
                ds=self.info.downsample,
                dsFactor=self.info.downsampleFactor,
                pen=PEN_BLACK,
            )

    def plot_integrated(self):
        self.make_axes(self.signals, sharex=True, sharey=False)
        for sig_key, pltidx in zip(self.signals, self.ax):
            self.signals[sig_key].plot_integrated(
                self.ax[pltidx],
                ds=self.info.downsample,
                dsFactor=self.info.downsampleFactor,
                pen=PEN_BLACK,
            )

    def plot_alone(self, key):
        self.make_axes({key: self.signals[key]})
        self.signals[key].plot(
            ax=self.ax[(0, 0)],
            ds=self.info.downsample,
            dsFactor=self.info.downsampleFactor,
            pen=PEN_BLACK,
        )


class Signal:
    def __init__(self, shot, name):
        self.shot = shot
        self.name = name

    def read_data(self, printer=print):
        t, x, ierr = da.py_lectur(self.shot, self.name)
        if ierr == 0:
            self.t = t
            self.x = x
        else:
            print(f"{self.shot} {self.name} - Error {ierr}:")
            # da.py_ertxt(ierr)
            self.t = [0]
            self.x = [0]
        self.ierr = ierr
        printer(f"{self.shot} {self.name} - Done")
        if printer is not print:
            print(f"{self.shot} {self.name} - Done")
        return self.shot, self.name

    def plot(self, ax, ds, dsFactor, pen):
        ax.clear()
        ax.setLabels(left=self.name)
        if self.ierr != 0:
            return
        if ds is True:
            ax.plot(self.t[::dsFactor], self.x[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, self.x, pen=pen)

    def plot_integrated(self, ax, ds, dsFactor, pen):
        ax.clear()
        nx = cumulative_trapezoid(self.x, self.t, initial=0)
        if ds is True:
            ax.plot(self.t[::dsFactor], nx[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, nx, pen=pen)
        ax.setLabels(left=self.name)
        axis = ax.getAxis("left")
        axis.setWidth(40)

    def spectrogram(self, tlim):
        if self.ierr != 0:
            return
        dt = np.mean(np.diff(self.t)).item()
        mask = (self.t > tlim[0]) & (self.t < tlim[1])
        self.spec_freqs, self.spec_times, sxx = spectrogram(
            self.x[mask],
            fs=round(1.0 / dt),
            window="hamming",
            nperseg=512,
            noverlap=500,
            return_onesided=True,
        )
        self.spec_vals = 10 * np.log10(sxx / sxx.max())
        self.spec_times += self.t[mask][0]
        print(f"Spgram {self.name} done")

    def plot_spec(self, ax, colormap, tlim):
        ax.clear()
        ax.setLabels(left=self.name)
        if self.ierr != 0:
            return
        if hasattr(self, "spec_freqs"):
            x0, y0 = self.spec_times[0], self.spec_freqs[0]
            w = self.spec_times[-1] - x0
            h = self.spec_freqs[-1] - y0
            print(x0, y0, w, h)
            img = pg.ImageItem(
                image=self.spec_vals.T, levels=(-40, 0), rect=[x0, y0, w, h]
            )
            ax.addItem(img)
            ax.setXRange(x0, x0 + w)
            ax.setYRange(y0, y0 + h)
            cbar = ax.addColorBar(img, colorMap=colormap, values=(-40, 0), width=0.2)
            cbar.getAxis("right").setWidth(20)
