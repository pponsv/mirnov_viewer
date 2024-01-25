MAIN = ./src/tjii_data_acquisition.f90
MODNAME = TJII_data_acquisition_f
ENV_ACTIVATION_PATH = ../../env/bin/activate

all: $(MAIN)
	. $(ENV_ACTIVATION_PATH); which python3
	. $(ENV_ACTIVATION_PATH); python3 -m numpy.f2py -c --f90flags='-Wno-tabs -lRpcC' -L./lib/ -m $(MODNAME) $(MAIN) ./lib/libRpcC.a

pyc: $(MAIN)
	. $(ENV_ACTIVATION_PATH); python3 -m numpy.f2py -h tmp.pyf -m $(MODNAME) $(MAIN)

clean:
	rm -f *.so

test:
	. $(ENV_ACTIVATION_PATH); python3 test.py