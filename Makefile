.PHONY : run build configure rebuild_ui clean remove_env deep_clean
ACTIVATE_VENV = . ./env/bin/activate
PYTHON=python3.10

run:
	$(ACTIVATE_VENV); python main.py

build: 
	$(ACTIVATE_VENV); $(MAKE) -C ./lib/TJII_data_acquisition

env: 
	test -d env || $(PYTHON) -m venv ./env

configure: 
	$(MAKE) env
	$(ACTIVATE_VENV); pip install -r requirements.txt
	$(MAKE) build

clean:
	rm -rf .vscode/ __pycache__/ src/ui/ figs/
	$(MAKE) -C ./lib/TJII_data_acquisition clean

remove_env:
	rm -rf env/

deep_clean: remove_env clean