make -C docs html

doc2dash -A -f -n experiment_foobar docs/build/html/

python -m sphinx.ext.intersphinx docs/build/html/objects.inv

---

To edit: At least domain.py