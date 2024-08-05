# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

CN_KEEP_TRAILING__DIGITS: int
DEBNAME_EXACT: int
DEBNAME_LOWER: int
DEBNAME_NICE: int
DEBNAME_UPPER: int
DQT_COMPILER: int
DQT_FULL: int
DQT_NAME_TYPE: int
DQT_NPURGED_2: int
DQT_NPURGED_4: int
DQT_NPURGED_8: int
FUNC_IMPORT_PREFIX: str
GETN_APPZERO: int
GETN_NODUMMY: int
GETN_NOFIXUP: int
GNCN_NOCOLOR: int
GNCN_NODBGNM: int
GNCN_NOFUNC: int
GNCN_NOLABEL: int
GNCN_NOSEG: int
GNCN_PREFDBG: int
GNCN_REQFUNC: int
GNCN_REQNAME: int
GNCN_SEGNUM: int
GNCN_SEG_FUNC: int
GN_COLORED: int
GN_DEMANGLED: int
GN_ISRET: int
GN_LOCAL: int
GN_LONG: int
GN_NOT_DUMMY: int
GN_NOT_ISRET: int
GN_SHORT: int
GN_STRICT: int
GN_VISIBLE: int
MAXNAMELEN: int
ME_ERRAUTO: int
ME_FRAME: int
ME_ILLSTR: int
ME_INTERR: int
ME_NOCOMP: int
ME_NOERROR_LIMIT: int
ME_NOHASHMEM: int
ME_NOSTRMEM: int
ME_PARAMERR: int
ME_SMALLANS: int
MNG_CALC_VALID: int
MNG_COMPILER_MSK: int
MNG_DEFFAR: int
MNG_DEFHUGE: int
MNG_DEFNEAR: int
MNG_DEFNEARANY: int
MNG_DEFNONE: int
MNG_DEFPTR64: int
MNG_DROP_IMP: int
MNG_IGN_ANYWAY: int
MNG_IGN_JMP: int
MNG_LONG_FORM: int
MNG_MOVE_JMP: int
MNG_NOBASEDT: int
MNG_NOCALLC: int
MNG_NOCLOSUR: int
MNG_NOCSVOL: int
MNG_NODEFINIT: int
MNG_NOECSU: int
MNG_NOMANAGE: int
MNG_NOMODULE: int
MNG_NOPOSTFC: int
MNG_NOPTRTYP: int
MNG_NOPTRTYP16: int
MNG_NORETTYPE: int
MNG_NOSCTYP: int
MNG_NOSTVIR: int
MNG_NOTHROW: int
MNG_NOTYPE: int
MNG_NOUNALG: int
MNG_NOUNDERSCORE: int
MNG_PTRMSK: int
MNG_SHORT_FORM: int
MNG_SHORT_S: int
MNG_SHORT_U: int
MNG_ZPT_SPACE: int
MT_BORLAN: int
MT_CASTING: int
MT_CDECL: int
MT_CLRCALL: int
MT_CLRCDTOR: int
MT_CONSTR: int
MT_DEFAULT: int
MT_DESTR: int
MT_DMDCALL: int
MT_FASTCALL: int
MT_FORTRAN: int
MT_GCC3: int
MT_GNU: int
MT_INTERRUPT: int
MT_LOCALNAME: int
MT_MEMBER: int
MT_MSCOMP: int
MT_MSFASTCALL: int
MT_OPERAT: int
MT_OTHER: int
MT_PARMAX: int
MT_PARSHF: int
MT_PASCAL: int
MT_PRIVATE: int
MT_PROTECT: int
MT_PUBLIC: int
MT_REGCALL: int
MT_RTTI: int
MT_STDCALL: int
MT_SYSCALL: int
MT_THISCALL: int
MT_VECTORCALL: int
MT_VISAGE: int
MT_VOIDARG: int
MT_VTABLE: int
MT_WATCOM: int
M_ANONNSP: int
M_AUTOCRT: int
M_CLASS: int
M_COMPILER: int
M_DBGNAME: int
M_ELLIPSIS: int
M_PARMSK: int
M_PRCMSK: int
M_SAVEREGS: int
M_STATIC: int
M_THUNK: int
M_TMPLNAM: int
M_TRUNCATE: int
M_TYPMASK: int
M_VIRTUAL: int
NT_ABS: int
NT_BMASK: int
NT_BYTE: int
NT_ENUM: int
NT_LOCAL: int
NT_NONE: int
NT_REGVAR: int
NT_SEG: int
NT_STKVAR: int
NT_STROFF: int
SN_AUTO: int
SN_CHECK: int
SN_DELTAIL: int
SN_FORCE: int
SN_IDBENC: int
SN_LOCAL: int
SN_NOCHECK: int
SN_NODUMMY: int
SN_NOLIST: int
SN_NON_AUTO: int
SN_NON_PUBLIC: int
SN_NON_WEAK: int
SN_NOWARN: int
SN_PUBLIC: int
SN_WEAK: int
SWIG_PYTHON_LEGACY_BOOL: int
UCDR_MANGLED: int
UCDR_NAME: int
UCDR_STRLIT: int
UCDR_TYPE: int
VNT_IDENT: int
VNT_STRLIT: int
VNT_TYPE: int
VNT_UDTMEM: int
VNT_VISIBLE: int
cvar: Any

