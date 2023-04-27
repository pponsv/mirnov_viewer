import numpy as np
import pandas as pd
import gc
import os

from scipy.signal import spectrogram as spect
from scipy.signal import savgol_filter
from scipy.fft import fft, ifft, fftfreq

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.rcParams['figure.figsize'] = [9, 6]

from TJII_data_acquisition import py_lectur, py_dimens

currentpath  = os.path.dirname(os.path.abspath(__file__))
datapath_lib = currentpath + '/../mirnov_probes/data/'
# cal          = pd.read_pickle(datapath_lib+'auxfiles/cal_sign_2021_03_30.pkl')
# coil_attr    = pd.read_pickle(datapath_lib+'auxfiles/coil_attr.pkl')

DIAGNOSTICS = {'NBI':
               [['IACCEL1_', 'NBI1', 'darkturquoise', 1], 
                ['IACCEL2_', 'NBI2', 'deepskyblue',   1]],
               'ECRH': 
               [['GR',  'ECRH1', 'yellow', 1], 
                ['GR2', 'ECRH2', 'gold',   1]],
               'Densidad, corriente, temperatura': 
               [['Ip_b4_', 'Plasma current', 'g', 1], 
                ['ECE10', 'Plasma temperature', 'k', -1],
                ['Densidad2_', 'Line density', 'r', 1]]}

LABELS = {'NBI': 
          ['', 'ylabel'],
          'ECRH': 
          ['', 'ylabel'],
          'Densidad, corriente, temperatura': 
          ['Time (ms)', 'ylabel']}

def nextpow2(n):
    return int(2**np.ceil(np.log2(n)))

def prevpow2(n):
    return int(2**np.floor(np.log2(n)))

def time_limits(time, t0, t1, fft=False):
    dt = (time[-1] - time[0])/(len(time)-1)
    if time[0] > t0:
        idx0 = 0
    else:
        idx0 = int((t0 - time[0])/dt)
    if time[-1] < t1:
        idx1 = -1
    else:
        idx1 = round((t1 - time[0])/dt)+1
        if fft:
            nidx = idx0 + nextpow2(idx1-idx0)
            if (nidx<len(time)):
                idx1 = nidx
            else:
                idx1 = idx0 + prevpow2(idx1-idx0)
    return idx0, idx1, dt, time[idx0:idx1]

def one_plot_diagnostics(SHOT, ax, f_nyq, tlim, legend=False, densidad=None):
    for label in DIAGNOSTICS:
        for diagnostic in DIAGNOSTICS[label]:
            diag, label, color, fac = diagnostic
            ndata, nvent, ierr = py_dimens(SHOT, diag)
            if ierr == 0:
                if (diag=='Densidad2_') & (densidad is not None):
                    diag = 'DENCM0_'
                time, data, t,t,t,t = py_lectur(SHOT, diag)
                data = fac*savgol_filter(data, 51, 3)
                tidx0, tidx1, tdt, ttime = time_limits(time, *tlim)
                fac = f_nyq/10
                ax.plot(ttime,
                        data[tidx0:tidx1],
                        label=label,
                        color=color,
                        linewidth=2)
                if (diag=='Densidad2_') or (diag=='DENCM0_'):
                    tmp = 1/np.sqrt(np.abs(data[tidx0:tidx1])+1)
                    ax.plot(ttime, 
                            tmp/tmp.max()*ax.get_ylim()[1], 
                            color='r', 
                            ls=':',
                            label='(Line density)**(-0.5)')
        if legend:
            ax.legend()

def custom_spect(time, data, tlim=(0,-1)):
    idx0, idx1, dt, ntime = time_limits(time, *tlim)
    print(idx0, idx1, dt, ntime)
    f_nyq = round(1/(2*dt))
    f, t, sxx = spect(data[idx0:idx1], 
                      fs=round(1/dt), 
                      window='hamming',
                      nperseg=512,
                      noverlap=400,
                      return_onesided=True)
    t += time[idx0]
    return f, t, 10*np.log10(sxx/sxx.max()), f_nyq

def plot_spect(SHOT, COIL, fig, ax, f, t, sxx):
    ax.clear()
    k = ax.pcolormesh(t,
                  f,
                  sxx,
                  vmax=0,
                  vmin=-40,
                  shading='nearest',
                  cmap=plt.get_cmap('jet'))
    ax.set_title('Shot = {},    Coil={},    dt = {:.4f}'
                 .format(SHOT, COIL, 1/(2*f[-1])))
    ax.set_ylabel('Frequency [kHz]')
    cbar = fig.colorbar(k, ax=ax)
    cbar.set_label('dB')

