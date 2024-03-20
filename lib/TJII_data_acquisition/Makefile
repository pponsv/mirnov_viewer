ACTIVATE_VENV = . ../../env/bin/activate

all: meson_configure meson_build

meson_configure:
	$(ACTIVATE_VENV); meson setup --wipe bld

meson_build:
	$(ACTIVATE_VENV); meson compile -C bld
	cp bld/TJII*.so ./

clean:
	rm -rf *.so ./bld/

test:
	$(ACTIVATE_VENV); python3 test.py