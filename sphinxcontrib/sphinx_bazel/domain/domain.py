"""
Bazel domain implementation for Sphinx.

Domain overview
===============

* **workspace**: contains the ``WORKSPACE`` file. Container for multiple packages

 * **package**: contains a ``BUILD`` file. Container for multiple targets

  * **target**: any file or .bzl-file. If last, following is available:

   * **rule**:  a defined rule inside a .bzl-file
   * **macro**: a defined macro-function inside a .bzl file


Domain directives
=================

* bazel-workspace
* bazel-package
* bazel-target
* bazel-rule
* bazel-macro
"""

# Implementation details/help taken from:
# Domains user manual : http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html
# Domains API: http://www.sphinx-doc.org/en/master/extdev/domainapi.html#domain-api
# Python Domain impl: https://github.com/sphinx-doc/sphinx/blob/master/sphinx/domains/python.py
# Java Domain impl: https://github.com/bronto/javasphinx/tree/master/javasphinx

from sphinx.domains import Domain, ObjType
from sphinx.locale import _
from typing import Iterable, Tuple

from sphinxcontrib.sphinx_bazel.domain.workspace import BazelWorkspace
from sphinxcontrib.sphinx_bazel.domain.object import BazelObject


class BazelDomain(Domain):
    """Bazel langage domain"""

    name = 'bazel'
    label = 'Bazel'
    object_types = {
        'workspace': ObjType(_('workspace'), 'workspace', 'ref'),
        'package': ObjType(_('package'), 'package', 'ref'),
        'target': ObjType(_('target'), 'target', 'ref'),
        'rule': ObjType(_('rule'), 'rule', 'ref'),
        'macro': ObjType(_('macro'), 'macro', 'ref'),
        'impl': ObjType(_('impl'), 'impl', 'ref'),
        'attribute': ObjType(_('attribute'), 'attribute', 'ref')
    }
    directives = {
        'workspace': BazelWorkspace,
        'package': BazelObject,
        'target': BazelObject,
        'rule': BazelObject,
        'macro': BazelObject,
        'implementation': BazelObject,
        'impl': BazelObject,
        'attribute': BazelObject,
    }
    roles = {}
    initial_data = {
        'objects': {},
        'workspaces': {}
    }
    indices = []
    

    def get_objects(self) -> Iterable[Tuple[str, str, str, str, str, int]]:
        objects = []
        for refname, (docname, obj_type) in self.data["objects"].items():
            yield (refname, refname, 'function', docname, refname, 1)
        # objects = []
        # name = 'name'
        # dispname = 'dispname'
        # obj_type = 'target'
        # docname = 'docname'
        # anchor = 'anchor'
        # priority = 1
        # breakpoint()
        #
        # object_tuple = (name, dispname, obj_type, docname, anchor, priority)
        # objects.append(object_tuple)
        # return objects
        
        # for refname, (docname, type, _) in self.data['objects'].items():
        

    def clear_doc(self, docname):
        objects = dict(self.data['objects'])

        for fullname, (fn, _) in objects.items():
            if fn == docname:
                del self.data['objects'][fullname]