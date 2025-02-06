install:
	pip3 install -r requirement.txt
populate:
	pip3 freeze > requirement.txt
run:
	python3 Sample/sample.py

.PHONY=install populate run
