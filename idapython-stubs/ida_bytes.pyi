# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
import ida_range
from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class compiled_binpat_vec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'compiled_binpat_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'compiled_binpat_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'compiled_binpat_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< compiled_binpat_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< compiled_binpat_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< compiled_binpat_t >::iterator': ...
    def erase(self, *args) -> 'qvector< compiled_binpat_t >::iterator': ...
    def find(self, *args) -> 'qvector< compiled_binpat_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'compiled_binpat_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

def enable_flags(*args) -> error_t: ...
def disable_flags(*args) -> error_t: ...
def change_storage_type(*args) -> error_t: ...
def next_addr(*args) -> ea_t: ...
def prev_addr(*args) -> ea_t: ...
def next_chunk(*args) -> ea_t: ...
def prev_chunk(*args) -> ea_t: ...
def chunk_start(*args) -> ea_t: ...
def chunk_size(*args) -> asize_t: ...
def find_free_chunk(*args) -> ea_t: ...
def next_that(*args) -> ea_t: ...
def next_unknown(*args) -> ea_t: ...
def prev_that(*args) -> ea_t: ...
def prev_unknown(*args) -> ea_t: ...
def prev_head(*args) -> ea_t: ...
def next_head(*args) -> ea_t: ...
def prev_not_tail(*args) -> ea_t: ...
def next_not_tail(*args) -> ea_t: ...
def prev_visea(*args) -> ea_t: ...
def next_visea(*args) -> ea_t: ...
def get_item_head(*args) -> ea_t: ...
def get_item_end(*args) -> ea_t: ...
def calc_max_item_end(*args) -> ea_t: ...

ITEM_END_FIXUP: Incomplete
ITEM_END_INITED: Incomplete
ITEM_END_NAME: Incomplete
ITEM_END_XREF: Incomplete
ITEM_END_CANCEL: Incomplete

def get_item_size(*args) -> asize_t: ...
def is_mapped(*args) -> bool: ...
def get_flags_ex(*args) -> flags64_t: ...

GFE_VALUE: Incomplete
GFE_IDB_VALUE: Incomplete

def get_flags(*args) -> flags64_t: ...
def get_full_flags(*args) -> flags64_t: ...
def get_item_flag(*args) -> flags64_t: ...
def get_item_refinfo(*args) -> bool: ...

MS_VAL: Incomplete
FF_IVL: Incomplete

def has_value(*args) -> bool: ...
def del_value(*args) -> None: ...
def is_loaded(*args) -> bool: ...
def nbits(*args) -> int: ...
def bytesize(*args) -> int: ...
def get_byte(*args) -> uchar: ...
def get_db_byte(*args) -> uchar: ...
def get_word(*args) -> ushort: ...
def get_dword(*args) -> uint32: ...
def get_qword(*args) -> uint64: ...
def get_wide_byte(*args) -> uint64: ...
def get_wide_word(*args) -> uint64: ...
def get_wide_dword(*args) -> uint64: ...

