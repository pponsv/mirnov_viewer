import TJII_data_acquisition as da
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

    def read_multi(self):
        # database.read_multi(info.shot, self.coils)
        pool = Pool(processes=5)
        res_async = []
        for coil in self.coils:
            print(self.shot, coil.name, "init")
            res_async.append(pool.apply_async(coil.read_data))
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
        # axis.setStyle(
        #     tickTextOffset=10,
        #     autoExpandTextSpace=True,
        #     textFillLimits=[(-1e12, 1e12)],
        # )
        # axis.setTicks([(x, "%.2f" % x) for x,_ in axis.tickValues(None,None,axis.orthoRange)])
        # print(axis.tickValues(None,None,axis.orthoRange))

# def read_multi(coils):
#     t0 = time()
#     pool = Pool(processes=5)
#     res_async = []
#     for coil in coils:
#         print(coil.shot, coil.name, "init")
#         res_async.append(pool.apply_async(coil.read_data))
#     pool.close()
#     res = []
#     for r in res_async:
#         res.append(r.get())
#     for r in res:
#         for idx, o in enumerate(coils):
#             if r.name == o.name:
#                 coils[idx] = r
#     pool.join()
#     print(f"Time elapsed: {(time() - t0):.5f}s")
