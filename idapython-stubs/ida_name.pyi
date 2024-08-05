# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class ea_name_vec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'ea_name_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'ea_name_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'ea_name_t *': ...
    def inject(self, *args) -> None: ...
    def begin(self, *args) -> 'qvector< ea_name_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< ea_name_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< ea_name_t >::iterator': ...
    def erase(self, *args) -> 'qvector< ea_name_t >::iterator': ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'ea_name_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

def get_name(*args) -> qstring: ...
def get_colored_name(*args) -> qstring: ...

MAXNAMELEN: Incomplete
FUNC_IMPORT_PREFIX: Incomplete

def set_name(*args) -> bool: ...

SN_CHECK: Incomplete
SN_NOCHECK: Incomplete
SN_PUBLIC: Incomplete
SN_NON_PUBLIC: Incomplete
SN_WEAK: Incomplete
SN_NON_WEAK: Incomplete
SN_AUTO: Incomplete
SN_NON_AUTO: Incomplete
SN_NOLIST: Incomplete
SN_NOWARN: Incomplete
SN_LOCAL: Incomplete
SN_IDBENC: Incomplete
SN_FORCE: Incomplete
SN_NODUMMY: Incomplete
SN_DELTAIL: Incomplete

def force_name(*args) -> bool: ...
def del_global_name(*args) -> bool: ...
def del_local_name(*args) -> bool: ...
def set_dummy_name(*args) -> bool: ...
def make_name_auto(*args) -> bool: ...
def make_name_user(*args) -> bool: ...

UCDR_STRLIT: Incomplete
UCDR_NAME: Incomplete
UCDR_MANGLED: Incomplete
UCDR_TYPE: Incomplete
VNT_IDENT: Incomplete
VNT_TYPE: Incomplete
VNT_UDTMEM: Incomplete
VNT_STRLIT: Incomplete
VNT_VISIBLE: Incomplete

def is_valid_cp(*args) -> bool: ...
def set_cp_validity(*args) -> None: ...
def get_cp_validity(*args) -> bool: ...
def is_ident_cp(*args) -> bool: ...
def is_strlit_cp(*args) -> bool: ...
def is_visible_cp(*args) -> bool: ...
def is_ident(*args) -> bool: ...
def is_valid_name(*args) -> bool: ...
def is_uname(*args) -> bool: ...
def is_valid_typename(*args) -> bool: ...
def extract_name(*args) -> 'qstring *': ...
def hide_name(*args) -> None: ...
def show_name(*args) -> None: ...
def get_name_ea(*args) -> ea_t: ...
def get_name_base_ea(*args) -> ea_t: ...
def get_name_value(*args) -> 'uval_t *': ...

NT_NONE: Incomplete
NT_BYTE: Incomplete
NT_LOCAL: Incomplete
NT_STKVAR: Incomplete
NT_ENUM: Incomplete
NT_ABS: Incomplete
NT_SEG: Incomplete
NT_STROFF: Incomplete
NT_BMASK: Incomplete
NT_REGVAR: Incomplete
GN_VISIBLE: Incomplete
GN_COLORED: Incomplete
GN_DEMANGLED: Incomplete
GN_STRICT: Incomplete
GN_SHORT: Incomplete
GN_LONG: Incomplete
GN_LOCAL: Incomplete
GN_ISRET: Incomplete
GN_NOT_ISRET: Incomplete
GN_NOT_DUMMY: Incomplete

def get_visible_name(*args) -> qstring: ...
def get_short_name(*args) -> qstring: ...
def get_long_name(*args) -> qstring: ...
def get_colored_short_name(*args) -> qstring: ...
def get_colored_long_name(*args) -> qstring: ...
def get_demangled_name(*args) -> qstring: ...
def get_colored_demangled_name(*args) -> qstring: ...
def get_name_color(*args) -> color_t: ...

GETN_APPZERO: Incomplete
GETN_NOFIXUP: Incomplete
GETN_NODUMMY: Incomplete

def get_name_expr(*args) -> 'qstring *': ...
def get_nice_colored_name(*args) -> 'qstring *': ...

GNCN_NOSEG: Incomplete
GNCN_NOCOLOR: Incomplete
GNCN_NOLABEL: Incomplete
GNCN_NOFUNC: Incomplete
GNCN_SEG_FUNC: Incomplete
GNCN_SEGNUM: Incomplete
GNCN_REQFUNC: Incomplete
GNCN_REQNAME: Incomplete
GNCN_NODBGNM: Incomplete
GNCN_PREFDBG: Incomplete

def append_struct_fields(*args) -> 'qstring *, adiff_t *': ...
def is_public_name(*args) -> bool: ...
def make_name_public(*args) -> None: ...
def make_name_non_public(*args) -> None: ...
def is_weak_name(*args) -> bool: ...
def make_name_weak(*args) -> None: ...
def make_name_non_weak(*args) -> None: ...
def get_nlist_size(*args) -> size_t: ...
def get_nlist_idx(*args) -> size_t: ...
def is_in_nlist(*args) -> bool: ...
def get_nlist_ea(*args) -> ea_t: ...
def get_nlist_name(*args) -> 'char const *': ...
def rebuild_nlist(*args) -> None: ...
def reorder_dummy_names(*args) -> None: ...

DEBNAME_EXACT: Incomplete
DEBNAME_LOWER: Incomplete
DEBNAME_UPPER: Incomplete
DEBNAME_NICE: Incomplete

class ea_name_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    ea: Incomplete
    name: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def set_debug_name(*args) -> bool: ...
