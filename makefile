run:
	python plymgf/classlexer.py ./data/test.mgf
test:
	python -m unittest discover testu
open:
	geany `python .script/allpath.py` &
doc:
	epydoc --html --name "PLYMGF" -v -o doc `python .script/allpath.py`
clean:
	rm -rf doc
	rm -f plymgf/*.pyc
	rm -f plymfg/*.out
	rm -f plymgf/parsetab.py
	rm -f *.out
pylint:
	pylint `python .script/allpath.py`
