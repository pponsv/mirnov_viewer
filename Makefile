.phony: run build

run:
	python3 main.py

build: 
	$(MAKE) -C ./lib/TJII_data_acquisition
	mkdir -p ./figs/