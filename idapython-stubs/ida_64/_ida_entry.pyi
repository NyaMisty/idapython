AEF_IDBENC: int
AEF_NODUMMY: int
AEF_UTF8: int
SWIG_PYTHON_LEGACY_BOOL: int

def add_entry(ord, ea, name, makecode, flags=...) -> bool: ...
def get_entry(ord) -> ea_t: ...
def get_entry_forwarder(ord) -> ssize_t: ...
def get_entry_name(ord) -> ssize_t: ...
def get_entry_ordinal(idx) -> uval_t: ...
def get_entry_qty() -> size_t: ...
def rename_entry(ord, name, flags=...) -> bool: ...
def set_entry_forwarder(ord, name, flags=...) -> bool: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"