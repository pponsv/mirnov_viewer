.PHONY : run build configure rebuild_ui clean remove_env deep_clean
ACTIVATE_VENV = . ./env/bin/activate

run:
	$(ACTIVATE_VENV); python3 main.py

build: 
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/TJII_data_acquisition

rebuild_ui: 
	mkdir -p src/ui/
	$(ACTIVATE_VENV); pyside6-uic ./ui/MainWindow.ui -o ./src/ui/ui_mainwindow.py
	$(ACTIVATE_VENV); pyside6-uic ./ui/ListDialog.ui -o ./src/ui/ui_listdialog.py

env: 
	test -d env || python3 -m venv ./env

configure: 
	$(MAKE) env
	$(ACTIVATE_VENV); pip install -r requirements.txt
	$(MAKE) rebuild_ui
	$(MAKE) build

clean:
	rm -rf .vscode/ __pycache__/ src/ui/
	$(MAKE) -C ./lib/TJII_data_acquisition clean

remove_env:
	rm -rf env/

deep_clean: remove_env clean