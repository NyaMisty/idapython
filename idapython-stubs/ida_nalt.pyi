# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_idaapi
from _typeshed import Incomplete

def _swig_repr(self): ...
def _swig_setattr_nondynamic_instance_variable(set): ...
def _swig_setattr_nondynamic_class_variable(set): ...
def _swig_add_metaclass(metaclass): ...

class _SwigNonDynamicMeta(type):
    __setattr__: Incomplete

SWIG_PYTHON_LEGACY_BOOL: Incomplete

class custom_data_type_ids_fids_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'short const &': ...
    def __setitem__(self, *args) -> None: ...
    def _get_bytes(self, *args) -> bytevec_t: ...
    def _set_bytes(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    bytes: Incomplete
    __swig_destroy__: Incomplete

class strpath_ids_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'unsigned long long const &': ...
    def __setitem__(self, *args) -> None: ...
    def _get_bytes(self, *args) -> bytevec_t: ...
    def _set_bytes(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    bytes: Incomplete
    __swig_destroy__: Incomplete

NALT_SWITCH: Incomplete
NALT_STRUCT: Incomplete
NALT_AFLAGS: Incomplete
NALT_LINNUM: Incomplete
NALT_ABSBASE: Incomplete
NALT_ENUM0: Incomplete
NALT_ENUM1: Incomplete
NALT_PURGE: Incomplete
NALT_STRTYPE: Incomplete
NALT_ALIGN: Incomplete
NALT_COLOR: Incomplete
NSUP_CMT: Incomplete
NSUP_REPCMT: Incomplete
NSUP_FOP1: Incomplete
NSUP_FOP2: Incomplete
NSUP_JINFO: Incomplete
NSUP_ARRAY: Incomplete
NSUP_OMFGRP: Incomplete
NSUP_FOP3: Incomplete
NSUP_SWITCH: Incomplete
NSUP_REF0: Incomplete
NSUP_REF1: Incomplete
NSUP_REF2: Incomplete
NSUP_OREF0: Incomplete
NSUP_OREF1: Incomplete
NSUP_OREF2: Incomplete
NSUP_STROFF0: Incomplete
NSUP_STROFF1: Incomplete
NSUP_SEGTRANS: Incomplete
NSUP_FOP4: Incomplete
NSUP_FOP5: Incomplete
NSUP_FOP6: Incomplete
NSUP_REF3: Incomplete
NSUP_REF4: Incomplete
NSUP_REF5: Incomplete
NSUP_OREF3: Incomplete
NSUP_OREF4: Incomplete
NSUP_OREF5: Incomplete
NSUP_XREFPOS: Incomplete
NSUP_CUSTDT: Incomplete
NSUP_GROUPS: Incomplete
NSUP_ARGEAS: Incomplete
NSUP_FOP7: Incomplete
NSUP_FOP8: Incomplete
NSUP_REF6: Incomplete
NSUP_REF7: Incomplete
NSUP_OREF6: Incomplete
NSUP_OREF7: Incomplete
NSUP_EX_FLAGS: Incomplete
NSUP_POINTS: Incomplete
NSUP_MANUAL: Incomplete
NSUP_TYPEINFO: Incomplete
NSUP_REGVAR: Incomplete
NSUP_LLABEL: Incomplete
NSUP_REGARG: Incomplete
NSUP_FTAILS: Incomplete
NSUP_GROUP: Incomplete
NSUP_OPTYPES: Incomplete
NSUP_ORIGFMD: Incomplete
NALT_CREF_TO: Incomplete
NALT_CREF_FROM: Incomplete
NALT_DREF_TO: Incomplete
NALT_DREF_FROM: Incomplete
NSUP_GR_INFO: Incomplete
NALT_GR_LAYX: Incomplete
NSUP_GR_LAYT: Incomplete
PATCH_TAG: Incomplete
IDB_DESKTOPS_NODE_NAME: Incomplete
IDB_DESKTOPS_TAG: Incomplete

def ea2node(*args) -> nodeidx_t: ...
def node2ea(*args) -> ea_t: ...
def end_ea2node(*args) -> nodeidx_t: ...
def getnode(*args) -> netnode: ...
def get_strid(*args) -> tid_t: ...

AFL_LINNUM: Incomplete
AFL_USERSP: Incomplete
AFL_PUBNAM: Incomplete
AFL_WEAKNAM: Incomplete
AFL_HIDDEN: Incomplete
AFL_MANUAL: Incomplete
AFL_NOBRD: Incomplete
AFL_ZSTROFF: Incomplete
AFL_BNOT0: Incomplete
AFL_BNOT1: Incomplete
AFL_LIB: Incomplete
AFL_TI: Incomplete
AFL_TI0: Incomplete
AFL_TI1: Incomplete
AFL_LNAME: Incomplete
AFL_TILCMT: Incomplete
AFL_LZERO0: Incomplete
AFL_LZERO1: Incomplete
AFL_COLORED: Incomplete
AFL_TERSESTR: Incomplete
AFL_SIGN0: Incomplete
AFL_SIGN1: Incomplete
AFL_NORET: Incomplete
AFL_FIXEDSPD: Incomplete
AFL_ALIGNFLOW: Incomplete
AFL_USERTI: Incomplete
AFL_RETFP: Incomplete
AFL_USEMODSP: Incomplete
AFL_NOTCODE: Incomplete
AFL_NOTPROC: Incomplete
AFL_TYPE_GUESSED: Incomplete
AFL_IDA_GUESSED: Incomplete
AFL_HR_GUESSED_FUNC: Incomplete
AFL_HR_GUESSED_DATA: Incomplete
AFL_HR_DETERMINED: Incomplete

def set_aflags(*args) -> None: ...
def upd_abits(*args) -> None: ...
def set_abits(*args) -> None: ...
def clr_abits(*args) -> None: ...
def get_aflags(*args) -> aflags_t: ...
def del_aflags(*args) -> None: ...
def has_aflag_linnum(*args) -> bool: ...
def is_aflag_usersp(*args) -> bool: ...
def is_aflag_public_name(*args) -> bool: ...
def is_aflag_weak_name(*args) -> bool: ...
def is_aflag_hidden_item(*args) -> bool: ...
def is_aflag_manual_insn(*args) -> bool: ...
def is_aflag_hidden_border(*args) -> bool: ...
def is_aflag_zstroff(*args) -> bool: ...
def is_aflag__bnot0(*args) -> bool: ...
def is_aflag__bnot1(*args) -> bool: ...
def is_aflag_libitem(*args) -> bool: ...
def has_aflag_ti(*args) -> bool: ...
def has_aflag_ti0(*args) -> bool: ...
def has_aflag_ti1(*args) -> bool: ...
def has_aflag_lname(*args) -> bool: ...
def is_aflag_tilcmt(*args) -> bool: ...
def is_aflag_lzero0(*args) -> bool: ...
def is_aflag_lzero1(*args) -> bool: ...
def is_aflag_colored_item(*args) -> bool: ...
def is_aflag_terse_struc(*args) -> bool: ...
def is_aflag__invsign0(*args) -> bool: ...
def is_aflag__invsign1(*args) -> bool: ...
def is_aflag_noret(*args) -> bool: ...
def is_aflag_fixed_spd(*args) -> bool: ...
def is_aflag_align_flow(*args) -> bool: ...
def is_aflag_userti(*args) -> bool: ...
def is_aflag_retfp(*args) -> bool: ...
def uses_aflag_modsp(*args) -> bool: ...
def is_aflag_notcode(*args) -> bool: ...
def is_aflag_notproc(*args) -> bool: ...
def is_aflag_type_guessed_by_ida(*args) -> bool: ...
def is_aflag_func_guessed_by_hexrays(*args) -> bool: ...
def is_aflag_data_guessed_by_hexrays(*args) -> bool: ...
def is_aflag_type_determined_by_hexrays(*args) -> bool: ...
def is_aflag_type_guessed_by_hexrays(*args) -> bool: ...
def is_hidden_item(*args) -> bool: ...
def hide_item(*args) -> None: ...
def unhide_item(*args) -> None: ...
def is_hidden_border(*args) -> bool: ...
def hide_border(*args) -> None: ...
def unhide_border(*args) -> None: ...
def uses_modsp(*args) -> bool: ...
def set_usemodsp(*args) -> None: ...
def clr_usemodsp(*args) -> None: ...
def is_zstroff(*args) -> bool: ...
def set_zstroff(*args) -> None: ...
def clr_zstroff(*args) -> None: ...
def is__bnot0(*args) -> bool: ...
def set__bnot0(*args) -> None: ...
def clr__bnot0(*args) -> None: ...
def is__bnot1(*args) -> bool: ...
def set__bnot1(*args) -> None: ...
def clr__bnot1(*args) -> None: ...
def is_libitem(*args) -> bool: ...
def set_libitem(*args) -> None: ...
def clr_libitem(*args) -> None: ...
def has_ti(*args) -> bool: ...
def set_has_ti(*args) -> None: ...
def clr_has_ti(*args) -> None: ...
def has_ti0(*args) -> bool: ...
def set_has_ti0(*args) -> None: ...
def clr_has_ti0(*args) -> None: ...
def has_ti1(*args) -> bool: ...
def set_has_ti1(*args) -> None: ...
def clr_has_ti1(*args) -> None: ...
def has_lname(*args) -> bool: ...
def set_has_lname(*args) -> None: ...
def clr_has_lname(*args) -> None: ...
def is_tilcmt(*args) -> bool: ...
def set_tilcmt(*args) -> None: ...
def clr_tilcmt(*args) -> None: ...
def is_usersp(*args) -> bool: ...
def set_usersp(*args) -> None: ...
def clr_usersp(*args) -> None: ...
def is_lzero0(*args) -> bool: ...
def set_lzero0(*args) -> None: ...
def clr_lzero0(*args) -> None: ...
def is_lzero1(*args) -> bool: ...
def set_lzero1(*args) -> None: ...
def clr_lzero1(*args) -> None: ...
def is_colored_item(*args) -> bool: ...
def set_colored_item(*args) -> None: ...
def clr_colored_item(*args) -> None: ...
def is_terse_struc(*args) -> bool: ...
def set_terse_struc(*args) -> None: ...
def clr_terse_struc(*args) -> None: ...
def is__invsign0(*args) -> bool: ...
def set__invsign0(*args) -> None: ...
def clr__invsign0(*args) -> None: ...
def is__invsign1(*args) -> bool: ...
def set__invsign1(*args) -> None: ...
def clr__invsign1(*args) -> None: ...
def is_noret(*args) -> bool: ...
def set_noret(*args) -> None: ...
def clr_noret(*args) -> None: ...
def is_fixed_spd(*args) -> bool: ...
def set_fixed_spd(*args) -> None: ...
def clr_fixed_spd(*args) -> None: ...
def is_align_flow(*args) -> bool: ...
def set_align_flow(*args) -> None: ...
def clr_align_flow(*args) -> None: ...
def is_userti(*args) -> bool: ...
def set_userti(*args) -> None: ...
def clr_userti(*args) -> None: ...
def is_retfp(*args) -> bool: ...
def set_retfp(*args) -> None: ...
def clr_retfp(*args) -> None: ...
def is_notproc(*args) -> bool: ...
def set_notproc(*args) -> None: ...
def clr_notproc(*args) -> None: ...
def is_type_guessed_by_ida(*args) -> bool: ...
def is_func_guessed_by_hexrays(*args) -> bool: ...
def is_data_guessed_by_hexrays(*args) -> bool: ...
def is_type_determined_by_hexrays(*args) -> bool: ...
def is_type_guessed_by_hexrays(*args) -> bool: ...
def set_type_guessed_by_ida(*args) -> None: ...
def set_func_guessed_by_hexrays(*args) -> None: ...
def set_data_guessed_by_hexrays(*args) -> None: ...
def set_type_determined_by_hexrays(*args) -> None: ...
def set_notcode(*args) -> None: ...
def clr_notcode(*args) -> None: ...
def is_notcode(*args) -> bool: ...
def set_visible_item(*args) -> None: ...
def is_visible_item(*args) -> bool: ...
def is_finally_visible_item(*args) -> bool: ...
def set_source_linnum(*args) -> None: ...
def get_source_linnum(*args) -> uval_t: ...
def del_source_linnum(*args) -> None: ...
def get_absbase(*args) -> ea_t: ...
def set_absbase(*args) -> None: ...
def del_absbase(*args) -> None: ...
def get_ind_purged(*args) -> ea_t: ...
def del_ind_purged(*args) -> None: ...
def get_str_type(*args) -> uint32: ...
def set_str_type(*args) -> None: ...
def del_str_type(*args) -> None: ...

STRWIDTH_1B: Incomplete
STRWIDTH_2B: Incomplete
STRWIDTH_4B: Incomplete
STRWIDTH_MASK: Incomplete
STRLYT_TERMCHR: Incomplete
STRLYT_PASCAL1: Incomplete
STRLYT_PASCAL2: Incomplete
STRLYT_PASCAL4: Incomplete
STRLYT_MASK: Incomplete
STRLYT_SHIFT: Incomplete
STRTYPE_TERMCHR: Incomplete
STRTYPE_C: Incomplete
STRTYPE_C_16: Incomplete
STRTYPE_C_32: Incomplete
STRTYPE_PASCAL: Incomplete
STRTYPE_PASCAL_16: Incomplete
STRTYPE_PASCAL_32: Incomplete
STRTYPE_LEN2: Incomplete
STRTYPE_LEN2_16: Incomplete
STRTYPE_LEN2_32: Incomplete
STRTYPE_LEN4: Incomplete
STRTYPE_LEN4_16: Incomplete
STRTYPE_LEN4_32: Incomplete

def get_str_type_code(*args) -> uchar: ...
def get_str_term1(*args) -> char: ...
def get_str_term2(*args) -> char: ...
def get_str_encoding_idx(*args) -> uchar: ...
def set_str_encoding_idx(*args) -> int32: ...
def make_str_type(*args) -> int32: ...
def is_pascal(*args) -> bool: ...
def get_str_type_prefix_length(*args) -> size_t: ...

STRENC_DEFAULT: Incomplete
STRENC_NONE: Incomplete

def get_alignment(*args) -> uint32: ...
def set_alignment(*args) -> None: ...
def del_alignment(*args) -> None: ...
def set_item_color(*args) -> None: ...
def get_item_color(*args) -> bgcolor_t: ...
def del_item_color(*args) -> bool: ...

class array_parameters_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    flags: Incomplete
    lineitems: Incomplete
    alignment: Incomplete
    def __init__(self, *args) -> None: ...
    def is_default(self, *args) -> bool: ...
    __swig_destroy__: Incomplete

AP_ALLOWDUPS: Incomplete
AP_SIGNED: Incomplete
AP_INDEX: Incomplete
AP_ARRAY: Incomplete
AP_IDXBASEMASK: Incomplete
AP_IDXDEC: Incomplete
AP_IDXHEX: Incomplete
AP_IDXOCT: Incomplete
AP_IDXBIN: Incomplete

def get_array_parameters(*args) -> ssize_t: ...
def set_array_parameters(*args) -> None: ...
def del_array_parameters(*args) -> None: ...

class switch_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    flags: Incomplete
    def get_shift(self, *args) -> int: ...
    def set_shift(self, *args) -> None: ...
    def get_jtable_element_size(self, *args) -> int: ...
    def set_jtable_element_size(self, *args) -> None: ...
    def get_vtable_element_size(self, *args) -> int: ...
    def set_vtable_element_size(self, *args) -> None: ...
    def has_default(self, *args) -> bool: ...
    def has_elbase(self, *args) -> bool: ...
    def is_sparse(self, *args) -> bool: ...
    def is_custom(self, *args) -> bool: ...
    def is_indirect(self, *args) -> bool: ...
    def is_subtract(self, *args) -> bool: ...
    def is_nolowcase(self, *args) -> bool: ...
    def use_std_table(self, *args) -> bool: ...
    def is_user_defined(self, *args) -> bool: ...
    ncases: Incomplete
    jumps: Incomplete
    values: Incomplete
    lowcase: Incomplete
    defjump: Incomplete
    startea: Incomplete
    jcases: Incomplete
    ind_lowcase: Incomplete
    def get_lowcase(self, *args) -> sval_t: ...
    elbase: Incomplete
    regnum: Incomplete
    regdtype: Incomplete
    def get_jtable_size(self, *args) -> int: ...
    def set_jtable_size(self, *args) -> None: ...
    def set_elbase(self, *args) -> None: ...
    def set_expr(self, *args) -> None: ...
    def get_jrange_vrange(self, *args) -> bool: ...
    custom: Incomplete
    SWITCH_INFO_VERSION: Incomplete
    def get_version(self, *args) -> int: ...
    expr_ea: Incomplete
    marks: Incomplete
    def __init__(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def assign(self, *args) -> None: ...
    def _get_values_lowcase(self, *args) -> ea_t: ...
    def _set_values_lowcase(self, *args) -> None: ...
    __swig_destroy__: Incomplete

SWI_SPARSE: Incomplete
SWI_V32: Incomplete
SWI_J32: Incomplete
SWI_VSPLIT: Incomplete
SWI_USER: Incomplete
SWI_DEF_IN_TBL: Incomplete
SWI_JMP_INV: Incomplete
SWI_SHIFT_MASK: Incomplete
SWI_ELBASE: Incomplete
SWI_JSIZE: Incomplete
SWI_VSIZE: Incomplete
SWI_SEPARATE: Incomplete
SWI_SIGNED: Incomplete
SWI_CUSTOM: Incomplete
SWI_INDIRECT: Incomplete
SWI_SUBTRACT: Incomplete
SWI_HXNOLOWCASE: Incomplete
SWI_STDTBL: Incomplete
SWI_DEFRET: Incomplete
SWI_SELFREL: Incomplete
SWI_JMPINSN: Incomplete
SWI_VERSION: Incomplete

def get_switch_info(*args) -> ssize_t: ...
def set_switch_info(*args) -> None: ...
def del_switch_info(*args) -> None: ...
def get_switch_parent(*args) -> ea_t: ...
def set_switch_parent(*args) -> None: ...
def del_switch_parent(*args) -> None: ...

class custom_data_type_ids_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    dtid: Incomplete
    fids: Incomplete
    def set(self, *args) -> None: ...
    def get_dtid(self, *args) -> tid_t: ...
    def __getFids(self, *args) -> 'wrapped_array_t< int16,8 >': ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def get_custom_data_type_ids(*args) -> int: ...
def set_custom_data_type_ids(*args) -> None: ...
def del_custom_data_type_ids(*args) -> None: ...
def is_reftype_target_optional(*args) -> bool: ...
def get_reftype_by_size(*args) -> reftype_t: ...

class refinfo_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    target: Incomplete
    base: Incomplete
    tdelta: Incomplete
    flags: Incomplete
    def type(self, *args) -> reftype_t: ...
    def is_target_optional(self, *args) -> bool: ...
    def no_base_xref(self, *args) -> bool: ...
    def is_pastend(self, *args) -> bool: ...
    def is_rvaoff(self, *args) -> bool: ...
    def is_custom(self, *args) -> bool: ...
    def is_subtract(self, *args) -> bool: ...
    def is_signed(self, *args) -> bool: ...
    def is_no_zeros(self, *args) -> bool: ...
    def is_no_ones(self, *args) -> bool: ...
    def is_selfref(self, *args) -> bool: ...
    def set_type(self, *args) -> None: ...
    def init(self, *args) -> None: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

cvar: Incomplete
V695_REF_OFF8: Incomplete
REF_OFF16: Incomplete
REF_OFF32: Incomplete
REF_LOW8: Incomplete
REF_LOW16: Incomplete
REF_HIGH8: Incomplete
REF_HIGH16: Incomplete
V695_REF_VHIGH: Incomplete
V695_REF_VLOW: Incomplete
REF_OFF64: Incomplete
REF_OFF8: Incomplete
REF_LAST: Incomplete
REFINFO_TYPE: Incomplete
REFINFO_RVAOFF: Incomplete
REFINFO_PASTEND: Incomplete
REFINFO_CUSTOM: Incomplete
REFINFO_NOBASE: Incomplete
REFINFO_SUBTRACT: Incomplete
REFINFO_SIGNEDOP: Incomplete
REFINFO_NO_ZEROS: Incomplete
REFINFO_NO_ONES: Incomplete
REFINFO_SELFREF: Incomplete

def find_custom_refinfo(*args) -> int: ...
def get_custom_refinfo(*args) -> 'custom_refinfo_handler_t const *': ...

MAXSTRUCPATH: Incomplete

class strpath_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    len: Incomplete
    ids: Incomplete
    delta: Incomplete
    def __getIds(self, *args) -> 'wrapped_array_t< tid_t,32 >': ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class enum_const_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    tid: Incomplete
    serial: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class opinfo_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    ri: Incomplete
    tid: Incomplete
    path: Incomplete
    strtype: Incomplete
    ec: Incomplete
    cd: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class printop_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    ti: Incomplete
    features: Incomplete
    suspop: Incomplete
    aflags: Incomplete
    flags: Incomplete
    def __init__(self, *args) -> None: ...
    def is_ti_initialized(self, *args) -> bool: ...
    def set_ti_initialized(self, *args) -> None: ...
    def is_aflags_initialized(self, *args) -> bool: ...
    def set_aflags_initialized(self, *args) -> None: ...
    def is_f64(self, *args) -> bool: ...
    def get_ti(self, *args) -> 'opinfo_t const *': ...
    is_ti_valid: Incomplete
    __swig_destroy__: Incomplete

POF_VALID_TI: Incomplete
POF_VALID_AFLAGS: Incomplete
POF_IS_F64: Incomplete

def set_refinfo_ex(*args) -> bool: ...
def set_refinfo(*args) -> bool: ...
def get_refinfo(*args) -> bool: ...
def del_refinfo(*args) -> bool: ...
def get_tinfo(*args) -> bool: ...
def set_tinfo(*args) -> bool: ...
def del_tinfo(*args) -> None: ...
def get_op_tinfo(*args) -> bool: ...
def set_op_tinfo(*args) -> bool: ...
def del_op_tinfo(*args) -> None: ...

RIDX_FILE_FORMAT_NAME: Incomplete
RIDX_SELECTORS: Incomplete
RIDX_GROUPS: Incomplete
RIDX_H_PATH: Incomplete
RIDX_C_MACROS: Incomplete
RIDX_SMALL_IDC_OLD: Incomplete
RIDX_NOTEPAD: Incomplete
RIDX_INCLUDE: Incomplete
RIDX_SMALL_IDC: Incomplete
RIDX_DUALOP_GRAPH: Incomplete
RIDX_DUALOP_TEXT: Incomplete
RIDX_MD5: Incomplete
RIDX_IDA_VERSION: Incomplete
RIDX_STR_ENCODINGS: Incomplete
RIDX_SRCDBG_PATHS: Incomplete
RIDX_DBG_BINPATHS: Incomplete
RIDX_SHA256: Incomplete
RIDX_ABINAME: Incomplete
RIDX_ARCHIVE_PATH: Incomplete
RIDX_PROBLEMS: Incomplete
RIDX_SRCDBG_UNDESIRED: Incomplete

def get_root_filename(*args) -> size_t: ...
def dbg_get_input_path(*args) -> size_t: ...
def get_input_file_path(*args) -> size_t: ...
def set_root_filename(*args) -> None: ...
def retrieve_input_file_size(*args) -> size_t: ...
def retrieve_input_file_crc32(*args) -> uint32: ...
def retrieve_input_file_md5(*args) -> uchar[ANY]: ...
def retrieve_input_file_sha256(*args) -> uchar[ANY]: ...
def get_asm_inc_file(*args) -> 'qstring *': ...
def set_asm_inc_file(*args) -> bool: ...
def get_imagebase(*args) -> ea_t: ...
def set_imagebase(*args) -> None: ...
def get_ids_modnode(*args) -> netnode: ...
def set_ids_modnode(*args) -> None: ...
def get_archive_path(*args) -> 'qstring *': ...
def set_archive_path(*args) -> bool: ...
def get_loader_format_name(*args) -> 'qstring *': ...
def set_loader_format_name(*args) -> None: ...
def get_initial_ida_version(*args) -> 'qstring *': ...
def get_ida_notepad_text(*args) -> 'qstring *': ...
def set_ida_notepad_text(*args) -> None: ...
def get_srcdbg_paths(*args) -> 'qstring *': ...
def set_srcdbg_paths(*args) -> None: ...
def get_srcdbg_undesired_paths(*args) -> 'qstring *': ...
def set_srcdbg_undesired_paths(*args) -> None: ...
def get_initial_idb_version(*args) -> ushort: ...
def get_idb_ctime(*args) -> time_t: ...
def get_elapsed_secs(*args) -> size_t: ...
def get_idb_nopens(*args) -> size_t: ...
def get_encoding_qty(*args) -> int: ...
def get_encoding_name(*args) -> 'char const *': ...
def add_encoding(*args) -> int: ...
def del_encoding(*args) -> bool: ...
def rename_encoding(*args) -> bool: ...

BPU_1B: Incomplete
BPU_2B: Incomplete
BPU_4B: Incomplete

def get_encoding_bpu(*args) -> int: ...
def get_encoding_bpu_by_name(*args) -> int: ...
def get_strtype_bpu(*args) -> int: ...
def get_default_encoding_idx(*args) -> int: ...
def set_default_encoding_idx(*args) -> bool: ...
def encoding_from_strtype(*args) -> 'char const *': ...
def get_outfile_encoding_idx(*args) -> int: ...
def set_outfile_encoding_idx(*args) -> bool: ...
def get_import_module_qty(*args) -> uint: ...
def delete_imports(*args) -> None: ...
def validate_idb_names(*args) -> int: ...
def set_gotea(*args) -> None: ...
def get_gotea(*args) -> ea_t: ...
def get_import_module_name(*args) -> 'PyObject *': ...
def enum_import_names(*args) -> int: ...
def switch_info_t__from_ptrval__(*args) -> 'switch_info_t *': ...
_real_get_switch_info = get_switch_info

def get_abi_name(): ...
get_initial_version = get_initial_idb_version