def spect_twofigs(tlim):
    fig  = plt.figure()
    ax0  = fig.add_subplot(2,1,1)
    ax1  = fig.add_subplot(2,1,2)
    div0 = make_axes_locatable(ax0)
    cax0 = div0.append_axes('right', size='5%', pad=0.07)
    div1 = make_axes_locatable(ax1)
    cax1 = div1.append_axes('right', size='5%', pad=0.07)
    cax1.remove()
    #ax1.xaxis.tick_top()
    ax0.set_xlim(tlim)
    ax1.sharex(ax0)
    
    ax1.set_xlabel('Time (ms)')
    ax0.set_ylabel('Frequency (kHz)')
    ax1.set_ylabel('UNIDADES')
#     plt.setp(ax1.get_xticklabels(), visible=False)
    return fig, ax0, ax1, cax0

def plot_diagnostics(SHOT, tlim):
    fig, axes = plt.subplots(len(DIAGNOSTICS), 1, sharex=True)
    for idx, diag in enumerate(DIAGNOSTICS):
        for name, leg, col, fac in DIAGNOSTICS[diag]:
            time, data, t,t,t,ierr = py_lectur(SHOT, name)
            if ierr == 0:
                data = fac*savgol_filter(data, 21, 3)
                tidx0, tidx1, tdt, ttime = time_limits(time, *tlim)
                axes[idx].plot(ttime, 
                               data[tidx0:tidx1], 
                               color=col, 
                               label=leg,
                               linewidth=3)
                axes[idx].axhline(0, linestyle=':', color='k', linewidth=0.5)
                axes[idx].set_xlim((ttime[0], ttime[-1]))
                axes[idx].set_title(diag)
                axes[idx].set_xlabel(LABELS[diag][0])
                axes[idx].set_ylabel(LABELS[diag][1])
                axes[idx].legend()
    fig.align_labels(axes)

def bandpass_filter(time, signal, trange, dt, freqs):
    """
    Implementation of a fft bandpass filter. Takes as arguments:
        - time:     Time array
        - signal:   Signal array
        - trange:   Time range where the filter is applied. In the same units as time.
        - dt:       Sampling time (in the same units as time).
        - freqs:    Filter frequencies. Array. 
            * F_low  = freqs[0]
            * F_high = freqs[1]
    Returns:
        - Time array of the filtered signal
        - The filtered signal
    """
    idx0, idx1 = ((trange - time[0])/dt).astype(int)
    nsignal    =   signal[idx0:idx1]
    f1         =   fft(nsignal)
    freq_arr   =   fftfreq(len(nsignal), d=dt)
    mask1      = ((freq_arr<freqs[1])  & (freq_arr>freqs[0]))
    mask2      = ((freq_arr<-freqs[0]) & (freq_arr>-freqs[1]))
    mask       =  (mask1 + mask2).astype(bool)
    rsignal    =   ifft(f1*mask)
    return time[idx0:idx1], np.real(rsignal)

def filter_subarray(coildata, coilnames, trange, frange):
    time  = coildata.index.to_numpy()
    dt_ms =  (time[-1] - time[0])/(len(time)-1)
    rdata = coildata.loc[:, coilnames].to_numpy().T
    fdata = []
    for idx, tdata in enumerate(rdata):
        t, fsig = bandpass_filter(time, tdata, trange, dt_ms, frange)
        fdata.append(fsig)
    return t, np.array(fdata)

def easy_spectrogram(SHOT, COIL='H1P01', tlim=(1050, 1250), densidad=None):
    time, data, *_, ierr = py_lectur(SHOT, COIL)
    if ierr!=0:
        print('Error: {}'.format(ierr))
        return None
    f, t, sxx, f_nyq = custom_spect(time, data, tlim=tlim)
    fig, ax0, ax1, cax = spect_twofigs((t[0], t[-1]))
    plot_spect(SHOT, COIL, fig, ax0, cax, f, t, sxx)
    one_plot_diagnostics(SHOT, ax1, f_nyq, tlim, legend=True, densidad=densidad)
    return fig, [ax0, ax1]


if __name__ == "__main__":
    SHOT = 51090
    COIL = 'H1P01'
    tlim = (1050, 1250)
    time, data, t,t,t,ierr = py_lectur(SHOT, COIL)
    if ierr != 0:
        print('Error: {}',format(ierr))
    else:
        f, t, sxx, f_nyq = custom_spect(time, data, tlim=tlim)

    fig, ax0, ax1, cax = spect_twofigs((t[0], t[-1]))
    plot_spect(SHOT, COIL, fig, ax0, cax, f, t, sxx)
    one_plot_diagnostics(SHOT, ax1, f_nyq, tlim, legend=True)
    ax1.legend()

    plot_diagnostics(SHOT, tlim)

    plt.show()
