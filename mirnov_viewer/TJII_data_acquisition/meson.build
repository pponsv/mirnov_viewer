MODULE_NAME = 'TJII_data_acquisition_f'

CXX = meson.get_compiler('c')
lib_rpc = CXX.find_library('RpcC', dirs: [meson.current_source_dir() / 'lib'])

np_dep = dependency('numpy')

numpy_inc = run_command(py, '-c', 'import numpy; print(numpy.get_include())', check: true).stdout().strip()
f2py_inc = run_command(py, '-c', 'import numpy.f2py; print(numpy.f2py.get_include())', check: true).stdout().strip()

inc_np = include_directories(numpy_inc)
inc_f2py = include_directories(f2py_inc)

py.extension_module(
  MODULE_NAME,
  [
    'src/tjii_data_acquisition.f90',
    'src/TJII_data_acquisition_f-f2pywrappers2.f90',
    'src/TJII_data_acquisition_fmodule.c',
    f2py_inc / 'fortranobject.c',
  ],
  include_directories: [inc_np, inc_f2py],
  dependencies: [py.dependency(), lib_rpc, np_dep],
  install: true,
  subdir: 'mirnov_viewer/TJII_data_acquisition',
)

py.install_sources(['__init__.py', 'main.py'], subdir: 'mirnov_viewer/TJII_data_acquisition')
