from lib import TJII_data_acquisition as da

# from spectrograms_lib import custom_spect
from scipy.signal import spectrogram
from scipy.integrate import cumulative_trapezoid
from multiprocessing import Pool
import pyqtgraph as pg
from auxfiles.mirnov_names import COIL_NAMES

import numpy as np


class Signal_array:
    def __init__(self, shot, names):
        self.shot = shot
        self.coils = [Signal(shot, name) for name in names]

    def read_seq(self):
        for coil in self.coils:
            coil.read_data()

    def read_multi(self, printer=print):
        # database.read_multi(info.shot, self.coils)
        def tmp_callback(result):
            printer(f"{result.shot} {result.name} done")
            return result

        pool = Pool(processes=5)
        res_async = []
        for coil in self.coils:
            printer(f"{self.shot} {coil.name} init")
            res_async.append(pool.apply_async(coil.read_data, callback=tmp_callback))
        pool.close()
        res = []
        for r in res_async:
            res.append(r.get())
        for r in res:
            for idx, o in enumerate(self.coils):
                if r.name == o.name:
                    self.coils[idx] = r
        pool.join()
        # load_multi.read_multi(self.coils)


class Signal:
    def __init__(self, shot, name):
        self.shot = shot
        self.name = name

    def read_data(self):
        t, x, ierr = da.py_lectur(self.shot, self.name)
        if ierr == 0:
            self.t = t
            self.x = x
            self.ierr = ierr
        else:
            print(f"Error {ierr}:", end="")
            da.py_ertxt(ierr)
            self.t = [0]
            self.x = [0]
            self.ierr = ierr
        print(self.shot, self.name, "done")
        return self

    # def read_data(self):
    #     self.t = np.linspace(0,100,100001)
    #     self.x = np.sin(125*2*np.pi*self.t) + np.cos(215*2*np.pi*self.t)+(1-0.5*np.random.rand(len(self.t)))
    #     return self

    def plot(self, ax, ds, dsFactor, pen):
        ax.clear()
        if ds is True:
            ax.plot(self.t[::dsFactor], self.x[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, self.x, pen=pen)
        ax.setLabels(title=self.name)
        axis = ax.getAxis("left")
        axis.setWidth(40)

    def plot_integrated(self, ax, ds, dsFactor, pen):
        ax.clear()
        nx = cumulative_trapezoid(self.x, self.t, initial=0)
        if ds is True:
            ax.plot(self.t[::dsFactor], nx[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, nx, pen=pen)
        ax.setLabels(title=self.name)
        axis = ax.getAxis("left")
        axis.setWidth(40)

    def spectrogram(self, tlim):
        if self.ierr == 0:
            dt = np.mean(np.diff(self.t))
            mask = (self.t > tlim[0]) & (self.t < tlim[1])
            self.spec_freqs, self.spec_times, sxx = spectrogram(
                self.x[mask],
                fs=round(1 / dt),
                window="hamming",
                nperseg=512,
                noverlap=500,
                return_onesided=True,
            )
            self.spec_vals = 10 * np.log10(sxx / sxx.max())
            self.spec_times += self.t[mask][0]
            print(f"Spgram {self.name} done")

    def plot_spec(self, ax, colormap, tlim):
        self.spectrogram(tlim)
        if hasattr(self, "spec_freqs"):
            x0, y0 = self.spec_times[0], self.spec_freqs[0]
            w = self.spec_times[-1] - x0
            h = self.spec_freqs[-1] - y0
            print(x0, y0, w, h)
            img = pg.ImageItem(
                image=self.spec_vals.T, levels=(-40, 0), rect=[x0, y0, w, h]
            )
            bar = pg.ColorBarItem((-40, 0), colorMap=colormap)
            ax.addItem(img)
            ax.setXRange(x0, x0 + w)
            ax.setYRange(y0, y0 + h)
            ax.setLabels(title=self.name)
            bar.setImageItem(img, insert_in=ax)
