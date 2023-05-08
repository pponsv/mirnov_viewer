import numpy as np
import pyqtgraph as pg
import mirnov_arrays as ma
from lib import TJII_data_acquisition as da

layout_size = {32: (4, 8), 25: (5, 5), 24: (4, 6)}

PEN_BLACK = pg.mkPen(color="#000000", width=1)
COLORMAP_JET = pg.colormap.getFromMatplotlib("jet")


def getLastShot(window):
    shot, ierr = da.py_lastshot()
    if ierr == 0:
        window.shotNumberInput.clear()
        window.shotNumberInput.insert(f"{shot}")
    else:
        window.statusbar.showMessage("Error reading last shot: {ierr}")


def make_array(info):
    if info.array == "Helical":
        names = ma.COIL_NAMES[info.array][info.subarray][info.orientation]
    else:
        names = ma.COIL_NAMES[info.array]
    return ma.Mirnov_array(info.shot, names)


def make_plots(layout, numx, numy, sharex=False, sharey=False):
    layout.clear()
    plots = {}
    for i in range(numy):
        for j in range(numx):
            plots[(i, j)] = layout.addPlot(i, j)
            if sharex is True:
                plots[(i, j)].setXLink(plots[(0, 0)])
            if sharey is True:
                plots[(i, j)].setYLink(plots[(0, 0)])
    return plots


def plot_coil(layout, info, array):
    coil = [co for co in array.coils if (co.name == info.selectedCoil)][0]
    print(coil.name)
    plots = make_plots(layout, 1, 1)
    coil.plot(
        ax=plots[(0, 0)],
        ds=info.downsample,
        dsFactor=info.downsampleFactor,
        pen=PEN_BLACK,
    )
    plots[(0, 0)].autoRange()


def plot_array(layout, info, array):
    nx, ny = layout_size[len(array.coils)]
    plots = make_plots(layout, nx, ny, sharex=True)
    for idx, pltidx in enumerate(plots):
        array.coils[idx].plot(
            plots[pltidx],
            ds=info.downsample,
            dsFactor=info.downsampleFactor,
            pen=PEN_BLACK,
        )
        # plots[pltidx].setLabels(title=array.coils_idx.)
        # plot_single(plots[(i, j)], array.coils[idx]x[::delta], y[::delta])


def spectrograms_array(layout, info, array):
    nx, ny = layout_size[len(array.coils)]
    plots = make_plots(layout, nx, ny, sharex=True, sharey=True)
    for idx, pltidx in enumerate(plots):
        array.coils[idx].plot_spec(plots[pltidx], colormap=COLORMAP_JET)
    # plots[(0, 0)].autoRange()


# def plot_spgrams(layout):
#     plots = make_plots(layout, 4, 8)
#     for i, j in plots:
#         img = pg.ImageItem(image=np.random.rand(5000, 500), levels=(0, 1))
#         bar = pg.ColorBarItem((0, 1), colorMap=COLORMAP_JET)
#         plots[(i, j)].addItem(img)
#         bar.setImageItem(img, insert_in=plots[(i, j)])
