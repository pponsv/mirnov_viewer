.PHONY : run build configure rebuild_ui clean remove_env deep_clean env
# ENV_PATH = $(HOME)/.envs/mirnov_viewer_env
ENV_PATH = ./env/
ACTIVATE_VENV = . $(ENV_PATH)/bin/activate

run:
	$(ACTIVATE_VENV); mirnov_viewer

install: clean env
	$(ACTIVATE_VENV); pip install --verbose .

rebuild_ui:
	$(ACTIVATE_VENV); pyside6-uic ./mirnov_viewer/ui/MainWindow.ui -o ./mirnov_viewer/ui_mainwindow.py
	$(ACTIVATE_VENV); pyside6-uic ./mirnov_viewer/ui/ListDialog.ui -o ./mirnov_viewer/ui_listdialog.py

env: 
	test -d $(ENV_PATH) || python3 -m venv $(ENV_PATH)

clean:
	rm -rf .vscode/ __pycache__/ figs/ bld/

remove_env:
	rm -rf $(ENV_PATH)

deep_clean: remove_env clean

release_build:
	$(MAKE) configure
	$(ACTIVATE_VENV); pip install pyinstaller
	$(ACTIVATE_VENV); pyinstaller dist/mirnov_viewer.spec --distpath ./bld/dist --workpath ./bld/build --clean
	
list:
	ls -R ./mirnov_viewer
	cat meson.build
	cat mirnov_viewer/meson.build
	cat mirnov_viewer/TJII_data_acquisition/meson.build