def get_debug_name(*args) -> 'qstring *': ...
def del_debug_names(*args) -> None: ...
def get_debug_name_ea(*args) -> ea_t: ...

DQT_NPURGED_8: Incomplete
DQT_NPURGED_4: Incomplete
DQT_NPURGED_2: Incomplete
DQT_COMPILER: Incomplete
DQT_NAME_TYPE: Incomplete
DQT_FULL: Incomplete

def demangle_name(*args) -> 'qstring *': ...
def is_name_defined_locally(*args) -> bool: ...
def cleanup_name(*args) -> 'qstring *': ...

CN_KEEP_TRAILING__DIGITS: Incomplete
ME_INTERR: Incomplete
ME_PARAMERR: Incomplete
ME_ILLSTR: Incomplete
ME_SMALLANS: Incomplete
ME_FRAME: Incomplete
ME_NOCOMP: Incomplete
ME_ERRAUTO: Incomplete
ME_NOHASHMEM: Incomplete
ME_NOSTRMEM: Incomplete
ME_NOERROR_LIMIT: Incomplete
M_PRCMSK: Incomplete
MT_DEFAULT: Incomplete
MT_CDECL: Incomplete
MT_PASCAL: Incomplete
MT_STDCALL: Incomplete
MT_FASTCALL: Incomplete
MT_THISCALL: Incomplete
MT_FORTRAN: Incomplete
MT_SYSCALL: Incomplete
MT_INTERRUPT: Incomplete
MT_MSFASTCALL: Incomplete
MT_CLRCALL: Incomplete
MT_DMDCALL: Incomplete
MT_VECTORCALL: Incomplete
MT_REGCALL: Incomplete
MT_LOCALNAME: Incomplete
M_SAVEREGS: Incomplete
M_CLASS: Incomplete
MT_PUBLIC: Incomplete
MT_PRIVATE: Incomplete
MT_PROTECT: Incomplete
MT_MEMBER: Incomplete
MT_VTABLE: Incomplete
MT_RTTI: Incomplete
M_PARMSK: Incomplete
MT_PARSHF: Incomplete
MT_PARMAX: Incomplete
M_ELLIPSIS: Incomplete
MT_VOIDARG: Incomplete
M_STATIC: Incomplete
M_VIRTUAL: Incomplete
M_AUTOCRT: Incomplete
M_TYPMASK: Incomplete
MT_OPERAT: Incomplete
MT_CONSTR: Incomplete
MT_DESTR: Incomplete
MT_CASTING: Incomplete
MT_CLRCDTOR: Incomplete
M_TRUNCATE: Incomplete
M_THUNK: Incomplete
M_ANONNSP: Incomplete
M_TMPLNAM: Incomplete
M_DBGNAME: Incomplete
M_COMPILER: Incomplete
MT_MSCOMP: Incomplete
MT_BORLAN: Incomplete
MT_WATCOM: Incomplete
MT_OTHER: Incomplete
MT_GNU: Incomplete
MT_GCC3: Incomplete
MT_VISAGE: Incomplete
MNG_PTRMSK: Incomplete
MNG_DEFNEAR: Incomplete
MNG_DEFNEARANY: Incomplete
MNG_DEFFAR: Incomplete
MNG_NOPTRTYP16: Incomplete
MNG_DEFHUGE: Incomplete
MNG_DEFPTR64: Incomplete
MNG_DEFNONE: Incomplete
MNG_NOPTRTYP: Incomplete
MNG_NODEFINIT: Incomplete
MNG_NOUNDERSCORE: Incomplete
MNG_NOTYPE: Incomplete
MNG_NORETTYPE: Incomplete
MNG_NOBASEDT: Incomplete
MNG_NOCALLC: Incomplete
MNG_NOPOSTFC: Incomplete
MNG_NOSCTYP: Incomplete
MNG_NOTHROW: Incomplete
MNG_NOSTVIR: Incomplete
MNG_NOECSU: Incomplete
MNG_NOCSVOL: Incomplete
MNG_NOCLOSUR: Incomplete
MNG_NOUNALG: Incomplete
MNG_NOMANAGE: Incomplete
MNG_NOMODULE: Incomplete
MNG_SHORT_S: Incomplete
MNG_SHORT_U: Incomplete
MNG_ZPT_SPACE: Incomplete
MNG_DROP_IMP: Incomplete
MNG_IGN_ANYWAY: Incomplete
MNG_IGN_JMP: Incomplete
MNG_MOVE_JMP: Incomplete
MNG_COMPILER_MSK: Incomplete
MNG_SHORT_FORM: Incomplete
MNG_LONG_FORM: Incomplete
MNG_CALC_VALID: Incomplete

def get_mangled_name_type(*args) -> mangled_name_type_t: ...
def get_debug_names(*args) -> 'PyObject *': ...
def get_ea_name(*args) -> qstring: ...
def validate_name(*args) -> 'PyObject *': ...

class NearestName:
    def __init__(self, ea_names) -> None: ...
    _names: Incomplete
    _addrs: Incomplete
    def update(self, ea_names) -> None: ...
    def find(self, ea): ...
    def _get_item(self, index): ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

def calc_gtn_flags(fromaddr, ea): ...

cvar: Incomplete
ignore_none: Incomplete
ignore_regvar: Incomplete
ignore_llabel: Incomplete
ignore_stkvar: Incomplete
ignore_glabel: Incomplete
MANGLED_CODE: Incomplete
MANGLED_DATA: Incomplete
MANGLED_UNKNOWN: Incomplete
