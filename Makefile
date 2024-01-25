.PHONY : run build configure rebuild_ui clean
ACTIVATE_VENV = . ./env/bin/activate

run:
	$(ACTIVATE_VENV); python3 main.py

build: 
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/TJII_data_acquisition
	mkdir -p ./figs/

rebuild_ui: 
	$(ACTIVATE_VENV); pyside6-uic ./ui/MainWindow.ui -o ./src/ui_mainwindow.py

env: 
	test -d env || python3 -m venv ./env

configure: 
	$(MAKE) env
	$(ACTIVATE_VENV); pip install -r requirements.txt
	$(MAKE) rebuild_ui
	$(MAKE) build

clean:
	rm -rf env/ .vscode/ __pycache__/ src/ui_*.py
	$(MAKE) -C ./lib/TJII_data_acquisition clean