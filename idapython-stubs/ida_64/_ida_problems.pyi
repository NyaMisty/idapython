from typing import Any

SWIG_PYTHON_LEGACY_BOOL: int
cvar: Any

def forget_problem(type, ea) -> bool: ...
def get_problem(type, lowea) -> ea_t: ...
def get_problem_desc(t, ea) -> ssize_t: ...
def get_problem_name(*args, **kwargs): ...
def is_problem_present(t, ea) -> bool: ...
def remember_problem(type, ea, msg=...) -> Any: ...
def was_ida_decision(ea) -> bool: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"