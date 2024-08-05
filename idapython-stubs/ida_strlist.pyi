# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class strwinsetup_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    minlen: Incomplete
    display_only_existing_strings: Incomplete
    only_7bit: Incomplete
    ignore_heads: Incomplete
    def _get_strtypes(self, *args) -> 'PyObject *': ...
    def _set_strtypes(self, *args) -> 'PyObject *': ...
    strtypes: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class string_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    ea: Incomplete
    length: Incomplete
    type: Incomplete
    def __init__(self, *args) -> None: ...
    def __lt__(self, *args) -> bool: ...
    __swig_destroy__: Incomplete

def get_strlist_options(*args) -> 'strwinsetup_t const *': ...
def build_strlist(*args) -> None: ...
def clear_strlist(*args) -> None: ...
def get_strlist_qty(*args) -> size_t: ...
def get_strlist_item(*args) -> bool: ...