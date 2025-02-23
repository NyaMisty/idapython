# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any

R_cs: int
R_ds: int
R_es: int
R_fs: int
R_gs: int
R_ss: int
SR_auto: int
SR_autostart: int
SR_inherit: int
SR_user: int
SWIG_PYTHON_LEGACY_BOOL: int

def copy_sreg_ranges(dst_rg, src_rg, map_selector=...) -> Any: ...
def del_sreg_range(ea, rg) -> bool: ...
def delete_sreg_range_t(self) -> Any: ...
def get_prev_sreg_range(out, ea, rg) -> bool: ...
def get_sreg(ea, rg) -> sel_t: ...
def get_sreg_range(out, ea, rg) -> bool: ...
def get_sreg_range_num(ea, rg) -> int: ...
def get_sreg_ranges_qty(rg) -> size_t: ...
def getn_sreg_range(out, rg, n) -> bool: ...
def new_sreg_range_t() -> sreg_range_t: ...
def set_default_dataseg(ds_sel) -> Any: ...
def set_default_sreg_value(sg, rg, value) -> bool: ...
def set_sreg_at_next_code(ea1, ea2, rg, value) -> Any: ...
def split_sreg_range(ea, rg, v, tag, silent=...) -> bool: ...
def sreg_range_t_swiginit(*args, **kwargs): ...
def sreg_range_t_swigregister(*args, **kwargs): ...
def sreg_range_t_tag_get(self) -> uchar: ...
def sreg_range_t_tag_set(self, tag) -> Any: ...
def sreg_range_t_val_get(self) -> sel_t: ...
def sreg_range_t_val_set(self, val) -> Any: ...
