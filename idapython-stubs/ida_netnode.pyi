# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete
BADNODE: Incomplete
SIZEOF_nodeidx_t: Incomplete

class netnode:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    @staticmethod
    def exist(*args) -> bool: ...
    def create(self, *args) -> bool: ...
    def kill(self, *args) -> None: ...
    def get_name(self, *args) -> ssize_t: ...
    def rename(self, *args) -> bool: ...
    def valobj(self, *args) -> ssize_t: ...
    def valstr(self, *args) -> ssize_t: ...
    def set(self, *args) -> bool: ...
    def delvalue(self, *args) -> bool: ...
    def set_long(self, *args) -> bool: ...
    def value_exists(self, *args) -> bool: ...
    def long_value(self, *args) -> nodeidx_t: ...
    def altval(self, *args) -> nodeidx_t: ...
    def altval_ea(self, *args) -> nodeidx_t: ...
    def altset(self, *args) -> bool: ...
    def altset_ea(self, *args) -> bool: ...
    def altdel_ea(self, *args) -> bool: ...
    def easet(self, *args) -> bool: ...
    def eaget(self, *args) -> ea_t: ...
    def eadel(self, *args) -> bool: ...
    def easet_idx(self, *args) -> bool: ...
    def eaget_idx(self, *args) -> ea_t: ...
    def easet_idx8(self, *args) -> bool: ...
    def eaget_idx8(self, *args) -> ea_t: ...
    def eadel_idx8(self, *args) -> bool: ...
    def altfirst(self, *args) -> nodeidx_t: ...
    def altnext(self, *args) -> nodeidx_t: ...
    def altlast(self, *args) -> nodeidx_t: ...
    def altprev(self, *args) -> nodeidx_t: ...
    def altshift(self, *args) -> size_t: ...
    def charval(self, *args) -> uchar: ...
    def charset(self, *args) -> bool: ...
    def chardel(self, *args) -> bool: ...
    def charval_ea(self, *args) -> uchar: ...
    def charset_ea(self, *args) -> bool: ...
    def chardel_ea(self, *args) -> bool: ...
    def charfirst(self, *args) -> nodeidx_t: ...
    def charnext(self, *args) -> nodeidx_t: ...
    def charlast(self, *args) -> nodeidx_t: ...
    def charprev(self, *args) -> nodeidx_t: ...
    def charshift(self, *args) -> size_t: ...
    def altval_idx8(self, *args) -> nodeidx_t: ...
    def altset_idx8(self, *args) -> bool: ...
    def altdel_idx8(self, *args) -> bool: ...
    def altfirst_idx8(self, *args) -> nodeidx_t: ...
    def altnext_idx8(self, *args) -> nodeidx_t: ...
    def altlast_idx8(self, *args) -> nodeidx_t: ...
    def altprev_idx8(self, *args) -> nodeidx_t: ...
    def charval_idx8(self, *args) -> uchar: ...
    def charset_idx8(self, *args) -> bool: ...
    def chardel_idx8(self, *args) -> bool: ...
    def charfirst_idx8(self, *args) -> nodeidx_t: ...
    def charnext_idx8(self, *args) -> nodeidx_t: ...
    def charlast_idx8(self, *args) -> nodeidx_t: ...
    def charprev_idx8(self, *args) -> nodeidx_t: ...
    def altdel(self, *args) -> bool: ...
    def altdel_all(self, *args) -> bool: ...
    def supval(self, *args) -> ssize_t: ...
    def supval_ea(self, *args) -> ssize_t: ...
    def supstr(self, *args) -> ssize_t: ...
    def supstr_ea(self, *args) -> ssize_t: ...
    def supdel_ea(self, *args) -> bool: ...
    def lower_bound(self, *args) -> nodeidx_t: ...
    def lower_bound_ea(self, *args) -> nodeidx_t: ...
    def supfirst(self, *args) -> nodeidx_t: ...
    def supnext(self, *args) -> nodeidx_t: ...
    def suplast(self, *args) -> nodeidx_t: ...
    def supprev(self, *args) -> nodeidx_t: ...
    def supshift(self, *args) -> size_t: ...
    def supval_idx8(self, *args) -> ssize_t: ...
    def supstr_idx8(self, *args) -> ssize_t: ...
    def supset_idx8(self, *args) -> bool: ...
    def supdel_idx8(self, *args) -> bool: ...
    def lower_bound_idx8(self, *args) -> nodeidx_t: ...
    def supfirst_idx8(self, *args) -> nodeidx_t: ...
    def supnext_idx8(self, *args) -> nodeidx_t: ...
    def suplast_idx8(self, *args) -> nodeidx_t: ...
    def supprev_idx8(self, *args) -> nodeidx_t: ...
    def supdel(self, *args) -> bool: ...
    def supdel_all(self, *args) -> bool: ...
    def supdel_range(self, *args) -> int: ...
    def supdel_range_idx8(self, *args) -> int: ...
    def hashval(self, *args) -> ssize_t: ...
    def hashstr(self, *args) -> ssize_t: ...
    def hashval_long(self, *args) -> nodeidx_t: ...
    def hashset(self, *args) -> bool: ...
    def hashset_idx(self, *args) -> bool: ...
    def hashdel(self, *args) -> bool: ...
    def hashfirst(self, *args) -> ssize_t: ...
    def hashnext(self, *args) -> ssize_t: ...
    def hashlast(self, *args) -> ssize_t: ...
    def hashprev(self, *args) -> ssize_t: ...
    def hashdel_all(self, *args) -> bool: ...
    def blobsize(self, *args) -> size_t: ...
    def blobsize_ea(self, *args) -> size_t: ...
    def setblob(self, *args) -> bool: ...
    def setblob_ea(self, *args) -> bool: ...
    def delblob(self, *args) -> int: ...
    def delblob_ea(self, *args) -> int: ...
    def blobshift(self, *args) -> size_t: ...
    def start(self, *args) -> bool: ...
    def end(self, *args) -> bool: ...
    def next(self, *args) -> bool: ...
    def prev(self, *args) -> bool: ...
    def copyto(self, *args) -> size_t: ...
    def moveto(self, *args) -> size_t: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def index(self, *args) -> nodeidx_t: ...
    def getblob(self, *args) -> 'PyObject *': ...
    def getclob(self, *args) -> 'PyObject *': ...
    def getblob_ea(self, *args) -> 'PyObject *': ...
    def hashstr_buf(self, *args) -> 'PyObject *': ...
    def hashset_buf(self, *args) -> bool: ...
    def supset(self, *args) -> bool: ...
    def supset_ea(self, *args) -> bool: ...
    __swig_destroy__: Incomplete

cvar: Incomplete
MAXNAMESIZE: Incomplete
MAX_NODENAME_SIZE: Incomplete
MAXSPECSIZE: Incomplete
atag: Incomplete
stag: Incomplete
htag: Incomplete
vtag: Incomplete
ntag: Incomplete
ltag: Incomplete
NETMAP_IDX: Incomplete
NETMAP_VAL: Incomplete
NETMAP_STR: Incomplete
NETMAP_X8: Incomplete
NETMAP_V8: Incomplete
NETMAP_VAL_NDX: Incomplete

def exist(*args) -> bool: ...
def netnode_exist(*args) -> bool: ...
