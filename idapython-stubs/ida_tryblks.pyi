# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
import ida_range
from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class tryblks_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'tryblk_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'tryblk_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'tryblk_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< tryblk_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< tryblk_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< tryblk_t >::iterator': ...
    def erase(self, *args) -> 'qvector< tryblk_t >::iterator': ...
    def find(self, *args) -> 'qvector< tryblk_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'tryblk_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class catchvec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'catch_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'catch_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'catch_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< catch_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< catch_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< catch_t >::iterator': ...
    def erase(self, *args) -> 'qvector< catch_t >::iterator': ...
    def find(self, *args) -> 'qvector< catch_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'catch_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class try_handler_t(ida_range.rangevec_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    disp: Incomplete
    fpreg: Incomplete
    def __init__(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class seh_t(try_handler_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    filter: Incomplete
    seh_code: Incomplete
    def clear(self, *args) -> None: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class catch_t(try_handler_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    obj: Incomplete
    type_id: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class tryblk_t(ida_range.rangevec_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    level: Incomplete
    def cpp(self, *args) -> 'catchvec_t &': ...
    def seh(self, *args) -> 'seh_t &': ...
    __swig_destroy__: Incomplete
    def __init__(self, *args) -> None: ...
    def get_kind(self, *args) -> uchar: ...
    def empty(self, *args) -> bool: ...
    def is_seh(self, *args) -> bool: ...
    def is_cpp(self, *args) -> bool: ...
    def clear(self, *args) -> None: ...
    def set_seh(self, *args) -> 'seh_t &': ...
    def set_cpp(self, *args) -> 'catchvec_t &': ...

def get_tryblks(*args) -> size_t: ...
def del_tryblks(*args) -> None: ...
def add_tryblk(*args) -> int: ...

TBERR_OK: Incomplete
TBERR_START: Incomplete
TBERR_END: Incomplete
TBERR_ORDER: Incomplete
TBERR_EMPTY: Incomplete
TBERR_KIND: Incomplete
TBERR_NO_CATCHES: Incomplete
TBERR_INTERSECT: Incomplete

def find_syseh(*args) -> ea_t: ...

TBEA_TRY: Incomplete
TBEA_CATCH: Incomplete
TBEA_SEHTRY: Incomplete
TBEA_SEHLPAD: Incomplete
TBEA_SEHFILT: Incomplete
TBEA_ANY: Incomplete
TBEA_FALLTHRU: Incomplete

def is_ea_tryblks(*args) -> bool: ...
