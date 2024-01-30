import numpy as np
import pyqtgraph as pg

# from . import signal_arrays as sa
from auxfiles.signal_names import LAYOUT_SIZE

# from .main_window import MainWindow
from lib import TJII_data_acquisition as da


PEN_BLACK = pg.mkPen(color="#000000", width=1)
COLORMAP = pg.colormap.getFromMatplotlib("jet")
COLORMAP = pg.colormap.get("CET-R4")


def getLastShot(lineedit, statusbar):
    shot, ierr = da.py_lastshot()
    if ierr == 0:
        lineedit.clear()
        lineedit.insert(f"{shot}")
    else:
        statusbar.showMessage("Error reading last shot: {ierr}")


def bandpass_filter_vec(vec, flim, dt=0.001):
    if flim is None:
        return vec
    ff = np.fft.fft(vec)
    fr = np.fft.fftfreq(len(vec), dt)
    mask = (np.abs(fr) <= flim[1]) & (np.abs(fr) >= flim[0])
    ff -= ff * (~mask)
    nsig = np.fft.ifft(ff, len(vec))
    return nsig.real


# def make_plots(layout, numx, numy, sharex=False, sharey=False):
#     layout.clear()
#     plots = {}
#     for i in range(numy):
#         for j in range(numx):
#             plots[(i, j)] = layout.addPlot(i, j)
#             if sharex is True:
#                 plots[(i, j)].setXLink(plots[(0, 0)])
#             if sharey is True:
#                 plots[(i, j)].setYLink(plots[(0, 0)])
#             plots[(i, j)].enableAutoRange(enable=True)
#     return plots


# def plot_coil(layout, info, array: sa.SignalArray):
#     coil = [co for co in array.signals if (co.name == info.selectedCoil)][0]
#     print(coil.name)
#     plots = make_plots(layout, 1, 1)
#     coil.plot(
#         ax=plots[(0, 0)],
#         ds=info.downsample,
#         dsFactor=info.downsampleFactor,
#         pen=PEN_BLACK,
#     )
# plots[(0, 0)].autoRange()


# def plot_integrated_array(layout, info, array: sa.SignalArray):
#     nx, ny = LAYOUT_SIZE[len(array.signals)]
#     plots = make_plots(layout, nx, ny, sharex=True)
#     for idx, pltidx in enumerate(plots):
#         array.signals[idx].plot_integrated(
#             plots[pltidx],
#             ds=info.downsample,
#             dsFactor=info.downsampleFactor,
#             pen=PEN_BLACK,
#         )
#     # plots[(0, 0)].autoRange()
#     return plots


# def plot_array(layout, info, array):
#     nx, ny = LAYOUT_SIZE[len(array.signals)]
#     plots = make_plots(layout, nx, ny, sharex=True)
#     for idx, pltidx in enumerate(plots):
#         array.signals[idx].plot(
#             plots[pltidx],
#             ds=info.downsample,
#             dsFactor=info.downsampleFactor,
#             pen=PEN_BLACK,
#         )
#     # plots[(0, 0)].autoRange()
#     return plots
# plots[pltidx].setLabels(title=array.coils_idx.)
# plot_single(plots[(i, j)], array.coils[idx]x[::delta], y[::delta])


# def spectrograms_array(layout, info, array, tlim):
#     nx, ny = LAYOUT_SIZE[len(array.signals)]
#     plots = make_plots(layout, nx, ny, sharex=True, sharey=True)
#     for idx, pltidx in enumerate(plots):
#         array.signals[idx].plot_spec(plots[pltidx], colormap=COLORMAP, tlim=tlim)
# plots[(0, 0)].autoRange()


# def plot_spgrams(layout):
#     plots = make_plots(layout, 4, 8)
#     for i, j in plots:
#         img = pg.ImageItem(image=np.random.rand(5000, 500), levels=(0, 1))
#         bar = pg.ColorBarItem((0, 1), colorMap=COLORMAP_JET)
#         plots[(i, j)].addItem(img)
#         bar.setImageItem(img, insert_in=plots[(i, j)])
