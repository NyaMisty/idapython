# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

SWIG_PYTHON_LEGACY_BOOL: int
TBEA_ANY: int
TBEA_CATCH: int
TBEA_FALLTHRU: int
TBEA_SEHFILT: int
TBEA_SEHLPAD: int
TBEA_SEHTRY: int
TBEA_TRY: int
TBERR_EMPTY: int
TBERR_END: int
TBERR_INTERSECT: int
TBERR_KIND: int
TBERR_NO_CATCHES: int
TBERR_OK: int
TBERR_ORDER: int
TBERR_START: int

def add_tryblk(tb) -> int: ...
def catch_t_obj_get(self) -> sval_t: ...
def catch_t_obj_set(self, obj) -> Any: ...
def catch_t_swiginit(*args, **kwargs): ...
def catch_t_swigregister(*args, **kwargs): ...
def catch_t_type_id_get(self) -> sval_t: ...
def catch_t_type_id_set(self, type_id) -> Any: ...
def catchvec_t___eq__(self, r) -> bool: ...
def catchvec_t___getitem__(self, i) -> catch_t: ...
def catchvec_t___len__(self) -> size_t: ...
def catchvec_t___ne__(self, r) -> bool: ...
def catchvec_t___setitem__(self, i, v) -> Any: ...
def catchvec_t__del(self, x) -> bool: ...
def catchvec_t_add_unique(self, x) -> bool: ...
def catchvec_t_at(self, _idx) -> catch_t: ...
@overload
def catchvec_t_begin(self) -> catch_t: ...
@overload
def catchvec_t_begin(self) -> catch_t: ...
def catchvec_t_capacity(self) -> size_t: ...
def catchvec_t_clear(self) -> Any: ...
def catchvec_t_empty(self) -> bool: ...
@overload
def catchvec_t_end(self) -> catch_t: ...
@overload
def catchvec_t_end(self) -> catch_t: ...
@overload
def catchvec_t_erase(self, it) -> catch_t: ...
@overload
def catchvec_t_erase(self, first, last) -> catch_t: ...
def catchvec_t_extract(self) -> catch_t: ...
@overload
def catchvec_t_find(self, x) -> catch_t: ...
@overload
def catchvec_t_find(self, x) -> catch_t: ...
def catchvec_t_grow(self, x=...) -> Any: ...
def catchvec_t_has(self, x) -> bool: ...
def catchvec_t_inject(self, s, len) -> Any: ...
def catchvec_t_insert(self, it, x) -> catch_t: ...
def catchvec_t_pop_back(self) -> Any: ...
@overload
def catchvec_t_push_back(self, x) -> Any: ...
@overload
def catchvec_t_push_back(self) -> catch_t: ...
def catchvec_t_qclear(self) -> Any: ...
def catchvec_t_reserve(self, cnt) -> Any: ...
@overload
def catchvec_t_resize(self, _newsize, x) -> Any: ...
@overload
def catchvec_t_resize(self, _newsize) -> Any: ...
def catchvec_t_size(self) -> size_t: ...
def catchvec_t_swap(self, r) -> Any: ...
def catchvec_t_swiginit(*args, **kwargs): ...
def catchvec_t_swigregister(*args, **kwargs): ...
def catchvec_t_truncate(self) -> Any: ...
def del_tryblks(range) -> Any: ...
def delete_catch_t(self) -> Any: ...
def delete_catchvec_t(self) -> Any: ...
def delete_seh_t(self) -> Any: ...
def delete_try_handler_t(self) -> Any: ...
def delete_tryblk_t(self) -> Any: ...
def delete_tryblks_t(self) -> Any: ...
def find_syseh(ea) -> ea_t: ...
def get_tryblks(tbv, range) -> size_t: ...
def is_ea_tryblks(ea, flags) -> bool: ...
def new_catch_t() -> catch_t: ...
def new_catchvec_t(x) -> catchvec_t: ...
def new_seh_t() -> seh_t: ...
def new_try_handler_t() -> try_handler_t: ...
def new_tryblk_t(r) -> tryblk_t: ...
def new_tryblks_t(x) -> tryblks_t: ...
def seh_t_clear(self) -> Any: ...
def seh_t_filter_get(self) -> rangevec_t: ...
def seh_t_filter_set(self, filter) -> Any: ...
def seh_t_seh_code_get(self) -> ea_t: ...
def seh_t_seh_code_set(self, seh_code) -> Any: ...
def seh_t_swiginit(*args, **kwargs): ...
def seh_t_swigregister(*args, **kwargs): ...
def try_handler_t_clear(self) -> Any: ...
def try_handler_t_disp_get(self) -> sval_t: ...
def try_handler_t_disp_set(self, disp) -> Any: ...
def try_handler_t_fpreg_get(self) -> int: ...
def try_handler_t_fpreg_set(self, fpreg) -> Any: ...
def try_handler_t_swiginit(*args, **kwargs): ...
def try_handler_t_swigregister(*args, **kwargs): ...
def tryblk_t_clear(self) -> Any: ...
def tryblk_t_cpp(self) -> catchvec_t: ...
def tryblk_t_empty(self) -> bool: ...
def tryblk_t_get_kind(self) -> uchar: ...
def tryblk_t_is_cpp(self) -> bool: ...
def tryblk_t_is_seh(self) -> bool: ...
def tryblk_t_level_get(self) -> uchar: ...
def tryblk_t_level_set(self, level) -> Any: ...
def tryblk_t_seh(self) -> seh_t: ...
def tryblk_t_set_cpp(self) -> catchvec_t: ...
def tryblk_t_set_seh(self) -> seh_t: ...
def tryblk_t_swiginit(*args, **kwargs): ...
def tryblk_t_swigregister(*args, **kwargs): ...
def tryblks_t___eq__(self, r) -> bool: ...
def tryblks_t___getitem__(self, i) -> tryblk_t: ...
def tryblks_t___len__(self) -> size_t: ...
def tryblks_t___ne__(self, r) -> bool: ...
def tryblks_t___setitem__(self, i, v) -> Any: ...
def tryblks_t__del(self, x) -> bool: ...
def tryblks_t_add_unique(self, x) -> bool: ...
def tryblks_t_at(self, _idx) -> tryblk_t: ...
@overload
def tryblks_t_begin(self) -> tryblk_t: ...
@overload
def tryblks_t_begin(self) -> tryblk_t: ...
def tryblks_t_capacity(self) -> size_t: ...
def tryblks_t_clear(self) -> Any: ...
def tryblks_t_empty(self) -> bool: ...
@overload
def tryblks_t_end(self) -> tryblk_t: ...
@overload
def tryblks_t_end(self) -> tryblk_t: ...
@overload
def tryblks_t_erase(self, it) -> tryblk_t: ...
@overload
def tryblks_t_erase(self, first, last) -> tryblk_t: ...
def tryblks_t_extract(self) -> tryblk_t: ...
@overload
def tryblks_t_find(self, x) -> tryblk_t: ...
@overload
def tryblks_t_find(self, x) -> tryblk_t: ...
def tryblks_t_grow(self, x=...) -> Any: ...
def tryblks_t_has(self, x) -> bool: ...
def tryblks_t_inject(self, s, len) -> Any: ...
def tryblks_t_insert(self, it, x) -> tryblk_t: ...
def tryblks_t_pop_back(self) -> Any: ...
@overload
def tryblks_t_push_back(self, x) -> Any: ...
@overload
def tryblks_t_push_back(self) -> tryblk_t: ...
def tryblks_t_qclear(self) -> Any: ...
def tryblks_t_reserve(self, cnt) -> Any: ...
@overload
def tryblks_t_resize(self, _newsize, x) -> Any: ...
@overload
def tryblks_t_resize(self, _newsize) -> Any: ...
def tryblks_t_size(self) -> size_t: ...
def tryblks_t_swap(self, r) -> Any: ...
def tryblks_t_swiginit(*args, **kwargs): ...
def tryblks_t_swigregister(*args, **kwargs): ...
def tryblks_t_truncate(self) -> Any: ...
