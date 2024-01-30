import numpy as np
import pyqtgraph as pg

from lib import TJII_data_acquisition as da


PEN_BLACK = pg.mkPen(color="#000000", width=1)
COLORMAP = pg.colormap.get("CET-R4")


def getLastShot(lineedit, statusbar):
    shot, ierr = da.py_lastshot()
    if ierr == 0:
        lineedit.clear()
        lineedit.insert(f"{shot}")
    else:
        statusbar.showMessage("Error reading last shot: {ierr}")


def bandpass_filter_vec(vec, flim, dt=0.001):
    if flim == (None, None):
        return vec
    ff = np.fft.fft(vec)
    fr = np.fft.fftfreq(len(vec), dt)
    mask = (np.abs(fr) <= flim[1]) & (np.abs(fr) >= flim[0])
    ff -= ff * (~mask)
    nsig = np.fft.ifft(ff, len(vec))
    return nsig.real


def get_value_from_field(field, kind):
    try:
        out = kind(field.text())
    except:
        out = None
    return out
