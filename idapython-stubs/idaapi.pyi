# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from ida_hexrays import *
from ida_allins import *
from ida_auto import *
from ida_bitrange import *
from ida_bytes import *
from ida_dbg import *
from ida_diskio import *
from ida_dirtree import *
from ida_entry import *
from ida_enum import *
from ida_expr import *
from ida_fixup import *
from ida_fpro import *
from ida_frame import *
from ida_funcs import *
from ida_gdl import *
from ida_graph import *
from ida_ida import *
from ida_idaapi import *
from ida_idc import *
from ida_idd import *
from ida_idp import *
from ida_ieee import *
from ida_kernwin import *
from ida_lines import *
from ida_loader import *
from ida_moves import *
from ida_nalt import *
from ida_name import *
from ida_netnode import *
from ida_offset import *
from ida_pro import *
from ida_problems import *
from ida_range import *
from ida_registry import *
from ida_regfinder import *
from ida_search import *
from ida_segment import *
from ida_segregs import *
from ida_srclang import *
from ida_strlist import *
from ida_struct import *
from ida_tryblks import *
from ida_typeinf import *
from ida_ua import *
from ida_xref import *
from _typeshed import Incomplete
from ida_dbg import dbg_can_query as dbg_can_query
from ida_funcs import set_func_end as set_func_end, set_func_start as set_func_start

class idaapi_Cvar:
    def __init__(self) -> None: ...
    def _get_module_cvar(self, modname): ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...

cvar: Incomplete
