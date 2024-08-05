# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

RANGE_KIND_FUNC: int
RANGE_KIND_HIDDEN_RANGE: int
RANGE_KIND_SEGMENT: int
RANGE_KIND_UNKNOWN: int
SWIG_PYTHON_LEGACY_BOOL: int

def array_of_rangesets___eq__(self, r) -> bool: ...
def array_of_rangesets___getitem__(self, i) -> rangeset_t: ...
def array_of_rangesets___len__(self) -> size_t: ...
def array_of_rangesets___ne__(self, r) -> bool: ...
def array_of_rangesets___setitem__(self, i, v) -> Any: ...
def array_of_rangesets__del(self, x) -> bool: ...
def array_of_rangesets_add_unique(self, x) -> bool: ...
def array_of_rangesets_at(self, _idx) -> rangeset_t: ...
@overload
def array_of_rangesets_begin(self) -> rangeset_t: ...
@overload
def array_of_rangesets_begin(self) -> rangeset_t: ...
def array_of_rangesets_capacity(self) -> size_t: ...
def array_of_rangesets_clear(self) -> Any: ...
def array_of_rangesets_empty(self) -> bool: ...
@overload
def array_of_rangesets_end(self) -> rangeset_t: ...
@overload
def array_of_rangesets_end(self) -> rangeset_t: ...
@overload
def array_of_rangesets_erase(self, it) -> rangeset_t: ...
@overload
def array_of_rangesets_erase(self, first, last) -> rangeset_t: ...
def array_of_rangesets_extract(self) -> rangeset_t: ...
@overload
def array_of_rangesets_find(self, x) -> rangeset_t: ...
@overload
def array_of_rangesets_find(self, x) -> rangeset_t: ...
def array_of_rangesets_grow(self, x=...) -> Any: ...
def array_of_rangesets_has(self, x) -> bool: ...
def array_of_rangesets_inject(self, s, len) -> Any: ...
def array_of_rangesets_insert(self, it, x) -> rangeset_t: ...
def array_of_rangesets_pop_back(self) -> Any: ...
@overload
def array_of_rangesets_push_back(self, x) -> Any: ...
@overload
def array_of_rangesets_push_back(self) -> rangeset_t: ...
def array_of_rangesets_qclear(self) -> Any: ...
def array_of_rangesets_reserve(self, cnt) -> Any: ...
@overload
def array_of_rangesets_resize(self, _newsize, x) -> Any: ...
@overload
def array_of_rangesets_resize(self, _newsize) -> Any: ...
def array_of_rangesets_size(self) -> size_t: ...
def array_of_rangesets_swap(self, r) -> Any: ...
def array_of_rangesets_swiginit(*args, **kwargs): ...
def array_of_rangesets_swigregister(*args, **kwargs): ...
def array_of_rangesets_truncate(self) -> Any: ...
def delete_array_of_rangesets(self) -> Any: ...
def delete_range_t(self) -> Any: ...
def delete_rangeset_t(self) -> Any: ...
def delete_rangevec_base_t(self) -> Any: ...
def delete_rangevec_t(self) -> Any: ...
def new_array_of_rangesets(x) -> array_of_rangesets: ...
def new_range_t(ea1=..., ea2=...) -> range_t: ...
def new_rangeset_t(ivs) -> rangeset_t: ...
def new_rangevec_base_t(x) -> rangevec_base_t: ...
def new_rangevec_t() -> rangevec_t: ...
def range_t___eq__(self, r) -> bool: ...
def range_t___ge__(self, r) -> bool: ...
def range_t___gt__(self, r) -> bool: ...
def range_t___le__(self, r) -> bool: ...
def range_t___lt__(self, r) -> bool: ...
def range_t___ne__(self, r) -> bool: ...
def range_t__print(self) -> size_t: ...
def range_t_clear(self) -> Any: ...
def range_t_compare(self, r) -> int: ...
@overload
def range_t_contains(self, ea) -> bool: ...
@overload
def range_t_contains(self, r) -> bool: ...
def range_t_empty(self) -> bool: ...
def range_t_end_ea_get(self) -> ea_t: ...
def range_t_end_ea_set(self, end_ea) -> Any: ...
def range_t_extend(self, ea) -> Any: ...
def range_t_intersect(self, r) -> Any: ...
def range_t_overlaps(self, r) -> bool: ...
def range_t_print(cb) -> size_t: ...
def range_t_size(self) -> asize_t: ...
def range_t_start_ea_get(self) -> ea_t: ...
def range_t_start_ea_set(self, start_ea) -> Any: ...
def range_t_swiginit(*args, **kwargs): ...
def range_t_swigregister(*args, **kwargs): ...
def rangeset_t___eq__(self, aset) -> bool: ...
def rangeset_t___ne__(self, aset) -> bool: ...
def rangeset_t__print(self) -> size_t: ...
@overload
def rangeset_t_add(self, range) -> bool: ...
@overload
def rangeset_t_add(self, start, _end) -> bool: ...
@overload
def rangeset_t_add(self, aset) -> bool: ...
@overload
def rangeset_t_begin(self) -> range_t: ...
@overload
def rangeset_t_begin(self) -> range_t: ...
def rangeset_t_cached_range(self) -> range_t: ...
def rangeset_t_clear(self) -> Any: ...
@overload
def rangeset_t_contains(self, ea) -> bool: ...
@overload
def rangeset_t_contains(self, aset) -> bool: ...
def rangeset_t_empty(self) -> bool: ...
@overload
def rangeset_t_end(self) -> range_t: ...
@overload
def rangeset_t_end(self) -> range_t: ...
def rangeset_t_find_range(self, ea) -> range_t: ...
def rangeset_t_getrange(self, idx) -> range_t: ...
@overload
def rangeset_t_has_common(self, range) -> bool: ...
@overload
def rangeset_t_has_common(self, aset) -> bool: ...
def rangeset_t_includes(self, range) -> bool: ...
def rangeset_t_intersect(self, aset) -> bool: ...
def rangeset_t_is_equal(self, aset) -> bool: ...
def rangeset_t_is_subset_of(self, aset) -> bool: ...
def rangeset_t_lastrange(self) -> range_t: ...
def rangeset_t_next_addr(self, ea) -> ea_t: ...
def rangeset_t_next_range(self, ea) -> ea_t: ...
def rangeset_t_nranges(self) -> size_t: ...
def rangeset_t_prev_addr(self, ea) -> ea_t: ...
def rangeset_t_prev_range(self, ea) -> ea_t: ...
@overload
def rangeset_t_sub(self, range) -> bool: ...
@overload
def rangeset_t_sub(self, ea) -> bool: ...
@overload
def rangeset_t_sub(self, aset) -> bool: ...
def rangeset_t_swap(self, r) -> Any: ...
def rangeset_t_swiginit(*args, **kwargs): ...
def rangeset_t_swigregister(*args, **kwargs): ...
def rangevec_base_t___eq__(self, r) -> bool: ...
def rangevec_base_t___getitem__(self, i) -> range_t: ...
def rangevec_base_t___len__(self) -> size_t: ...
def rangevec_base_t___ne__(self, r) -> bool: ...
def rangevec_base_t___setitem__(self, i, v) -> Any: ...
def rangevec_base_t__del(self, x) -> bool: ...
def rangevec_base_t_add_unique(self, x) -> bool: ...
def rangevec_base_t_at(self, _idx) -> range_t: ...
@overload
def rangevec_base_t_begin(self) -> range_t: ...
@overload
def rangevec_base_t_begin(self) -> range_t: ...
def rangevec_base_t_capacity(self) -> size_t: ...
def rangevec_base_t_clear(self) -> Any: ...
def rangevec_base_t_empty(self) -> bool: ...
@overload
def rangevec_base_t_end(self) -> range_t: ...
@overload
def rangevec_base_t_end(self) -> range_t: ...
@overload
def rangevec_base_t_erase(self, it) -> range_t: ...
@overload
def rangevec_base_t_erase(self, first, last) -> range_t: ...
def rangevec_base_t_extract(self) -> range_t: ...
@overload
def rangevec_base_t_find(self, x) -> range_t: ...
@overload
def rangevec_base_t_find(self, x) -> range_t: ...
def rangevec_base_t_grow(self, x=...) -> Any: ...
def rangevec_base_t_has(self, x) -> bool: ...
def rangevec_base_t_inject(self, s, len) -> Any: ...
def rangevec_base_t_insert(self, it, x) -> range_t: ...
def rangevec_base_t_pop_back(self) -> Any: ...
@overload
def rangevec_base_t_push_back(self, x) -> Any: ...
@overload
def rangevec_base_t_push_back(self) -> range_t: ...
def rangevec_base_t_qclear(self) -> Any: ...
def rangevec_base_t_reserve(self, cnt) -> Any: ...
@overload
def rangevec_base_t_resize(self, _newsize, x) -> Any: ...
@overload
def rangevec_base_t_resize(self, _newsize) -> Any: ...
def rangevec_base_t_size(self) -> size_t: ...
def rangevec_base_t_swap(self, r) -> Any: ...
def rangevec_base_t_swiginit(*args, **kwargs): ...
def rangevec_base_t_swigregister(*args, **kwargs): ...
def rangevec_base_t_truncate(self) -> Any: ...
def rangevec_t_swiginit(*args, **kwargs): ...
def rangevec_t_swigregister(*args, **kwargs): ...
