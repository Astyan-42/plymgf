run:
	python plymgf/classlexer.py ./testu/data/test.mgf
test:
	python -m unittest discover testu
open:
	geany `python .script/allpath.py` &
doc:
	epydoc --html --name "PLYMGF" -v -o doc `python .script/allpath.py`
clean:
	rm -rf build
	rm -rf dist
	rm -rf plymgf.egg-info
	rm -rf doc
	rm -f plymgf/*.pyc
	rm -f plymfg/*.out
	rm -f plymgf/parsetab.py
	rm -f *.out
pylint:
	pylint `python .script/allpath.py`
develop:
	python setup.py develop
sourcedist:
	python setup.py sdist
register:
	python setup.py register sdist upload