class octet_generator_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    value: Incomplete
    ea: Incomplete
    avail_bits: Incomplete
    high_byte_first: Incomplete
    def __init__(self, *args) -> None: ...
    def invert_byte_order(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def get_octet2(*args) -> 'uchar *': ...
def get_16bit(*args) -> uint32: ...
def get_32bit(*args) -> uint32: ...
def get_64bit(*args) -> uint64: ...
def get_data_value(*args) -> bool: ...
def get_original_byte(*args) -> uint64: ...
def get_original_word(*args) -> uint64: ...
def get_original_dword(*args) -> uint64: ...
def get_original_qword(*args) -> uint64: ...
def put_byte(*args) -> bool: ...
def put_word(*args) -> None: ...
def put_dword(*args) -> None: ...
def put_qword(*args) -> None: ...
def patch_byte(*args) -> bool: ...
def patch_word(*args) -> bool: ...
def patch_dword(*args) -> bool: ...
def patch_qword(*args) -> bool: ...
def revert_byte(*args) -> bool: ...
def add_byte(*args) -> None: ...
def add_word(*args) -> None: ...
def add_dword(*args) -> None: ...
def add_qword(*args) -> None: ...
def get_zero_ranges(*args) -> bool: ...

GMB_READALL: Incomplete
GMB_WAITBOX: Incomplete

def put_bytes(*args) -> None: ...
def patch_bytes(*args) -> None: ...

MS_CLS: Incomplete
FF_CODE: Incomplete
FF_DATA: Incomplete
FF_TAIL: Incomplete
FF_UNK: Incomplete

def is_code(*args) -> bool: ...
def f_is_code(*args) -> bool: ...
def is_data(*args) -> bool: ...
def f_is_data(*args) -> bool: ...
def is_tail(*args) -> bool: ...
def f_is_tail(*args) -> bool: ...
def is_not_tail(*args) -> bool: ...
def f_is_not_tail(*args) -> bool: ...
def is_unknown(*args) -> bool: ...
def is_head(*args) -> bool: ...
def f_is_head(*args) -> bool: ...
def del_items(*args) -> bool: ...

DELIT_SIMPLE: Incomplete
DELIT_EXPAND: Incomplete
DELIT_DELNAMES: Incomplete
DELIT_NOTRUNC: Incomplete
DELIT_NOUNAME: Incomplete
DELIT_NOCMT: Incomplete
DELIT_KEEPFUNC: Incomplete

def is_manual_insn(*args) -> bool: ...
def get_manual_insn(*args) -> 'qstring *': ...
def set_manual_insn(*args) -> None: ...

MS_COMM: Incomplete
FF_COMM: Incomplete
FF_REF: Incomplete
FF_LINE: Incomplete
FF_NAME: Incomplete
FF_LABL: Incomplete
FF_FLOW: Incomplete
FF_SIGN: Incomplete
FF_BNOT: Incomplete
FF_UNUSED: Incomplete

def is_flow(*args) -> bool: ...
def has_extra_cmts(*args) -> bool: ...
def f_has_extra_cmts(*args) -> bool: ...
def has_cmt(*args) -> bool: ...
def f_has_cmt(*args) -> bool: ...
def has_xref(*args) -> bool: ...
def f_has_xref(*args) -> bool: ...
def has_name(*args) -> bool: ...
def f_has_name(*args) -> bool: ...

FF_ANYNAME: Incomplete

def has_dummy_name(*args) -> bool: ...
def f_has_dummy_name(*args) -> bool: ...
def has_auto_name(*args) -> bool: ...
def has_any_name(*args) -> bool: ...
def has_user_name(*args) -> bool: ...
def f_has_user_name(*args) -> bool: ...
def is_invsign(*args) -> bool: ...
def toggle_sign(*args) -> bool: ...
def is_bnot(*args) -> bool: ...
def toggle_bnot(*args) -> bool: ...
def is_lzero(*args) -> bool: ...
def set_lzero(*args) -> bool: ...
def clr_lzero(*args) -> bool: ...
def toggle_lzero(*args) -> bool: ...
def leading_zero_important(*args) -> bool: ...

MS_N_TYPE: Incomplete
FF_N_VOID: Incomplete
FF_N_NUMH: Incomplete
FF_N_NUMD: Incomplete
FF_N_CHAR: Incomplete
FF_N_SEG: Incomplete
FF_N_OFF: Incomplete
FF_N_NUMB: Incomplete
FF_N_NUMO: Incomplete
FF_N_ENUM: Incomplete
FF_N_FOP: Incomplete
FF_N_STRO: Incomplete
FF_N_STK: Incomplete
FF_N_FLT: Incomplete
FF_N_CUST: Incomplete

def get_operand_type_shift(*args) -> int: ...
def get_operand_flag(*args) -> flags64_t: ...
def is_flag_for_operand(*args) -> bool: ...
def is_defarg0(*args) -> bool: ...
def is_defarg1(*args) -> bool: ...
def is_off0(*args) -> bool: ...
def is_off1(*args) -> bool: ...
def is_char0(*args) -> bool: ...
def is_char1(*args) -> bool: ...
def is_seg0(*args) -> bool: ...
def is_seg1(*args) -> bool: ...
def is_enum0(*args) -> bool: ...
def is_enum1(*args) -> bool: ...
def is_stroff0(*args) -> bool: ...
def is_stroff1(*args) -> bool: ...
def is_stkvar0(*args) -> bool: ...
def is_stkvar1(*args) -> bool: ...
def is_float0(*args) -> bool: ...
def is_float1(*args) -> bool: ...
def is_custfmt0(*args) -> bool: ...
def is_custfmt1(*args) -> bool: ...
def is_numop0(*args) -> bool: ...
def is_numop1(*args) -> bool: ...
def get_optype_flags0(*args) -> flags64_t: ...
def get_optype_flags1(*args) -> flags64_t: ...

OPND_OUTER: Incomplete
OPND_MASK: Incomplete
OPND_ALL: Incomplete

def is_defarg(*args) -> bool: ...
def is_off(*args) -> bool: ...
def is_char(*args) -> bool: ...
def is_seg(*args) -> bool: ...
def is_enum(*args) -> bool: ...
def is_manual(*args) -> bool: ...
def is_stroff(*args) -> bool: ...
def is_stkvar(*args) -> bool: ...
def is_fltnum(*args) -> bool: ...
def is_custfmt(*args) -> bool: ...
def is_numop(*args) -> bool: ...
def is_suspop(*args) -> bool: ...
def op_adds_xrefs(*args) -> bool: ...
def set_op_type(*args) -> bool: ...
def op_seg(*args) -> bool: ...
def op_enum(*args) -> bool: ...
def get_enum_id(*args) -> 'uchar *': ...
def op_based_stroff(*args) -> bool: ...
def get_stroff_path(*args) -> int: ...
def op_stkvar(*args) -> bool: ...
def set_forced_operand(*args) -> bool: ...
def get_forced_operand(*args) -> 'qstring *': ...
def is_forced_operand(*args) -> bool: ...
def combine_flags(*args) -> flags64_t: ...
def char_flag(*args) -> flags64_t: ...
def off_flag(*args) -> flags64_t: ...
def enum_flag(*args) -> flags64_t: ...
def stroff_flag(*args) -> flags64_t: ...
def stkvar_flag(*args) -> flags64_t: ...
def flt_flag(*args) -> flags64_t: ...
def custfmt_flag(*args) -> flags64_t: ...
def seg_flag(*args) -> flags64_t: ...
def num_flag(*args) -> flags64_t: ...
def hex_flag(*args) -> flags64_t: ...
def dec_flag(*args) -> flags64_t: ...
def oct_flag(*args) -> flags64_t: ...
def bin_flag(*args) -> flags64_t: ...
def op_chr(*args) -> bool: ...
def op_num(*args) -> bool: ...
def op_hex(*args) -> bool: ...
def op_dec(*args) -> bool: ...
def op_oct(*args) -> bool: ...
def op_bin(*args) -> bool: ...
def op_flt(*args) -> bool: ...
def op_custfmt(*args) -> bool: ...
def clr_op_type(*args) -> bool: ...
def get_default_radix(*args) -> int: ...
def get_radix(*args) -> int: ...

DT_TYPE: Incomplete
FF_BYTE: Incomplete
FF_WORD: Incomplete
FF_DWORD: Incomplete
FF_QWORD: Incomplete
FF_TBYTE: Incomplete
FF_STRLIT: Incomplete
FF_STRUCT: Incomplete
FF_OWORD: Incomplete
FF_FLOAT: Incomplete
FF_DOUBLE: Incomplete
FF_PACKREAL: Incomplete
FF_ALIGN: Incomplete
FF_CUSTOM: Incomplete
FF_YWORD: Incomplete
FF_ZWORD: Incomplete

def code_flag(*args) -> flags64_t: ...
def byte_flag(*args) -> flags64_t: ...
def word_flag(*args) -> flags64_t: ...
def dword_flag(*args) -> flags64_t: ...
def qword_flag(*args) -> flags64_t: ...
def oword_flag(*args) -> flags64_t: ...
def yword_flag(*args) -> flags64_t: ...
def zword_flag(*args) -> flags64_t: ...
def tbyte_flag(*args) -> flags64_t: ...
def strlit_flag(*args) -> flags64_t: ...
def stru_flag(*args) -> flags64_t: ...
def cust_flag(*args) -> flags64_t: ...
def align_flag(*args) -> flags64_t: ...
def float_flag(*args) -> flags64_t: ...
def double_flag(*args) -> flags64_t: ...
def packreal_flag(*args) -> flags64_t: ...
def is_byte(*args) -> bool: ...
def is_word(*args) -> bool: ...
def is_dword(*args) -> bool: ...
def is_qword(*args) -> bool: ...
def is_oword(*args) -> bool: ...
def is_yword(*args) -> bool: ...
def is_zword(*args) -> bool: ...
def is_tbyte(*args) -> bool: ...
def is_float(*args) -> bool: ...
def is_double(*args) -> bool: ...
def is_pack_real(*args) -> bool: ...
def is_strlit(*args) -> bool: ...
def is_struct(*args) -> bool: ...
def is_align(*args) -> bool: ...
def is_custom(*args) -> bool: ...
def f_is_byte(*args) -> bool: ...
def f_is_word(*args) -> bool: ...
def f_is_dword(*args) -> bool: ...
def f_is_qword(*args) -> bool: ...
def f_is_oword(*args) -> bool: ...
def f_is_yword(*args) -> bool: ...
def f_is_tbyte(*args) -> bool: ...
def f_is_float(*args) -> bool: ...
def f_is_double(*args) -> bool: ...
def f_is_pack_real(*args) -> bool: ...
def f_is_strlit(*args) -> bool: ...
def f_is_struct(*args) -> bool: ...
def f_is_align(*args) -> bool: ...
def f_is_custom(*args) -> bool: ...
def is_same_data_type(*args) -> bool: ...
def get_flags_by_size(*args) -> flags64_t: ...
def create_data(*args) -> bool: ...
def calc_dflags(*args) -> flags64_t: ...
def create_byte(*args) -> bool: ...
def create_word(*args) -> bool: ...
def create_dword(*args) -> bool: ...
def create_qword(*args) -> bool: ...
def create_oword(*args) -> bool: ...
def create_yword(*args) -> bool: ...
def create_zword(*args) -> bool: ...
def create_tbyte(*args) -> bool: ...
def create_float(*args) -> bool: ...
def create_double(*args) -> bool: ...
def create_packed_real(*args) -> bool: ...
def create_struct(*args) -> bool: ...
def create_custdata(*args) -> bool: ...
def create_align(*args) -> bool: ...
def calc_min_align(*args) -> int: ...
def calc_max_align(*args) -> int: ...
def calc_def_align(*args) -> int: ...
def create_16bit_data(*args) -> bool: ...
def create_32bit_data(*args) -> bool: ...

ALOPT_IGNHEADS: Incomplete
ALOPT_IGNPRINT: Incomplete
ALOPT_IGNCLT: Incomplete
ALOPT_MAX4K: Incomplete
ALOPT_ONLYTERM: Incomplete
ALOPT_APPEND: Incomplete

def get_max_strlit_length(*args) -> size_t: ...

STRCONV_ESCAPE: Incomplete
STRCONV_REPLCHAR: Incomplete
STRCONV_INCLLEN: Incomplete

def create_strlit(*args) -> bool: ...

PSTF_TNORM: Incomplete
PSTF_TBRIEF: Incomplete
PSTF_TINLIN: Incomplete
PSTF_TMASK: Incomplete
PSTF_HOTKEY: Incomplete
PSTF_ENC: Incomplete
PSTF_ONLY_ENC: Incomplete
PSTF_ATTRIB: Incomplete

def get_opinfo(*args) -> 'opinfo_t *': ...
def set_opinfo(*args) -> bool: ...
def get_data_elsize(*args) -> asize_t: ...
def get_full_data_elsize(*args) -> asize_t: ...
def is_varsize_item(*args) -> int: ...
def get_possible_item_varsize(*args) -> asize_t: ...
def can_define_item(*args) -> bool: ...

MS_CODE: Incomplete
FF_FUNC: Incomplete
FF_IMMD: Incomplete
FF_JUMP: Incomplete

def has_immd(*args) -> bool: ...
def is_func(*args) -> bool: ...
def set_immd(*args) -> bool: ...

class data_type_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    props: Incomplete
    name: Incomplete
    menu_name: Incomplete
    hotkey: Incomplete
    asm_keyword: Incomplete
    value_size: Incomplete
    def is_present_in_menus(self, *args) -> bool: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def __get_id(self, *args) -> int: ...
    id: Incomplete
    __real__init__ = __init__
    def __init__(self, *args) -> None: ...

DTP_NODUP: Incomplete

class data_format_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    props: Incomplete
    name: Incomplete
    menu_name: Incomplete
    hotkey: Incomplete
    value_size: Incomplete
    text_width: Incomplete
    def is_present_in_menus(self, *args) -> bool: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def __get_id(self, *args) -> int: ...
    id: Incomplete
    __real__init__ = __init__
    def __init__(self, *args) -> None: ...

def get_custom_data_type(*args) -> 'data_type_t const *': ...
def get_custom_data_format(*args) -> 'data_format_t const *': ...
def attach_custom_data_format(*args) -> bool: ...
def detach_custom_data_format(*args) -> bool: ...
def is_attached_custom_data_format(*args) -> bool: ...
def get_custom_data_types(*args) -> int: ...
def get_custom_data_formats(*args) -> int: ...
def find_custom_data_type(*args) -> int: ...
def find_custom_data_format(*args) -> int: ...
def set_cmt(*args) -> bool: ...
def get_cmt(*args) -> 'qstring *': ...
def append_cmt(*args) -> bool: ...
def get_predef_insn_cmt(*args) -> 'qstring *': ...
def find_byte(*args) -> ea_t: ...
def find_byter(*args) -> ea_t: ...

class compiled_binpat_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    bytes: Incomplete
    mask: Incomplete
    strlits: Incomplete
    encidx: Incomplete
    def __init__(self, *args) -> None: ...
    def all_bytes_defined(self, *args) -> bool: ...
    def qclear(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    __swig_destroy__: Incomplete

PBSENC_DEF1BPU: Incomplete
PBSENC_ALL: Incomplete

def parse_binpat_str(*args) -> 'qstring *': ...
def bin_search3(*args) -> 'size_t *': ...

BIN_SEARCH_CASE: Incomplete
BIN_SEARCH_NOCASE: Incomplete
BIN_SEARCH_NOBREAK: Incomplete
BIN_SEARCH_INITED: Incomplete
BIN_SEARCH_NOSHOW: Incomplete
BIN_SEARCH_FORWARD: Incomplete
BIN_SEARCH_BACKWARD: Incomplete
BIN_SEARCH_BITMASK: Incomplete

def next_inited(*args) -> ea_t: ...
def prev_inited(*args) -> ea_t: ...
def equal_bytes(*args) -> bool: ...

class hidden_range_t(ida_range.range_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    description: Incomplete
    header: Incomplete
    footer: Incomplete
    visible: Incomplete
    color: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def update_hidden_range(*args) -> bool: ...
def add_hidden_range(*args) -> bool: ...
def get_hidden_range(*args) -> 'hidden_range_t *': ...
def getn_hidden_range(*args) -> 'hidden_range_t *': ...
def get_hidden_range_qty(*args) -> int: ...
def get_hidden_range_num(*args) -> int: ...
def get_prev_hidden_range(*args) -> 'hidden_range_t *': ...
def get_next_hidden_range(*args) -> 'hidden_range_t *': ...
def get_first_hidden_range(*args) -> 'hidden_range_t *': ...
def get_last_hidden_range(*args) -> 'hidden_range_t *': ...
def del_hidden_range(*args) -> bool: ...
def add_mapping(*args) -> bool: ...
def del_mapping(*args) -> None: ...
def use_mapping(*args) -> ea_t: ...
def get_mappings_qty(*args) -> size_t: ...
def get_mapping(*args) -> 'ea_t *, ea_t *, asize_t *': ...
def free_chunk(*args) -> ea_t: ...

MS_0TYPE: Incomplete
FF_0VOID: Incomplete
FF_0NUMH: Incomplete
FF_0NUMD: Incomplete
FF_0CHAR: Incomplete
FF_0SEG: Incomplete
FF_0OFF: Incomplete
FF_0NUMB: Incomplete
FF_0NUMO: Incomplete
FF_0ENUM: Incomplete
FF_0FOP: Incomplete
FF_0STRO: Incomplete
FF_0STK: Incomplete
FF_0FLT: Incomplete
FF_0CUST: Incomplete
MS_1TYPE: Incomplete
FF_1VOID: Incomplete
FF_1NUMH: Incomplete
FF_1NUMD: Incomplete
FF_1CHAR: Incomplete
FF_1SEG: Incomplete
FF_1OFF: Incomplete
FF_1NUMB: Incomplete
FF_1NUMO: Incomplete
FF_1ENUM: Incomplete
FF_1FOP: Incomplete
FF_1STRO: Incomplete
FF_1STK: Incomplete
FF_1FLT: Incomplete
FF_1CUST: Incomplete

def visit_patched_bytes(*args) -> int: ...
def get_bytes(*args) -> 'PyObject *': ...
def get_bytes_and_mask(*args) -> 'PyObject *': ...
def get_strlit_contents(*args) -> 'PyObject *': ...
def bin_search(*args) -> ea_t: ...
def print_strlit_type(*args) -> 'PyObject *': ...
def get_octet(*args) -> 'PyObject *': ...
def get_8bit(*args) -> 'PyObject *': ...
def op_stroff(*args) -> bool: ...
def register_custom_data_type(*args) -> int: ...
def unregister_custom_data_type(*args) -> bool: ...
def register_custom_data_format(*args) -> int: ...
def unregister_custom_data_format(*args) -> bool: ...
def __walk_types_and_formats(formats, type_action, format_action, installing): ...
def register_data_types_and_formats(formats): ...
def unregister_data_types_and_formats(formats): ...