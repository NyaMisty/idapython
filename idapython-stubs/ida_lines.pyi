# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete
COLOR_ON: Incomplete
COLOR_OFF: Incomplete
COLOR_ESC: Incomplete
COLOR_INV: Incomplete
SCOLOR_ON: Incomplete
SCOLOR_OFF: Incomplete
SCOLOR_ESC: Incomplete
SCOLOR_INV: Incomplete
SCOLOR_DEFAULT: Incomplete
SCOLOR_REGCMT: Incomplete
SCOLOR_RPTCMT: Incomplete
SCOLOR_AUTOCMT: Incomplete
SCOLOR_INSN: Incomplete
SCOLOR_DATNAME: Incomplete
SCOLOR_DNAME: Incomplete
SCOLOR_DEMNAME: Incomplete
SCOLOR_SYMBOL: Incomplete
SCOLOR_CHAR: Incomplete
SCOLOR_STRING: Incomplete
SCOLOR_NUMBER: Incomplete
SCOLOR_VOIDOP: Incomplete
SCOLOR_CREF: Incomplete
SCOLOR_DREF: Incomplete
SCOLOR_CREFTAIL: Incomplete
SCOLOR_DREFTAIL: Incomplete
SCOLOR_ERROR: Incomplete
SCOLOR_PREFIX: Incomplete
SCOLOR_BINPREF: Incomplete
SCOLOR_EXTRA: Incomplete
SCOLOR_ALTOP: Incomplete
SCOLOR_HIDNAME: Incomplete
SCOLOR_LIBNAME: Incomplete
SCOLOR_LOCNAME: Incomplete
SCOLOR_CODNAME: Incomplete
SCOLOR_ASMDIR: Incomplete
SCOLOR_MACRO: Incomplete
SCOLOR_DSTR: Incomplete
SCOLOR_DCHAR: Incomplete
SCOLOR_DNUM: Incomplete
SCOLOR_KEYWORD: Incomplete
SCOLOR_REG: Incomplete
SCOLOR_IMPNAME: Incomplete
SCOLOR_SEGNAME: Incomplete
SCOLOR_UNKNAME: Incomplete
SCOLOR_CNAME: Incomplete
SCOLOR_UNAME: Incomplete
SCOLOR_COLLAPSED: Incomplete
SCOLOR_ADDR: Incomplete
COLOR_SELECTED: Incomplete
COLOR_LIBFUNC: Incomplete
COLOR_REGFUNC: Incomplete
COLOR_CODE: Incomplete
COLOR_DATA: Incomplete
COLOR_UNKNOWN: Incomplete
COLOR_EXTERN: Incomplete
COLOR_CURITEM: Incomplete
COLOR_CURLINE: Incomplete
COLOR_HIDLINE: Incomplete
COLOR_LUMFUNC: Incomplete
COLOR_BG_MAX: Incomplete

def tag_strlen(*args) -> ssize_t: ...
def calc_prefix_color(*args) -> color_t: ...
def calc_bg_color(*args) -> bgcolor_t: ...
def add_sourcefile(*args) -> bool: ...
def get_sourcefile(*args) -> 'char const *': ...
def del_sourcefile(*args) -> bool: ...
def install_user_defined_prefix(*args) -> bool: ...

class user_defined_prefix_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def get_user_defined_prefix(self, *args) -> None: ...
    def __disown__(self): ...

cvar: Incomplete
COLOR_DEFAULT: Incomplete
COLOR_REGCMT: Incomplete
COLOR_RPTCMT: Incomplete
COLOR_AUTOCMT: Incomplete
COLOR_INSN: Incomplete
COLOR_DATNAME: Incomplete
COLOR_DNAME: Incomplete
COLOR_DEMNAME: Incomplete
COLOR_SYMBOL: Incomplete
COLOR_CHAR: Incomplete
COLOR_STRING: Incomplete
COLOR_NUMBER: Incomplete
COLOR_VOIDOP: Incomplete
COLOR_CREF: Incomplete
COLOR_DREF: Incomplete
COLOR_CREFTAIL: Incomplete
COLOR_DREFTAIL: Incomplete
COLOR_ERROR: Incomplete
COLOR_PREFIX: Incomplete
COLOR_BINPREF: Incomplete
COLOR_EXTRA: Incomplete
COLOR_ALTOP: Incomplete
COLOR_HIDNAME: Incomplete
COLOR_LIBNAME: Incomplete
COLOR_LOCNAME: Incomplete
COLOR_CODNAME: Incomplete
COLOR_ASMDIR: Incomplete
COLOR_MACRO: Incomplete
COLOR_DSTR: Incomplete
COLOR_DCHAR: Incomplete
COLOR_DNUM: Incomplete
COLOR_KEYWORD: Incomplete
COLOR_REG: Incomplete
COLOR_IMPNAME: Incomplete
COLOR_SEGNAME: Incomplete
COLOR_UNKNAME: Incomplete
COLOR_CNAME: Incomplete
COLOR_UNAME: Incomplete
COLOR_COLLAPSED: Incomplete
COLOR_FG_MAX: Incomplete
COLOR_ADDR: Incomplete
COLOR_OPND1: Incomplete
COLOR_OPND2: Incomplete
COLOR_OPND3: Incomplete
COLOR_OPND4: Incomplete
COLOR_OPND5: Incomplete
COLOR_OPND6: Incomplete
COLOR_OPND7: Incomplete
COLOR_OPND8: Incomplete
COLOR_RESERVED1: Incomplete
COLOR_LUMINA: Incomplete
VEL_POST: Incomplete
VEL_CMT: Incomplete

def add_extra_line(*args) -> bool: ...
def add_extra_cmt(*args) -> bool: ...
def add_pgm_cmt(*args) -> bool: ...

GDISMF_AS_STACK: Incomplete
GDISMF_ADDR_TAG: Incomplete

def generate_disasm_line(*args) -> 'qstring *': ...

GENDSM_FORCE_CODE: Incomplete
GENDSM_MULTI_LINE: Incomplete
GENDSM_REMOVE_TAGS: Incomplete

def get_first_free_extra_cmtidx(*args) -> int: ...
def update_extra_cmt(*args) -> None: ...
def del_extra_cmt(*args) -> None: ...
def get_extra_cmt(*args) -> int: ...
def delete_extra_cmts(*args) -> None: ...
def create_encoding_helper(*args) -> 'encoder_t *': ...
def tag_remove(*args) -> 'PyObject *': ...
def set_user_defined_prefix(*args) -> 'PyObject *': ...
def tag_addr(*args) -> 'PyObject *': ...
def tag_skipcode(*args) -> int: ...
def tag_skipcodes(*args) -> int: ...
def tag_advance(*args) -> int: ...
def generate_disassembly(*args) -> 'PyObject *': ...

COLOR_ADDR_SIZE: Incomplete
SCOLOR_FG_MAX: str
SCOLOR_OPND1: Incomplete
SCOLOR_OPND2: Incomplete
SCOLOR_OPND3: Incomplete
SCOLOR_OPND4: Incomplete
SCOLOR_OPND5: Incomplete
SCOLOR_OPND6: Incomplete
SCOLOR_UTF8: Incomplete
PALETTE_SIZE: Incomplete

def requires_color_esc(c): ...
def COLSTR(str, tag): ...

E_PREV: Incomplete
E_NEXT: Incomplete