def append_struct_fields(disp, n, path, flags, delta, appzero) -> flags64_t: ...
def cleanup_name(ea, name, flags=...) -> bool: ...
def del_debug_names(ea1, ea2) -> Any: ...
def del_global_name(ea) -> bool: ...
def del_local_name(ea) -> bool: ...
def delete_ea_name_t(self) -> Any: ...
def delete_ea_name_vec_t(self) -> Any: ...
def demangle_name(name, disable_mask, demreq=...) -> int32: ...
def ea_name_t_ea_get(self) -> ea_t: ...
def ea_name_t_ea_set(self, ea) -> Any: ...
def ea_name_t_name_get(*args, **kwargs): ...
def ea_name_t_name_set(self, name) -> Any: ...
def ea_name_t_swiginit(*args, **kwargs): ...
def ea_name_t_swigregister(*args, **kwargs): ...
def ea_name_vec_t___getitem__(self, i) -> ea_name_t: ...
def ea_name_vec_t___len__(self) -> size_t: ...
def ea_name_vec_t___setitem__(self, i, v) -> Any: ...
def ea_name_vec_t_at(self, _idx) -> ea_name_t: ...
@overload
def ea_name_vec_t_begin(self) -> ea_name_t: ...
@overload
def ea_name_vec_t_begin(self) -> ea_name_t: ...
def ea_name_vec_t_capacity(self) -> size_t: ...
def ea_name_vec_t_clear(self) -> Any: ...
def ea_name_vec_t_empty(self) -> bool: ...
@overload
def ea_name_vec_t_end(self) -> ea_name_t: ...
@overload
def ea_name_vec_t_end(self) -> ea_name_t: ...
@overload
def ea_name_vec_t_erase(self, it) -> ea_name_t: ...
@overload
def ea_name_vec_t_erase(self, first, last) -> ea_name_t: ...
def ea_name_vec_t_extract(self) -> ea_name_t: ...
def ea_name_vec_t_grow(self, x=...) -> Any: ...
def ea_name_vec_t_inject(self, s, len) -> Any: ...
def ea_name_vec_t_insert(self, it, x) -> ea_name_t: ...
def ea_name_vec_t_pop_back(self) -> Any: ...
@overload
def ea_name_vec_t_push_back(self, x) -> Any: ...
@overload
def ea_name_vec_t_push_back(self) -> ea_name_t: ...
def ea_name_vec_t_qclear(self) -> Any: ...
def ea_name_vec_t_reserve(self, cnt) -> Any: ...
@overload
def ea_name_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def ea_name_vec_t_resize(self, _newsize) -> Any: ...
def ea_name_vec_t_size(self) -> size_t: ...
def ea_name_vec_t_swap(self, r) -> Any: ...
def ea_name_vec_t_swiginit(*args, **kwargs): ...
def ea_name_vec_t_swigregister(*args, **kwargs): ...
def ea_name_vec_t_truncate(self) -> Any: ...
def extract_name(line, x) -> ssize_t: ...
def force_name(ea, name, flags=...) -> bool: ...
def get_colored_demangled_name(ea, inhibitor, demform, gtn_flags=...) -> qstring: ...
def get_colored_long_name(ea, gtn_flags=...) -> qstring: ...
def get_colored_name(ea) -> qstring: ...
def get_colored_short_name(ea, gtn_flags=...) -> qstring: ...
def get_cp_validity(kind, cp, endcp=...) -> bool: ...
def get_debug_name(ea_ptr, how) -> ssize_t: ...
def get_debug_name_ea(name) -> ea_t: ...
def get_debug_names(names, ea1, ea2) -> Any: ...
def get_demangled_name(ea, inhibitor, demform, gtn_flags=...) -> qstring: ...
def get_ea_name(ea, gtn_flags=...) -> qstring: ...
def get_long_name(ea, gtn_flags=...) -> qstring: ...
def get_mangled_name_type(name) -> mangled_name_type_t: ...
def get_name(ea) -> qstring: ...
def get_name_base_ea(_from, to) -> ea_t: ...
def get_name_color(_from, ea) -> color_t: ...
def get_name_ea(_from, name) -> ea_t: ...
def get_name_expr(_from, n, ea, off, flags=...) -> ssize_t: ...
def get_name_value(_from, name) -> int: ...
def get_nice_colored_name(ea, flags=...) -> ssize_t: ...
def get_nlist_ea(idx) -> ea_t: ...
def get_nlist_idx(ea) -> size_t: ...
def get_nlist_name(*args, **kwargs): ...
def get_nlist_size() -> size_t: ...
def get_short_name(ea, gtn_flags=...) -> qstring: ...
def get_visible_name(ea, gtn_flags=...) -> qstring: ...
def hide_name(ea) -> Any: ...
def is_ident(name) -> bool: ...
def is_ident_cp(cp) -> bool: ...
def is_in_nlist(ea) -> bool: ...
def is_name_defined_locally(pfn, name, ignore_name_def, ea1=..., ea2=...) -> bool: ...
def is_public_name(ea) -> bool: ...
def is_strlit_cp(cp, specific_ranges=...) -> bool: ...
def is_uname(name) -> bool: ...
def is_valid_cp(cp, kind, data=...) -> bool: ...
def is_valid_name(name, cpuregs_permitted) -> bool: ...
def is_valid_typename(name) -> bool: ...
def is_visible_cp(cp) -> bool: ...
def is_weak_name(ea) -> bool: ...
def make_name_auto(ea) -> bool: ...
def make_name_non_public(ea) -> Any: ...
def make_name_non_weak(ea) -> Any: ...
def make_name_public(ea) -> Any: ...
def make_name_user(ea) -> bool: ...
def make_name_weak(ea) -> Any: ...
def new_ea_name_t(_ea, _name) -> ea_name_t: ...
def new_ea_name_vec_t(x) -> ea_name_vec_t: ...
def rebuild_nlist() -> Any: ...
def reorder_dummy_names() -> Any: ...
def set_cp_validity(kind, cp, endcp=..., valid=...) -> Any: ...
def set_debug_name(ea, name) -> bool: ...
def set_dummy_name(_from, ea) -> bool: ...
def set_name(ea, name, flags=...) -> bool: ...
def show_name(ea) -> Any: ...
def validate_name(*args, **kwargs): ...
