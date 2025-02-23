from typing import Any

SWIG_PYTHON_LEGACY_BOOL: int

def build_strlist() -> Any: ...
def clear_strlist() -> Any: ...
def delete_string_info_t(self) -> Any: ...
def delete_strwinsetup_t(self) -> Any: ...
def get_strlist_item(si, n) -> bool: ...
def get_strlist_options() -> strwinsetup_t: ...
def get_strlist_qty() -> size_t: ...
def new_string_info_t(_ea=...) -> string_info_t: ...
def new_strwinsetup_t() -> strwinsetup_t: ...
def string_info_t___lt__(self, r) -> bool: ...
def string_info_t_ea_get(self) -> ea_t: ...
def string_info_t_ea_set(self, ea) -> Any: ...
def string_info_t_length_get(self) -> int: ...
def string_info_t_length_set(self, length) -> Any: ...
def string_info_t_swiginit(*args, **kwargs): ...
def string_info_t_swigregister(*args, **kwargs): ...
def string_info_t_type_get(self) -> int: ...
def string_info_t_type_set(self, type) -> Any: ...
def strwinsetup_t__get_strtypes(*args, **kwargs): ...
def strwinsetup_t__set_strtypes(*args, **kwargs): ...
def strwinsetup_t_display_only_existing_strings_get(self) -> uchar: ...
def strwinsetup_t_display_only_existing_strings_set(self, display_only_existing_strings) -> Any: ...
def strwinsetup_t_ignore_heads_get(self) -> uchar: ...
def strwinsetup_t_ignore_heads_set(self, ignore_heads) -> Any: ...
def strwinsetup_t_minlen_get(self) -> sval_t: ...
def strwinsetup_t_minlen_set(self, minlen) -> Any: ...
def strwinsetup_t_only_7bit_get(self) -> uchar: ...
def strwinsetup_t_only_7bit_set(self, only_7bit) -> Any: ...
def strwinsetup_t_swiginit(*args, **kwargs): ...
def strwinsetup_t_swigregister(*args, **kwargs): ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"