from typing import Any

DEFMASK: int
ENFL_REGEX: int
ENUM_MEMBER_ERROR_ENUM: int
ENUM_MEMBER_ERROR_ILLV: int
ENUM_MEMBER_ERROR_MASK: int
ENUM_MEMBER_ERROR_NAME: int
ENUM_MEMBER_ERROR_VALUE: int
SWIG_PYTHON_LEGACY_BOOL: int
cvar: Any

def add_enum(idx, name, flag) -> enum_t: ...
def add_enum_member(id, name, value, bmask=...) -> int: ...
def del_enum(id) -> Any: ...
def del_enum_member(id, value, serial, bmask) -> bool: ...
def delete_enum_member_visitor_t(self) -> Any: ...
def disown_enum_member_visitor_t(*args, **kwargs): ...
def enum_member_visitor_t_swiginit(*args, **kwargs): ...
def enum_member_visitor_t_swigregister(*args, **kwargs): ...
def enum_member_visitor_t_visit_enum_member(self, cid, value) -> int: ...
def for_all_enum_members(id, cv) -> int: ...
def get_bmask_cmt(id, bmask, repeatable) -> ssize_t: ...
def get_bmask_name(id, bmask) -> ssize_t: ...
def get_enum(name) -> enum_t: ...
def get_enum_cmt(id, repeatable) -> ssize_t: ...
def get_enum_flag(id) -> flags64_t: ...
def get_enum_idx(id) -> uval_t: ...
def get_enum_member(id, value, serial, mask) -> const_t: ...
def get_enum_member_bmask(id) -> bmask_t: ...
def get_enum_member_by_name(name) -> const_t: ...
def get_enum_member_cmt(id, repeatable) -> ssize_t: ...
def get_enum_member_enum(id) -> enum_t: ...
def get_enum_member_name(id) -> ssize_t: ...
def get_enum_member_serial(cid) -> uchar: ...
def get_enum_member_value(id) -> uval_t: ...
def get_enum_name(id) -> ssize_t: ...
def get_enum_name2(id, flags=...) -> ssize_t: ...
def get_enum_qty() -> size_t: ...
def get_enum_size(id) -> size_t: ...
def get_enum_type_ordinal(id) -> int32: ...
def get_enum_width(id) -> size_t: ...
def get_first_bmask(enum_id) -> bmask_t: ...
def get_first_enum_member(id, bmask=...) -> uval_t: ...
def get_first_serial_enum_member(id, value, bmask) -> const_t: ...
def get_last_bmask(enum_id) -> bmask_t: ...
def get_last_enum_member(id, bmask=...) -> uval_t: ...
def get_last_serial_enum_member(id, value, bmask) -> const_t: ...
def get_next_bmask(enum_id, bmask) -> bmask_t: ...
def get_next_enum_member(id, value, bmask=...) -> uval_t: ...
def get_next_serial_enum_member(in_out_serial, first_cid) -> const_t: ...
def get_prev_bmask(enum_id, bmask) -> bmask_t: ...
def get_prev_enum_member(id, value, bmask=...) -> uval_t: ...
def get_prev_serial_enum_member(in_out_serial, first_cid) -> const_t: ...
def getn_enum(idx) -> enum_t: ...
def is_bf(id) -> bool: ...
def is_enum_fromtil(id) -> bool: ...
def is_enum_hidden(id) -> bool: ...
def is_ghost_enum(id) -> bool: ...
def is_one_bit_mask(mask) -> bool: ...
def new_enum_member_visitor_t(_self) -> enum_member_visitor_t: ...
def set_bmask_cmt(id, bmask, cmt, repeatable) -> bool: ...
def set_bmask_name(id, bmask, name) -> bool: ...
def set_enum_bf(id, bf) -> bool: ...
def set_enum_cmt(id, cmt, repeatable) -> bool: ...
def set_enum_flag(id, flag) -> bool: ...
def set_enum_fromtil(id, fromtil) -> bool: ...
def set_enum_ghost(id, ghost) -> bool: ...
def set_enum_hidden(id, hidden) -> bool: ...
def set_enum_idx(id, idx) -> bool: ...
def set_enum_member_cmt(id, cmt, repeatable) -> bool: ...
def set_enum_member_name(id, name) -> bool: ...
def set_enum_name(id, name) -> bool: ...
def set_enum_type_ordinal(id, ord) -> Any: ...
def set_enum_width(id, width) -> bool: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"