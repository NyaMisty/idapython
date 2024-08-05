# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

def get_problem_desc(*args) -> 'qstring *': ...
def remember_problem(*args) -> None: ...
def get_problem(*args) -> ea_t: ...
def forget_problem(*args) -> bool: ...
def get_problem_name(*args) -> 'char const *': ...
def is_problem_present(*args) -> bool: ...
def was_ida_decision(*args) -> bool: ...

cvar: Incomplete
PR_NOBASE: Incomplete
PR_NONAME: Incomplete
PR_NOFOP: Incomplete
PR_NOCMT: Incomplete
PR_NOXREFS: Incomplete
PR_JUMP: Incomplete
PR_DISASM: Incomplete
PR_HEAD: Incomplete
PR_ILLADDR: Incomplete
PR_MANYLINES: Incomplete
PR_BADSTACK: Incomplete
PR_ATTN: Incomplete
PR_FINAL: Incomplete
PR_ROLLED: Incomplete
PR_COLLISION: Incomplete
PR_DECIMP: Incomplete
PR_END: Incomplete
