run:
	python plymgf/classlexer.py
clean:
	rm -f plymgf/*.pyc
	rm -f plymfg/*.out
	rm -f plymgf/parsetab.py
test:
	python -m unittest discover plymgf
