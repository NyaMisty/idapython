from typing import Any

COLOR_BG_MAX: int
COLOR_CODE: int
COLOR_CURITEM: int
COLOR_CURLINE: int
COLOR_DATA: int
COLOR_ESC: str
COLOR_EXTERN: int
COLOR_HIDLINE: int
COLOR_INV: str
COLOR_LIBFUNC: int
COLOR_LUMFUNC: int
COLOR_OFF: str
COLOR_ON: str
COLOR_REGFUNC: int
COLOR_SELECTED: int
COLOR_UNKNOWN: int
GDISMF_ADDR_TAG: int
GDISMF_AS_STACK: int
GENDSM_FORCE_CODE: int
GENDSM_MULTI_LINE: int
GENDSM_REMOVE_TAGS: int
SCOLOR_ADDR: str
SCOLOR_ALTOP: str
SCOLOR_ASMDIR: str
SCOLOR_AUTOCMT: str
SCOLOR_BINPREF: str
SCOLOR_CHAR: str
SCOLOR_CNAME: str
SCOLOR_CODNAME: str
SCOLOR_COLLAPSED: str
SCOLOR_CREF: str
SCOLOR_CREFTAIL: str
SCOLOR_DATNAME: str
SCOLOR_DCHAR: str
SCOLOR_DEFAULT: str
SCOLOR_DEMNAME: str
SCOLOR_DNAME: str
SCOLOR_DNUM: str
SCOLOR_DREF: str
SCOLOR_DREFTAIL: str
SCOLOR_DSTR: str
SCOLOR_ERROR: str
SCOLOR_ESC: str
SCOLOR_EXTRA: str
SCOLOR_HIDNAME: str
SCOLOR_IMPNAME: str
SCOLOR_INSN: str
SCOLOR_INV: str
SCOLOR_KEYWORD: str
SCOLOR_LIBNAME: str
SCOLOR_LOCNAME: str
SCOLOR_MACRO: str
SCOLOR_NUMBER: str
SCOLOR_OFF: str
SCOLOR_ON: str
SCOLOR_PREFIX: str
SCOLOR_REG: str
SCOLOR_REGCMT: str
SCOLOR_RPTCMT: str
SCOLOR_SEGNAME: str
SCOLOR_STRING: str
SCOLOR_SYMBOL: str
SCOLOR_UNAME: str
SCOLOR_UNKNAME: str
SCOLOR_VOIDOP: str
SWIG_PYTHON_LEGACY_BOOL: int
VEL_CMT: int
VEL_POST: int
cvar: Any

def add_extra_cmt(ea, isprev, format) -> bool: ...
def add_extra_line(ea, isprev, format) -> bool: ...
def add_pgm_cmt(format) -> bool: ...
def add_sourcefile(ea1, ea2, filename) -> bool: ...
def calc_bg_color(ea) -> bgcolor_t: ...
def calc_prefix_color(ea) -> color_t: ...
def create_encoding_helper(*args, **kwargs): ...
def del_extra_cmt(ea, what) -> Any: ...
def del_sourcefile(ea) -> bool: ...
def delete_extra_cmts(ea, what) -> Any: ...
def delete_user_defined_prefix_t(self) -> Any: ...
def disown_user_defined_prefix_t(*args, **kwargs): ...
def generate_disasm_line(ea, flags=...) -> bool: ...
def generate_disassembly(*args, **kwargs): ...
def get_extra_cmt(ea, what) -> ssize_t: ...
def get_first_free_extra_cmtidx(ea, start) -> int: ...
def get_sourcefile(*args, **kwargs): ...
def install_user_defined_prefix(prefix_len, udp, owner) -> bool: ...
def new_user_defined_prefix_t(_self, prefix_len, owner) -> user_defined_prefix_t: ...
def set_user_defined_prefix(*args, **kwargs): ...
def tag_addr(*args, **kwargs): ...
def tag_advance(line, cnt) -> int: ...
def tag_remove(*args, **kwargs): ...
def tag_skipcode(line) -> int: ...
def tag_skipcodes(line) -> int: ...
def tag_strlen(line) -> ssize_t: ...
def update_extra_cmt(ea, what, str) -> Any: ...
def user_defined_prefix_t_get_user_defined_prefix(self, ea, insn, lnnum, indent, line) -> Any: ...
def user_defined_prefix_t_swiginit(*args, **kwargs): ...
def user_defined_prefix_t_swigregister(*args, **kwargs): ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"