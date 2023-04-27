import time
import TJII_data_acquisition as da
from multiprocessing import Pool

def getLastShot(window):
    shot, ierr = da.py_lastshot()
    if ierr==0:
        window.shotNumberInput.insert(f"{shot}")
    else:
        window.statusbar.showMessage('Error reading last shot: {ierr}')

def read_multi(shot, coils):
    # t0 = time()
    pool = Pool(processes=5)
    res_async = []
    for coil in coils:
        print(shot, coil.name, "init")
        res_async.append(pool.apply_async(coil.read_data))
    pool.close()
    res = []
    for r in res_async:
        res.append(r.get())
    for r in res:
        for idx, o in enumerate(coils):
            if r.name == o.name:
                coils[idx] = r
    pool.join()
    # print(f"Time elapsed: {(time() - t0):.5f}s")