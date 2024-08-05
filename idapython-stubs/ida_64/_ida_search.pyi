SEARCH_BRK: int
SEARCH_CASE: int
SEARCH_DEF: int
SEARCH_DOWN: int
SEARCH_IDENT: int
SEARCH_NEXT: int
SEARCH_NOBRK: int
SEARCH_NOSHOW: int
SEARCH_REGEX: int
SEARCH_UP: int
SEARCH_USE: int
SEARCH_USESEL: int
SWIG_PYTHON_LEGACY_BOOL: int

def find_binary(arg1, arg2, arg3, arg4, arg5) -> ea_t: ...
def find_code(ea, sflag) -> ea_t: ...
def find_data(ea, sflag) -> ea_t: ...
def find_defined(ea, sflag) -> ea_t: ...
def find_error(ea, sflag) -> ea_t: ...
def find_imm(ea, sflag, search_value) -> ea_t: ...
def find_not_func(ea, sflag) -> ea_t: ...
def find_notype(ea, sflag) -> ea_t: ...
def find_reg_access(out, start_ea, end_ea, regname, sflag) -> ea_t: ...
def find_suspop(ea, sflag) -> ea_t: ...
def find_text(start_ea, y, x, ustr, sflag) -> ea_t: ...
def find_unknown(ea, sflag) -> ea_t: ...
def search_down(sflag) -> bool: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"