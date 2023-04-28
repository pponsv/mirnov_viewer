import TJII_data_acquisition as da
from spectrograms_lib import custom_spect
from multiprocessing import Pool
import database
from auxfiles.mirnov_names import COIL_NAMES



class Mirnov_array:
    def __init__(self, shot, names):
        self.shot = shot
        self.coils = [Mirnov_coil(shot, name) for name in names]

    def read_seq(self):
        for coil in self.coils:
            coil.read_data(self.shot)

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


class Mirnov_coil:
    def __init__(self, shot, name):
        self.shot = shot
        self.name = name

    def read_data(self):
        t, x, ierr = da.py_lectur(self.shot, self.name)
        if ierr == 0:
            self.t = t
            self.x = x
        else:
            print(f"Error {ierr}:")
            da.py_ertxt(ierr)
            self.t = [0]
            self.x = [0]
        print(self.shot, self.name, "done")
        return self

    def plot(self, ax, ds, dsFactor, pen):
        ax.clear()
        if ds is True:
            ax.plot(self.t[::dsFactor], self.x[::dsFactor], pen=pen)
        else:
            ax.plot(self.t, self.x, pen=pen)
        ax.setLabels(title=self.name)
        axis = ax.getAxis("left")
        axis.setWidth(40)

    def spectrogram(self):
        self.spec_freqs, self.spec_times, self.spec_vals, fnyq = custom_spect(self.t, self.x)

    def plot_spec(self):
        self.spectrogram()
        
