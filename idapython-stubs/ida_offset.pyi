# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

def get_default_reftype(*args) -> reftype_t: ...
def op_offset_ex(*args) -> bool: ...
def op_offset(*args) -> bool: ...
def op_plain_offset(*args) -> bool: ...
def get_offbase(*args) -> ea_t: ...
def get_offset_expression(*args) -> 'qstring *': ...
def get_offset_expr(*args) -> 'qstring *': ...
def can_be_off32(*args) -> ea_t: ...
def calc_offset_base(*args) -> ea_t: ...
def calc_probable_base_by_value(*args) -> ea_t: ...
def calc_reference_data(*args) -> bool: ...
def add_refinfo_dref(*args) -> ea_t: ...
def calc_target(*args) -> ea_t: ...
def calc_basevalue(*args) -> ea_t: ...
