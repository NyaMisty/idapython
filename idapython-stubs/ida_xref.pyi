# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
from _typeshed import Incomplete
from collections.abc import Generator

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

def create_switch_xrefs(*args) -> bool: ...

class cases_and_targets_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    cases: Incomplete
    targets: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def calc_switch_cases(*args) -> 'cases_and_targets_t *': ...
def create_switch_table(*args) -> bool: ...

fl_U: Incomplete
fl_CF: Incomplete
fl_CN: Incomplete
fl_JF: Incomplete
fl_JN: Incomplete
fl_USobsolete: Incomplete
fl_F: Incomplete
dr_U: Incomplete
dr_O: Incomplete
dr_W: Incomplete
dr_R: Incomplete
dr_T: Incomplete
dr_I: Incomplete
dr_S: Incomplete
XREF_USER: Incomplete
XREF_TAIL: Incomplete
XREF_BASE: Incomplete
XREF_MASK: Incomplete
XREF_PASTEND: Incomplete

def xrefchar(*args) -> char: ...
def add_cref(*args) -> bool: ...
def del_cref(*args) -> bool: ...
def add_dref(*args) -> bool: ...
def del_dref(*args) -> None: ...

class xrefblk_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    frm: Incomplete
    to: Incomplete
    iscode: Incomplete
    type: Incomplete
    user: Incomplete
    def first_from(self, *args) -> bool: ...
    def first_to(self, *args) -> bool: ...
    def next_from(self, *args) -> bool: ...
    def next_to(self, *args) -> bool: ...
    def crefs_to(self, ea) -> Generator[Incomplete, None, None]: ...
    def fcrefs_to(self, ea) -> Generator[Incomplete, None, None]: ...
    def crefs_from(self, ea) -> Generator[Incomplete, None, None]: ...
    def fcrefs_from(self, ea) -> Generator[Incomplete, None, None]: ...
    def drefs_to(self, ea) -> Generator[Incomplete, None, None]: ...
    def drefs_from(self, ea) -> Generator[Incomplete, None, None]: ...
    def refs_from(self, ea, flag) -> Generator[Incomplete, None, Incomplete]: ...
    def refs_to(self, ea, flag) -> Generator[Incomplete, None, Incomplete]: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

XREF_ALL: Incomplete
XREF_FAR: Incomplete
XREF_DATA: Incomplete

def get_first_dref_from(*args) -> ea_t: ...
def get_next_dref_from(*args) -> ea_t: ...
def get_first_dref_to(*args) -> ea_t: ...
def get_next_dref_to(*args) -> ea_t: ...
def get_first_cref_from(*args) -> ea_t: ...
def get_next_cref_from(*args) -> ea_t: ...
def get_first_cref_to(*args) -> ea_t: ...
def get_next_cref_to(*args) -> ea_t: ...
def get_first_fcref_from(*args) -> ea_t: ...
def get_next_fcref_from(*args) -> ea_t: ...
def get_first_fcref_to(*args) -> ea_t: ...
def get_next_fcref_to(*args) -> ea_t: ...
def has_external_refs(*args) -> bool: ...
def delete_switch_table(*args) -> None: ...

class casevec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'qvector< long long > &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'qvector< long long > const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'qvector< long long > *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< qvector< long long > >::const_iterator': ...
    def end(self, *args) -> 'qvector< qvector< long long > >::const_iterator': ...
    def insert(self, *args) -> 'qvector< qvector< long long > >::iterator': ...
    def erase(self, *args) -> 'qvector< qvector< long long > >::iterator': ...
    def find(self, *args) -> 'qvector< qvector< long long > >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'qvector< long long > const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator