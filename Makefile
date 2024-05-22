.PHONY : run build configure rebuild_ui clean remove_env deep_clean
ACTIVATE_VENV = . ./env/bin/activate
PYTHON = python3.10

run:
	$(ACTIVATE_VENV); python main.py

build: 
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/TJII_data_acquisition

rebuild_ui: 
	mkdir -p src/ui/
	$(ACTIVATE_VENV); pyside6-uic ./ui/MainWindow.ui -o ./src/ui/ui_mainwindow.py
	$(ACTIVATE_VENV); pyside6-uic ./ui/ListDialog.ui -o ./src/ui/ui_listdialog.py

env: 
	test -d env || $(PYTHON) -m venv ./env

configure: 
	$(MAKE) env
	$(ACTIVATE_VENV); pip install -r requirements.txt
	$(MAKE) rebuild_ui
	$(MAKE) build

clean:
	rm -rf .vscode/ __pycache__/ src/ui/ figs/ bld/
	$(MAKE) -C ./lib/TJII_data_acquisition clean

remove_env:
	rm -rf env/

deep_clean: remove_env clean

release_build:
	$(MAKE) configure
	$(ACTIVATE_VENV); pip install pyinstaller
	$(ACTIVATE_VENV); pyinstaller dist/mirnov_viewer.spec --distpath ./bld/dist --workpath ./bld/build --clean
	
