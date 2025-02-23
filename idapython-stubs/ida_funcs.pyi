# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
import ida_range
from _typeshed import Incomplete
from collections.abc import Generator

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class dyn_stkpnt_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'stkpnt_t const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

class dyn_regvar_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'regvar_t const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

class dyn_range_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'range_t const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

class dyn_ea_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'unsigned long long const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

class dyn_regarg_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'regarg_t const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

def free_regarg(*args) -> None: ...

class regarg_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    reg: Incomplete
    type: Incomplete
    name: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def swap(self, *args) -> None: ...

class func_t(ida_range.range_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    flags: Incomplete
    def is_far(self, *args) -> bool: ...
    def does_return(self, *args) -> bool: ...
    def analyzed_sp(self, *args) -> bool: ...
    def need_prolog_analysis(self, *args) -> bool: ...
    frame: Incomplete
    frsize: Incomplete
    frregs: Incomplete
    argsize: Incomplete
    fpd: Incomplete
    color: Incomplete
    pntqty: Incomplete
    points: Incomplete
    regvarqty: Incomplete
    regvars: Incomplete
    regargqty: Incomplete
    regargs: Incomplete
    tailqty: Incomplete
    tails: Incomplete
    owner: Incomplete
    refqty: Incomplete
    referers: Incomplete
    def __init__(self, *args) -> None: ...
    def __get_points__(self, *args) -> 'dynamic_wrapped_array_t< stkpnt_t >': ...
    def __get_regvars__(self, *args) -> 'dynamic_wrapped_array_t< regvar_t >': ...
    def __get_tails__(self, *args) -> 'dynamic_wrapped_array_t< range_t >': ...
    def __get_referers__(self, *args) -> 'dynamic_wrapped_array_t< ea_t >': ...
    def __get_regargs__(self, *args) -> 'dynamic_wrapped_array_t< regarg_t >': ...
    def addresses(self) -> Generator[Incomplete, Incomplete, None]: ...
    def code_items(self) -> Generator[Incomplete, Incomplete, None]: ...
    def data_items(self) -> Generator[Incomplete, Incomplete, None]: ...
    def head_items(self) -> Generator[Incomplete, Incomplete, None]: ...
    def not_tails(self) -> Generator[Incomplete, Incomplete, None]: ...
    def __iter__(self): ...
    __swig_destroy__: Incomplete

FUNC_NORET: Incomplete
FUNC_FAR: Incomplete
FUNC_LIB: Incomplete
FUNC_STATICDEF: Incomplete
FUNC_FRAME: Incomplete
FUNC_USERFAR: Incomplete
FUNC_HIDDEN: Incomplete
FUNC_THUNK: Incomplete
FUNC_BOTTOMBP: Incomplete
FUNC_NORET_PENDING: Incomplete
FUNC_SP_READY: Incomplete
FUNC_FUZZY_SP: Incomplete
FUNC_PROLOG_OK: Incomplete
FUNC_PURGED_OK: Incomplete
FUNC_TAIL: Incomplete
FUNC_LUMINA: Incomplete
FUNC_OUTLINE: Incomplete
FUNC_REANALYZE: Incomplete

def is_func_entry(*args) -> bool: ...
def is_func_tail(*args) -> bool: ...
def lock_func_range(*args) -> None: ...

class lock_func:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class lock_func_with_tails_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def is_func_locked(*args) -> bool: ...
def get_func(*args) -> 'func_t *': ...
def get_func_chunknum(*args) -> int: ...
def func_contains(*args) -> bool: ...
def is_same_func(*args) -> bool: ...
def getn_func(*args) -> 'func_t *': ...
def get_func_qty(*args) -> size_t: ...
def get_func_num(*args) -> int: ...
def get_prev_func(*args) -> 'func_t *': ...
def get_next_func(*args) -> 'func_t *': ...
def get_func_ranges(*args) -> ea_t: ...
def get_func_cmt(*args) -> 'qstring *': ...
def set_func_cmt(*args) -> bool: ...
def update_func(*args) -> bool: ...
def add_func_ex(*args) -> bool: ...
def add_func(*args) -> bool: ...
def del_func(*args) -> bool: ...
def set_func_start(*args) -> int: ...

MOVE_FUNC_OK: Incomplete
MOVE_FUNC_NOCODE: Incomplete
MOVE_FUNC_BADSTART: Incomplete
MOVE_FUNC_NOFUNC: Incomplete
MOVE_FUNC_REFUSED: Incomplete

def set_func_end(*args) -> bool: ...
def reanalyze_function(*args) -> None: ...
def find_func_bounds(*args) -> int: ...

FIND_FUNC_NORMAL: Incomplete
FIND_FUNC_DEFINE: Incomplete
FIND_FUNC_IGNOREFN: Incomplete
FIND_FUNC_KEEPBD: Incomplete
FIND_FUNC_UNDEF: Incomplete
FIND_FUNC_OK: Incomplete
FIND_FUNC_EXIST: Incomplete

def get_func_name(*args) -> 'qstring *': ...
def calc_func_size(*args) -> asize_t: ...
def get_func_bitness(*args) -> int: ...
def get_func_bits(*args) -> int: ...
def get_func_bytes(*args) -> int: ...
def is_visible_func(*args) -> bool: ...
def is_finally_visible_func(*args) -> bool: ...
def set_visible_func(*args) -> None: ...
def set_func_name_if_jumpfunc(*args) -> int: ...
def calc_thunk_func_target(*args) -> 'ea_t *': ...
def func_does_return(*args) -> bool: ...
def reanalyze_noret_flag(*args) -> bool: ...
def set_noret_insn(*args) -> bool: ...
def get_fchunk(*args) -> 'func_t *': ...
def getn_fchunk(*args) -> 'func_t *': ...
def get_fchunk_qty(*args) -> size_t: ...
def get_fchunk_num(*args) -> int: ...
def get_prev_fchunk(*args) -> 'func_t *': ...
def get_next_fchunk(*args) -> 'func_t *': ...
def append_func_tail(*args) -> bool: ...
def remove_func_tail(*args) -> bool: ...
def set_tail_owner(*args) -> bool: ...
def func_tail_iterator_set(*args) -> bool: ...
def func_tail_iterator_set_ea(*args) -> bool: ...
def func_parent_iterator_set(*args) -> bool: ...
def f_any(*args) -> bool: ...

class func_tail_iterator_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def set(self, *args) -> bool: ...
    def set_ea(self, *args) -> bool: ...
    def set_range(self, *args) -> bool: ...
    def chunk(self, *args) -> 'range_t const &': ...
    def first(self, *args) -> bool: ...
    def last(self, *args) -> bool: ...
    def __next__(self, *args) -> bool: ...
    def prev(self, *args) -> bool: ...
    def main(self, *args) -> bool: ...
    def __iter__(self): ...
    next = __next__

class func_item_iterator_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    def set(self, *args) -> bool: ...
    def set_range(self, *args) -> bool: ...
    def first(self, *args) -> bool: ...
    def last(self, *args) -> bool: ...
    def current(self, *args) -> ea_t: ...
    def chunk(self, *args) -> 'range_t const &': ...
    def __next__(self, *args) -> bool: ...
    def prev(self, *args) -> bool: ...
    def next_addr(self, *args) -> bool: ...
    def next_head(self, *args) -> bool: ...
    def next_code(self, *args) -> bool: ...
    def next_data(self, *args) -> bool: ...
    def next_not_tail(self, *args) -> bool: ...
    def prev_addr(self, *args) -> bool: ...
    def prev_head(self, *args) -> bool: ...
    def prev_code(self, *args) -> bool: ...
    def prev_data(self, *args) -> bool: ...
    def prev_not_tail(self, *args) -> bool: ...
    def decode_prev_insn(self, *args) -> bool: ...
    def decode_preceding_insn(self, *args) -> bool: ...
    def succ(self, *args) -> bool: ...
    def succ_code(self, *args) -> bool: ...
    def __iter__(self): ...
    next = __next__
    def addresses(self) -> Generator[Incomplete, None, None]: ...
    def code_items(self) -> Generator[Incomplete, None, None]: ...
    def data_items(self) -> Generator[Incomplete, None, None]: ...
    def head_items(self) -> Generator[Incomplete, None, None]: ...
    def not_tails(self) -> Generator[Incomplete, None, None]: ...
    __swig_destroy__: Incomplete

class func_parent_iterator_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def set(self, *args) -> bool: ...
    def parent(self, *args) -> ea_t: ...
    def first(self, *args) -> bool: ...
    def last(self, *args) -> bool: ...
    def __next__(self, *args) -> bool: ...
    def prev(self, *args) -> bool: ...
    def reset_fnt(self, *args) -> None: ...
    def __iter__(self): ...
    next = __next__

def get_prev_func_addr(*args) -> ea_t: ...
def get_next_func_addr(*args) -> ea_t: ...
def read_regargs(*args) -> None: ...
def add_regarg(*args) -> None: ...

IDASGN_OK: Incomplete
IDASGN_BADARG: Incomplete
IDASGN_APPLIED: Incomplete
IDASGN_CURRENT: Incomplete
IDASGN_PLANNED: Incomplete

def plan_to_apply_idasgn(*args) -> int: ...
def apply_idasgn_to(*args) -> int: ...
def get_idasgn_qty(*args) -> int: ...
def get_current_idasgn(*args) -> int: ...
def calc_idasgn_state(*args) -> int: ...
def del_idasgn(*args) -> int: ...
def get_idasgn_title(*args) -> 'qstring *': ...
def apply_startup_sig(*args) -> bool: ...
def try_to_add_libfunc(*args) -> int: ...

LIBFUNC_FOUND: Incomplete
LIBFUNC_NONE: Incomplete
LIBFUNC_DELAY: Incomplete

def get_fchunk_referer(*args) -> ea_t: ...
def get_idasgn_desc(*args) -> 'PyObject *': ...
def get_idasgn_desc_with_matches(*args) -> 'PyObject *': ...
def func_t__from_ptrval__(*args) -> 'func_t *': ...
