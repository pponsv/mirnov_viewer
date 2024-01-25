.PHONY : run build
SHELL := /bin/bash

run:
	. env/bin/activate; python3 main.py

build: 
	$(MAKE) -C ./lib/TJII_data_acquisition
	mkdir -p ./figs/

configure: 
	test -d env || python3 -m venv ./env
	. env/bin/activate; pip install pur
	. env/bin/activate; pip install -r requirements.txt
	. env/bin/activate; pyside6-uic ./ui/MainWindow.ui -o ./src/ui_mainwindow.py
	$(MAKE) build

clean:
	rm -rf env/ .vscode/ __pycache__/ src/ui_*.py