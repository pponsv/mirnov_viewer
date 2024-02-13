import numpy as np
import pyqtgraph as pg

from scipy.signal import buttord, butter, sosfilt
from lib import TJII_data_acquisition as da


PEN_BLACK = pg.mkPen(color="#000000", width=1)
COLORMAP = pg.colormap.get("CET-R4")


def getLastShot(lineedit, printer=print):
    shot, ierr = da.py_lastshot()
    if ierr == 0:
        lineedit.clear()
        lineedit.insert(f"{shot}")
    else:
        printer("Error reading last shot: {ierr}")


def bandpass_filter_vec(vec, flim, dt=0.001):
    if flim == (None, None):
        return vec
    fnyq = 1 / (2 * dt)
    try:
        if (flim[0] == 0) or (flim[0] is None):
            ord, wn = buttord(
                wp=flim[1], ws=1.1 * flim[1], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="lowpass", output="sos", fs=1 / dt)
        elif np.isclose(flim[1], fnyq) or (flim[1] is None):
            ord, wn = buttord(
                wp=flim[0], ws=0.9 * flim[0], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="highpass", output="sos", fs=1 / dt)
        else:
            ord, wn = buttord(
                wp=flim, ws=[0.9 * flim[0], 1.1 * flim[1]], gpass=3, gstop=20, fs=1 / dt
            )
            sos = butter(ord, wn, btype="bandpass", output="sos", fs=1 / dt)
    except:
        print("Butterworth filter error - using FFT filter")
        return bandpass_filter_fft(vec, flim, dt)
    return sosfilt(sos, vec)


def bandpass_filter_fft(vec, flim, dt=0.001):
    if None in flim:
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
