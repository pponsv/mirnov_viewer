MAIN = ./src/tjii_data_acquisition.f90
MODNAME = TJII_data_acquisition_f

all: $(MAIN)
	f2py3 -c --f90flags='-Wno-tabs -lRpcC' -L./lib/ -m $(MODNAME) $(MAIN) ./lib/libRpcC.a

pyc: $(MAIN)
	f2py3 -h tmp.pyf -m $(MODNAME) $(MAIN)

clean:
	rm -f *.so

test:
	python3 test.py