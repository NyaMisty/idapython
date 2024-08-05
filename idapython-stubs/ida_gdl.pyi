# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"
import ida_range
from _typeshed import Incomplete
from collections.abc import Generator

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete
fcb_normal: Incomplete
fcb_indjump: Incomplete
fcb_ret: Incomplete
fcb_cndret: Incomplete
fcb_noret: Incomplete
fcb_enoret: Incomplete
fcb_extern: Incomplete
fcb_error: Incomplete

class node_iterator:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def __ref__(self, *args) -> int: ...
    __swig_destroy__: Incomplete

class gdl_graph_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    __swig_destroy__: Incomplete
    def get_node_label(self, *args) -> 'char *': ...
    def print_graph_attributes(self, *args) -> None: ...
    def print_node(self, *args) -> bool: ...
    def print_edge(self, *args) -> bool: ...
    def print_node_attributes(self, *args) -> None: ...
    def size(self, *args) -> int: ...
    def node_qty(self, *args) -> int: ...
    def exists(self, *args) -> bool: ...
    def entry(self, *args) -> int: ...
    def exit(self, *args) -> int: ...
    def nsucc(self, *args) -> int: ...
    def npred(self, *args) -> int: ...
    def succ(self, *args) -> int: ...
    def pred(self, *args) -> int: ...
    def empty(self, *args) -> bool: ...
    def get_node_color(self, *args) -> bgcolor_t: ...
    def get_edge_color(self, *args) -> bgcolor_t: ...
    def nedge(self, *args) -> size_t: ...
    def edge(self, *args) -> int: ...
    def front(self, *args) -> int: ...
    def begin(self, *args) -> node_iterator: ...
    def end(self, *args) -> node_iterator: ...
    def __init__(self, *args) -> None: ...
    def __disown__(self): ...

def gen_gdl(*args) -> None: ...
def display_gdl(*args) -> int: ...
def gen_flow_graph(*args) -> bool: ...

CHART_PRINT_NAMES: Incomplete
CHART_GEN_DOT: Incomplete
CHART_GEN_GDL: Incomplete
CHART_WINGRAPH: Incomplete

def gen_simple_call_chart(*args) -> bool: ...
def gen_complex_call_chart(*args) -> bool: ...

CHART_NOLIBFUNCS: Incomplete
CHART_REFERENCING: Incomplete
CHART_REFERENCED: Incomplete
CHART_RECURSIVE: Incomplete
CHART_FOLLOW_DIRECTION: Incomplete
CHART_IGNORE_XTRN: Incomplete
CHART_IGNORE_DATA_BSS: Incomplete
CHART_IGNORE_LIB_TO: Incomplete
CHART_IGNORE_LIB_FROM: Incomplete
CHART_PRINT_COMMENTS: Incomplete
CHART_PRINT_DOTS: Incomplete

class cancellable_graph_t(gdl_graph_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    cancelled: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def __disown__(self): ...

class qbasic_block_t(ida_range.range_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def is_noret_block(*args) -> bool: ...
def is_ret_block(*args) -> bool: ...

FC_PRINT: Incomplete
FC_NOEXT: Incomplete
FC_RESERVED: Incomplete
FC_APPND: Incomplete
FC_CHKBREAK: Incomplete
FC_CALL_ENDS: Incomplete
FC_NOPREDS: Incomplete
FC_OUTLINES: Incomplete

class qflow_chart_t(cancellable_graph_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    title: Incomplete
    bounds: Incomplete
    pfn: Incomplete
    flags: Incomplete
    nproper: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def create(self, *args) -> None: ...
    def append_to_flowchart(self, *args) -> None: ...
    def refresh(self, *args) -> None: ...
    def calc_block_type(self, *args) -> fc_block_type_t: ...
    def is_ret_block(self, *args) -> bool: ...
    def is_noret_block(self, *args) -> bool: ...
    def print_node_attributes(self, *args) -> None: ...
    def nsucc(self, *args) -> int: ...
    def npred(self, *args) -> int: ...
    def succ(self, *args) -> int: ...
    def pred(self, *args) -> int: ...
    def get_node_label(self, *args) -> 'char *': ...
    def size(self, *args) -> int: ...
    def print_names(self, *args) -> bool: ...
    def __getitem__(self, *args) -> 'qbasic_block_t *': ...

class BasicBlock:
    _fc: Incomplete
    id: Incomplete
    start_ea: Incomplete
    end_ea: Incomplete
    type: Incomplete
    def __init__(self, id, bb, fc) -> None: ...
    def preds(self) -> Generator[Incomplete, None, None]: ...
    def succs(self) -> Generator[Incomplete, None, None]: ...

class FlowChart:
    _q: Incomplete
    def __init__(self, f: Incomplete | None = None, bounds: Incomplete | None = None, flags: int = 0) -> None: ...
    size: Incomplete
    def refresh(self) -> None: ...
    def _getitem(self, index): ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

FC_PREDS: int
