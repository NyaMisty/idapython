from typing import Any

SWIG_PYTHON_LEGACY_BOOL: int

def bitrange_t___eq__(self, r) -> bool: ...
def bitrange_t___ge__(self, r) -> bool: ...
def bitrange_t___gt__(self, r) -> bool: ...
def bitrange_t___le__(self, r) -> bool: ...
def bitrange_t___lt__(self, r) -> bool: ...
def bitrange_t___ne__(self, r) -> bool: ...
def bitrange_t___str__(self) -> qstring: ...
def bitrange_t_apply_mask(self, subrange) -> bool: ...
def bitrange_t_bitoff(self) -> uint: ...
def bitrange_t_bitsize(self) -> uint: ...
def bitrange_t_bytesize(self) -> uint: ...
def bitrange_t_compare(self, r) -> int: ...
def bitrange_t_create_union(self, r) -> Any: ...
def bitrange_t_empty(self) -> bool: ...
def bitrange_t_extract(self, src, is_mf) -> bool: ...
def bitrange_t_has_common(self, r) -> bool: ...
def bitrange_t_init(self, bit_ofs, size_in_bits) -> Any: ...
def bitrange_t_inject(self, dst, src, is_mf) -> bool: ...
def bitrange_t_intersect(self, r) -> Any: ...
def bitrange_t_mask64(self) -> uint64: ...
def bitrange_t_reset(self) -> Any: ...
def bitrange_t_shift_down(self, cnt) -> Any: ...
def bitrange_t_shift_up(self, cnt) -> Any: ...
def bitrange_t_sub(self, r) -> bool: ...
def bitrange_t_swiginit(*args, **kwargs): ...
def bitrange_t_swigregister(*args, **kwargs): ...
def delete_bitrange_t(self) -> Any: ...
def new_bitrange_t(bit_ofs=..., size_in_bits=...) -> bitrange_t: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"