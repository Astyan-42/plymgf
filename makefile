run:
	python plymgf/classlexer.py ./plymgf/data/test.mgf
runreader:
	python plymgf/mgfreader.py ./plymgf/data/test.mgf
test:
	python -m unittest discover plymgf
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
	mv testu tests
	python setup.py develop
	mv tests testu
sourcedist:
	mv testu tests
	python setup.py sdist
	mv tests testu
register:
	mv testu tests
	python setup.py register sdist upload
	mv tests testu
