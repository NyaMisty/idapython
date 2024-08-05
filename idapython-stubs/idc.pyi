# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

import ida_auto
import ida_bytes
import ida_dbg
import ida_entry
import ida_enum
import ida_fixup
import ida_frame
import ida_funcs
import ida_idc
import ida_idd
import ida_idp
import ida_kernwin
import ida_lines
import ida_loader
import ida_nalt
import ida_name
import ida_offset
import ida_pro
import ida_search
import ida_segment
import ida_struct
import ida_ua
import ida_xref
from _typeshed import Incomplete
from collections.abc import Generator

__EA64__: Incomplete
WORDMASK: Incomplete

class DeprecatedIDCError(Exception): ...

__warned_deprecated_proto_confusion: Incomplete

def __warn_once_deprecated_proto_confusion(what, alternative) -> None: ...
def _IDC_GetAttr(obj, attrmap, attroffs): ...
def _IDC_SetAttr(obj, attrmap, attroffs, value): ...

BADADDR: Incomplete
BADSEL: Incomplete
SIZE_MAX: Incomplete
MS_VAL: Incomplete
FF_IVL: Incomplete

def has_value(F): ...
def byte_value(F): ...
def is_loaded(ea): ...

MS_CLS: Incomplete
FF_CODE: Incomplete
FF_DATA: Incomplete
FF_TAIL: Incomplete
FF_UNK: Incomplete

def is_code(F): ...
def is_data(F): ...
def is_tail(F): ...
def is_unknown(F): ...
def is_head(F): ...

MS_COMM: Incomplete
FF_COMM: Incomplete
FF_REF: Incomplete
FF_LINE: Incomplete
FF_NAME: Incomplete
FF_LABL: Incomplete
FF_FLOW: Incomplete
FF_ANYNAME = FF_LABL | FF_NAME

def is_flow(F): ...
def isExtra(F): ...
def isRef(F): ...
def hasName(F): ...
def hasUserName(F): ...

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

def is_defarg0(F): ...
def is_defarg1(F): ...
def isDec0(F): ...
def isDec1(F): ...
def isHex0(F): ...
def isHex1(F): ...
def isOct0(F): ...
def isOct1(F): ...
def isBin0(F): ...
def isBin1(F): ...
def is_off0(F): ...
def is_off1(F): ...
def is_char0(F): ...
def is_char1(F): ...
def is_seg0(F): ...
def is_seg1(F): ...
def is_enum0(F): ...
def is_enum1(F): ...
def is_manual0(F): ...
def is_manual1(F): ...
def is_stroff0(F): ...
def is_stroff1(F): ...
def is_stkvar0(F): ...
def is_stkvar1(F): ...

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

def is_byte(F): ...
def is_word(F): ...
def is_dword(F): ...
def is_qword(F): ...
def is_oword(F): ...
def is_tbyte(F): ...
def is_float(F): ...
def is_double(F): ...
def is_pack_real(F): ...
def is_strlit(F): ...
def is_struct(F): ...
def is_align(F): ...

MS_CODE: Incomplete
FF_FUNC: Incomplete
FF_IMMD: Incomplete
FF_JUMP: Incomplete
_scope = ida_loader.loader_t
_scope = ida_loader
NEF_SEGS: Incomplete
NEF_RSCS: Incomplete
NEF_NAME: Incomplete
NEF_MAN: Incomplete
NEF_FILL: Incomplete
NEF_IMPS: Incomplete
NEF_FIRST: Incomplete
NEF_CODE: Incomplete
NEF_RELOAD: Incomplete
NEF_FLAT: Incomplete

def value_is_string(var) -> None: ...
def value_is_long(var) -> None: ...
def value_is_float(var) -> None: ...
def value_is_func(var) -> None: ...
def value_is_pvoid(var) -> None: ...
def value_is_int64(var) -> None: ...
def to_ea(seg, off): ...
def form(format, *args) -> None: ...
def substr(s, x1, x2) -> None: ...
def strstr(s1, s2) -> None: ...
def strlen(s) -> None: ...
def xtol(s) -> None: ...
def atoa(ea): ...
def ltoa(n, radix) -> None: ...
def atol(s) -> None: ...
def rotate_left(value, count, nbits, offset): ...
def rotate_dword(x, count): ...
def rotate_word(x, count): ...
def rotate_byte(x, count): ...

IDCHK_OK: int
IDCHK_ARG: int
IDCHK_KEY: int
IDCHK_MAX: int
add_idc_hotkey = ida_kernwin.add_idc_hotkey
del_idc_hotkey = ida_kernwin.del_idc_hotkey
jumpto = ida_kernwin.jumpto
auto_wait = ida_auto.auto_wait

def eval_idc(expr): ...
def EVAL_FAILURE(code): ...
def save_database(idbname, flags: int = 0): ...

DBFL_BAK: Incomplete

def validate_idb_names(do_repair: int = 0): ...
qexit = ida_pro.qexit

def call_system(command): ...
def qsleep(milliseconds) -> None: ...
load_and_run_plugin = ida_loader.load_and_run_plugin
plan_to_apply_idasgn = ida_funcs.plan_to_apply_idasgn

def delete_all_segments() -> None: ...
create_insn = ida_ua.create_insn

def plan_and_wait(sEA, eEA, final_pass: bool = True): ...
def set_name(ea, name, flags=...): ...

SN_CHECK: Incomplete
SN_NOCHECK: Incomplete
SN_PUBLIC: Incomplete
SN_NON_PUBLIC: Incomplete
SN_WEAK: Incomplete
SN_NON_WEAK: Incomplete
SN_AUTO: Incomplete
SN_NON_AUTO: Incomplete
SN_NOLIST: Incomplete
SN_NOWARN: Incomplete
SN_LOCAL: Incomplete
set_cmt = ida_bytes.set_cmt

def make_array(ea, nitems): ...
def create_strlit(ea, endea): ...
create_data = ida_bytes.create_data

def create_byte(ea): ...
def create_word(ea): ...
def create_dword(ea): ...
def create_qword(ea): ...
def create_oword(ea): ...
def create_yword(ea): ...
def create_float(ea): ...
def create_double(ea): ...
def create_pack_real(ea): ...
def create_tbyte(ea): ...
def create_struct(ea, size, strname): ...
create_custom_data = ida_bytes.create_custdata
create_align = ida_bytes.create_align

def define_local_var(start, end, location, name): ...
del_items = ida_bytes.del_items
DELIT_SIMPLE: Incomplete
DELIT_EXPAND: Incomplete
DELIT_DELNAMES: Incomplete

def set_array_params(ea, flags, litems, align): ...

AP_ALLOWDUPS: int
AP_SIGNED: int
AP_INDEX: int
AP_ARRAY: int
AP_IDXBASEMASK: int
AP_IDXDEC: int
AP_IDXHEX: int
AP_IDXOCT: int
AP_IDXBIN: int
op_bin = ida_bytes.op_bin
op_oct = ida_bytes.op_oct
op_dec = ida_bytes.op_dec
op_hex = ida_bytes.op_hex
op_chr = ida_bytes.op_chr

def op_plain_offset(ea, n, base): ...

OPND_OUTER: Incomplete
op_offset = ida_offset.op_offset
REF_OFF8: Incomplete
REF_OFF16: Incomplete
REF_OFF32: Incomplete
REF_LOW8: Incomplete
REF_LOW16: Incomplete
REF_HIGH8: Incomplete
REF_HIGH16: Incomplete
REF_OFF64: Incomplete
REFINFO_RVA: int
REFINFO_PASTEND: int
REFINFO_NOBASE: int
REFINFO_SUBTRACT: int
REFINFO_SIGNEDOP: int
op_seg = ida_bytes.op_seg
op_num = ida_bytes.op_num
op_flt = ida_bytes.op_flt
op_man = ida_bytes.set_forced_operand
toggle_sign = ida_bytes.toggle_sign

def toggle_bnot(ea, n): ...
op_enum = ida_bytes.op_enum

def op_stroff(ea, n, strid, delta): ...
op_stkvar = ida_bytes.op_stkvar

def op_offset_high16(ea, n, target): ...
def MakeVar(ea) -> None: ...

E_PREV: Incomplete
E_NEXT: Incomplete
get_extra_cmt = ida_lines.get_extra_cmt
update_extra_cmt = ida_lines.update_extra_cmt
del_extra_cmt = ida_lines.del_extra_cmt
set_manual_insn = ida_bytes.set_manual_insn
get_manual_insn = ida_bytes.get_manual_insn
patch_dbg_byte = ida_dbg.put_dbg_byte
patch_byte = ida_bytes.patch_byte
patch_word = ida_bytes.patch_word
patch_dword = ida_bytes.patch_dword
patch_qword = ida_bytes.patch_qword
SR_inherit: int
SR_user: int
SR_auto: int
SR_autostart: int

def split_sreg_range(ea, reg, value, tag=...): ...
auto_mark_range = ida_auto.auto_mark_range
auto_unmark = ida_auto.auto_unmark

def AutoMark(ea, qtype): ...

AU_UNK: Incomplete
AU_CODE: Incomplete
AU_PROC: Incomplete
AU_USED: Incomplete
AU_LIBF: Incomplete
AU_FINAL: Incomplete

def gen_file(filetype, path, ea1, ea2, flags): ...

OFILE_MAP: Incomplete
OFILE_EXE: Incomplete
OFILE_IDC: Incomplete
OFILE_LST: Incomplete
OFILE_ASM: Incomplete
OFILE_DIF: Incomplete
GENFLG_MAPSEG: Incomplete
GENFLG_MAPNAME: Incomplete
GENFLG_MAPDMNG: Incomplete
GENFLG_MAPLOC: Incomplete
GENFLG_IDCTYPE: Incomplete
GENFLG_ASMTYPE: Incomplete
GENFLG_GENHTML: Incomplete
GENFLG_ASMINC: Incomplete

def gen_flow_graph(outfile, title, ea1, ea2, flags): ...

CHART_PRINT_NAMES: int
CHART_GEN_GDL: int
CHART_WINGRAPH: int
CHART_NOLIBFUNCS: int

def gen_simple_call_chart(outfile, title, flags): ...
def idadir(): ...
get_root_filename = ida_nalt.get_root_filename
get_input_file_path = ida_nalt.get_input_file_path
set_root_filename = ida_nalt.set_root_filename

def get_idb_path(): ...
retrieve_input_file_md5 = ida_nalt.retrieve_input_file_md5
get_full_flags = ida_bytes.get_full_flags
get_db_byte = ida_bytes.get_db_byte

def get_bytes(ea, size, use_dbg: bool = False): ...
get_wide_byte = ida_bytes.get_wide_byte

def __DbgValue(ea, len): ...
def read_dbg_byte(ea): ...
def read_dbg_word(ea): ...
def read_dbg_dword(ea): ...
def read_dbg_qword(ea): ...
read_dbg_memory = ida_idd.dbg_read_memory

def write_dbg_memory(ea, data): ...
get_original_byte = ida_bytes.get_original_byte
get_wide_word = ida_bytes.get_wide_word
get_wide_dword = ida_bytes.get_wide_dword
get_qword = ida_bytes.get_qword

def GetFloat(ea): ...
def GetDouble(ea): ...
def get_name_ea_simple(name): ...
get_name_ea = ida_name.get_name_ea

def get_segm_by_sel(base): ...
get_screen_ea = ida_kernwin.get_screen_ea

def get_curline(): ...
def read_selection_start(): ...
def read_selection_end(): ...
def get_sreg(ea, reg): ...
next_addr = ida_bytes.next_addr
prev_addr = ida_bytes.prev_addr

def next_head(ea, maxea=...): ...
def prev_head(ea, minea: int = 0): ...
next_not_tail = ida_bytes.next_not_tail
prev_not_tail = ida_bytes.prev_not_tail
get_item_head = ida_bytes.get_item_head
get_item_end = ida_bytes.get_item_end

def get_item_size(ea): ...
def func_contains(func_ea, ea): ...

GN_VISIBLE: Incomplete
GN_COLORED: Incomplete
GN_DEMANGLED: Incomplete
GN_STRICT: Incomplete
GN_SHORT: Incomplete
GN_LONG: Incomplete
GN_LOCAL: Incomplete
GN_ISRET: Incomplete
GN_NOT_ISRET: Incomplete
calc_gtn_flags = ida_name.calc_gtn_flags

def get_name(ea, gtn_flags: int = 0): ...
def demangle_name(name, disable_mask): ...
def generate_disasm_line(ea, flags): ...

GENDSM_FORCE_CODE: Incomplete
GENDSM_MULTI_LINE: Incomplete

def GetDisasm(ea): ...
def print_insn_mnem(ea): ...
def print_operand(ea, n): ...
def get_operand_type(ea, n): ...

o_void: Incomplete
o_reg: Incomplete
o_mem: Incomplete
o_phrase: Incomplete
o_displ: Incomplete
o_imm: Incomplete
o_far: Incomplete
o_near: Incomplete
o_idpspec0: Incomplete
o_idpspec1: Incomplete
o_idpspec2: Incomplete
o_idpspec3: Incomplete
o_idpspec4: Incomplete
o_idpspec5: Incomplete
o_trreg: Incomplete
o_dbreg: Incomplete
o_crreg: Incomplete
o_fpreg: Incomplete
o_mmxreg: Incomplete
o_xmmreg: Incomplete
o_reglist: Incomplete
o_creglist: Incomplete
o_creg: Incomplete
o_fpreglist: Incomplete
o_text: Incomplete
o_cond: Incomplete
o_spr: Incomplete
o_twofpr: Incomplete
o_shmbme: Incomplete
o_crf: Incomplete
o_crb: Incomplete
o_dcr: Incomplete

def get_operand_value(ea, n): ...
GetCommentEx = ida_bytes.get_cmt
get_cmt = GetCommentEx
get_forced_operand = ida_bytes.get_forced_operand
BPU_1B: Incomplete
BPU_2B: Incomplete
BPU_4B: Incomplete
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
STRTYPE_LEN2: Incomplete
STRTYPE_LEN2_16: Incomplete
STRTYPE_LEN4: Incomplete
STRTYPE_LEN4_16: Incomplete
STRTYPE_C16 = STRTYPE_C_16

def get_strlit_contents(ea, length: int = -1, strtype=...): ...
def get_str_type(ea): ...
find_suspop = ida_search.find_suspop
find_code = ida_search.find_code
find_data = ida_search.find_data
find_unknown = ida_search.find_unknown
find_defined = ida_search.find_defined
find_imm = ida_search.find_imm
SEARCH_UP: Incomplete
SEARCH_DOWN: Incomplete
SEARCH_NEXT: Incomplete
SEARCH_CASE: Incomplete
SEARCH_REGEX: Incomplete
SEARCH_NOBRK: Incomplete
SEARCH_NOSHOW: Incomplete

def find_text(ea, flag, y, x, searchstr): ...
def find_binary(ea, flag, searchstr, radix: int = 16): ...
def process_config_line(directive): ...

INF_VERSION: int
INF_PROCNAME: int
INF_GENFLAGS: int
INF_LFLAGS: int
INF_DATABASE_CHANGE_COUNT: int
INF_CHANGE_COUNTER = INF_DATABASE_CHANGE_COUNT
INF_FILETYPE: int
FT_EXE_OLD: int
FT_COM_OLD: int
FT_BIN: int
FT_DRV: int
FT_WIN: int
FT_HEX: int
FT_MEX: int
FT_LX: int
FT_LE: int
FT_NLM: int
FT_COFF: int
FT_PE: int
FT_OMF: int
FT_SREC: int
FT_ZIP: int
FT_OMFLIB: int
FT_AR: int
FT_LOADER: int
FT_ELF: int
FT_W32RUN: int
FT_AOUT: int
FT_PRC: int
FT_EXE: int
FT_COM: int
FT_AIXAR: int
FT_MACHO: int
INF_OSTYPE: int
OSTYPE_MSDOS: int
OSTYPE_WIN: int
OSTYPE_OS2: int
OSTYPE_NETW: int
INF_APPTYPE: int
APPT_CONSOLE: int
APPT_GRAPHIC: int
APPT_PROGRAM: int
APPT_LIBRARY: int
APPT_DRIVER: int
APPT_1THREAD: int
APPT_MTHREAD: int
APPT_16BIT: int
APPT_32BIT: int
INF_ASMTYPE: int
INF_SPECSEGS: int
INF_AF: int

def _import_module_flag_sets(module, prefixes) -> None: ...

INF_AF2: int
INF_BASEADDR: int
INF_START_SS: int
INF_START_CS: int
INF_START_IP: int
INF_START_EA: int
INF_START_SP: int
INF_MAIN: int
INF_MIN_EA: int
INF_MAX_EA: int
INF_OMIN_EA: int
INF_OMAX_EA: int
INF_LOWOFF: int
INF_LOW_OFF = INF_LOWOFF
INF_HIGHOFF: int
INF_HIGH_OFF = INF_HIGHOFF
INF_MAXREF: int
INF_PRIVRANGE_START_EA: int
INF_START_PRIVRANGE = INF_PRIVRANGE_START_EA
INF_PRIVRANGE_END_EA: int
INF_END_PRIVRANGE = INF_PRIVRANGE_END_EA
INF_NETDELTA: int
INF_XREFNUM: int
INF_TYPE_XREFNUM: int
INF_TYPE_XREFS = INF_TYPE_XREFNUM
INF_REFCMTNUM: int
INF_REFCMTS = INF_REFCMTNUM
INF_XREFFLAG: int
INF_XREFS = INF_XREFFLAG
INF_MAX_AUTONAME_LEN: int
INF_NAMETYPE: int
INF_SHORT_DEMNAMES: int
INF_SHORT_DN = INF_SHORT_DEMNAMES
INF_LONG_DEMNAMES: int
INF_LONG_DN = INF_LONG_DEMNAMES
INF_DEMNAMES: int
INF_LISTNAMES: int
INF_INDENT: int
INF_CMT_INDENT: int
INF_COMMENT: int
INF_MARGIN: int
INF_LENXREF: int
INF_OUTFLAGS: int
INF_CMTFLG: int
INF_CMTFLAG = INF_CMTFLG
INF_LIMITER: int
INF_BORDER = INF_LIMITER
INF_BIN_PREFIX_SIZE: int
INF_BINPREF = INF_BIN_PREFIX_SIZE
INF_PREFFLAG: int
INF_STRLIT_FLAGS: int
INF_STRLIT_BREAK: int
INF_STRLIT_ZEROES: int
INF_STRTYPE: int
INF_STRLIT_PREF: int
INF_STRLIT_SERNUM: int
INF_DATATYPES: int
INF_CC_ID: int
COMP_MASK: int
COMP_UNK: int
COMP_MS: int
COMP_BC: int
COMP_WATCOM: int
COMP_GNU: int
COMP_VISAGE: int
COMP_BP: int
INF_CC_CM: int
INF_CC_SIZE_I: int
INF_CC_SIZE_B: int
INF_CC_SIZE_E: int
INF_CC_DEFALIGN: int
INF_CC_SIZE_S: int
INF_CC_SIZE_L: int
INF_CC_SIZE_LL: int
INF_CC_SIZE_LDBL: int
INF_COMPILER = INF_CC_ID
INF_MODEL = INF_CC_CM
INF_SIZEOF_INT = INF_CC_SIZE_I
INF_SIZEOF_BOOL = INF_CC_SIZE_B
INF_SIZEOF_ENUM = INF_CC_SIZE_E
INF_SIZEOF_ALGN = INF_CC_DEFALIGN
INF_SIZEOF_SHORT = INF_CC_SIZE_S
INF_SIZEOF_LONG = INF_CC_SIZE_L
INF_SIZEOF_LLONG = INF_CC_SIZE_LL
INF_SIZEOF_LDBL = INF_CC_SIZE_LDBL
INF_ABIBITS: int
INF_APPCALL_OPTIONS: int
_INF_attrs_accessors: Incomplete

def get_inf_attr(attr): ...
def set_inf_attr(attr, value): ...
set_processor_type = ida_idp.set_processor_type
SETPROC_IDB: Incomplete
SETPROC_LOADER: Incomplete
SETPROC_LOADER_NON_FATAL: Incomplete
SETPROC_USER: Incomplete

def SetPrcsr(processor): ...
def get_processor_name(): ...
set_target_assembler = ida_idp.set_target_assembler

def batch(batch): ...
def process_ui_action(name, flags: int = 0): ...
ask_seg = ida_kernwin.ask_seg
ask_yn = ida_kernwin.ask_yn
msg = ida_kernwin.msg
warning = ida_kernwin.warning
error = ida_kernwin.error
set_ida_state = ida_auto.set_ida_state
IDA_STATUS_READY: int
IDA_STATUS_THINKING: int
IDA_STATUS_WAITING: int
IDA_STATUS_WORK: int
refresh_idaview_anyway = ida_kernwin.refresh_idaview_anyway
refresh_lists = ida_kernwin.refresh_choosers

def sel2para(sel): ...
def find_selector(val): ...
set_selector = ida_segment.set_selector
del_selector = ida_segment.del_selector

def get_first_seg(): ...
def get_next_seg(ea): ...
def get_segm_start(ea): ...
def get_segm_end(ea): ...
def get_segm_name(ea): ...
def add_segm_ex(startea, endea, base, use32, align, comb, flags): ...

ADDSEG_NOSREG: Incomplete
ADDSEG_OR_DIE: Incomplete
ADDSEG_NOTRUNC: Incomplete
ADDSEG_QUIET: Incomplete
ADDSEG_FILLGAP: Incomplete
ADDSEG_SPARSE: Incomplete

def AddSeg(startea, endea, base, use32, align, comb): ...
del_segm = ida_segment.del_segm
SEGMOD_KILL: Incomplete
SEGMOD_KEEP: Incomplete
SEGMOD_SILENT: Incomplete

def set_segment_bounds(ea, startea, endea, flags): ...
def set_segm_name(ea, name): ...
def set_segm_class(ea, segclass): ...
def set_segm_alignment(ea, alignment): ...
_scope = ida_segment.segment_t
_scope = ida_segment
saAbs: Incomplete
saRelByte: Incomplete
saRelWord: Incomplete
saRelPara: Incomplete
saRelPage: Incomplete
saRelDble: Incomplete
saRel4K: Incomplete
saGroup: Incomplete
saRel32Bytes: Incomplete
saRel64Bytes: Incomplete
saRelQword: Incomplete

def set_segm_combination(segea, comb): ...

scPriv: Incomplete
scPub: Incomplete
scPub2: Incomplete
scStack: Incomplete
scCommon: Incomplete
scPub3: Incomplete

def set_segm_addressing(ea, bitness): ...
def selector_by_name(segname): ...
def set_default_sreg_value(ea, reg, value): ...
def set_segm_type(segea, segtype): ...

SEG_NORM: Incomplete
SEG_XTRN: Incomplete
SEG_CODE: Incomplete
SEG_DATA: Incomplete
SEG_IMP: Incomplete
SEG_GRP: Incomplete
SEG_NULL: Incomplete
SEG_UNDF: Incomplete
SEG_BSS: Incomplete
SEG_ABSSYM: Incomplete
SEG_COMM: Incomplete
SEG_IMEM: Incomplete

def get_segm_attr(segea, attr): ...
def set_segm_attr(segea, attr, value): ...

SEGATTR_START: int
SEGATTR_END: int
SEGATTR_ORGBASE: int
SEGATTR_ALIGN: int
SEGATTR_COMB: int
SEGATTR_PERM: int
SEGATTR_BITNESS: int
SEGATTR_FLAGS: int
SEGATTR_SEL: int
SEGATTR_ES: int
SEGATTR_CS: int
SEGATTR_SS: int
SEGATTR_DS: int
SEGATTR_FS: int
SEGATTR_GS: int
SEGATTR_TYPE: int
SEGATTR_COLOR: int
_SEGATTRMAP: Incomplete
SFL_COMORG: int
SFL_OBOK: int
SFL_HIDDEN: int
SFL_DEBUG: int
SFL_LOADER: int
SFL_HIDETYPE: int

def move_segm(ea, to, flags): ...

MSF_SILENT: int
MSF_NOFIX: int
MSF_LDKEEP: int
MSF_FIXONCE: int
MOVE_SEGM_OK: int
MOVE_SEGM_PARAM: int
MOVE_SEGM_ROOM: int
MOVE_SEGM_IDP: int
MOVE_SEGM_CHUNK: int
MOVE_SEGM_LOADER: int
MOVE_SEGM_ODD: int
MOVE_SEGM_ORPHAN: Incomplete
MOVE_SEGM_DEBUG: Incomplete
MOVE_SEGM_SOURCEFILES: Incomplete
MOVE_SEGM_MAPPING: Incomplete
MOVE_SEGM_INVAL: Incomplete
rebase_program = ida_segment.rebase_program
set_storage_type = ida_bytes.change_storage_type
STT_VA: int
STT_MM: int
fl_CF: int
fl_CN: int
fl_JF: int
fl_JN: int
fl_F: int
XREF_USER: int
add_cref = ida_xref.add_cref
del_cref = ida_xref.del_cref
get_first_cref_from = ida_xref.get_first_cref_from
get_next_cref_from = ida_xref.get_next_cref_from
get_first_cref_to = ida_xref.get_first_cref_to
get_next_cref_to = ida_xref.get_next_cref_to
get_first_fcref_from = ida_xref.get_first_fcref_from
get_next_fcref_from = ida_xref.get_next_fcref_from
get_first_fcref_to = ida_xref.get_first_fcref_to
get_next_fcref_to = ida_xref.get_next_fcref_to
dr_O: Incomplete
dr_W: Incomplete
dr_R: Incomplete
dr_T: Incomplete
dr_I: Incomplete
add_dref = ida_xref.add_dref
del_dref = ida_xref.del_dref
get_first_dref_from = ida_xref.get_first_dref_from
get_next_dref_from = ida_xref.get_next_dref_from
get_first_dref_to = ida_xref.get_first_dref_to
get_next_dref_to = ida_xref.get_next_dref_to

def get_xref_type() -> None: ...
def fopen(f, mode) -> None: ...
def fclose(handle) -> None: ...
def filelength(handle) -> None: ...
def fseek(handle, offset, origin) -> None: ...
def ftell(handle) -> None: ...
def LoadFile(filepath, pos, ea, size): ...
def loadfile(filepath, pos, ea, size): ...
def SaveFile(filepath, pos, ea, size): ...
def savefile(filepath, pos, ea, size): ...
def fgetc(handle) -> None: ...
def fputc(byte, handle) -> None: ...
def fprintf(handle, format, *args) -> None: ...
def readshort(handle, mostfirst) -> None: ...
def readlong(handle, mostfirst) -> None: ...
def writeshort(handle, word, mostfirst) -> None: ...
def writelong(handle, dword, mostfirst) -> None: ...
def readstr(handle) -> None: ...
def writestr(handle, s) -> None: ...
add_func = ida_funcs.add_func
del_func = ida_funcs.del_func
set_func_end = ida_funcs.set_func_end

def get_next_func(ea): ...
def get_prev_func(ea): ...
def get_func_attr(ea, attr): ...
def set_func_attr(ea, attr, value): ...

FUNCATTR_START: int
FUNCATTR_END: int
FUNCATTR_FLAGS: int
FUNCATTR_FRAME: int
FUNCATTR_FRSIZE: int
FUNCATTR_FRREGS: int
FUNCATTR_ARGSIZE: int
FUNCATTR_FPD: int
FUNCATTR_COLOR: int
FUNCATTR_OWNER: int
FUNCATTR_REFQTY: int
_FUNCATTRMAP: Incomplete

def get_func_flags(ea): ...
_scope = ida_funcs.func_t
_scope = ida_funcs
FUNC_NORET: Incomplete
FUNC_FAR: Incomplete
FUNC_LIB: Incomplete
FUNC_STATIC: Incomplete
FUNC_FRAME: Incomplete
FUNC_USERFAR: Incomplete
FUNC_HIDDEN: Incomplete
FUNC_THUNK: Incomplete
FUNC_BOTTOMBP: Incomplete
FUNC_NORET_PENDING: Incomplete
FUNC_SP_READY: Incomplete
FUNC_PURGED_OK: Incomplete
FUNC_TAIL: Incomplete
FUNC_LUMINA: Incomplete
FUNC_OUTLINE: Incomplete

def set_func_flags(ea, flags): ...
def get_func_name(ea): ...
def get_func_cmt(ea, repeatable): ...
def set_func_cmt(ea, cmt, repeatable): ...
def choose_func(title): ...
def get_func_off_str(ea): ...
def find_func_end(ea): ...
def get_frame_id(ea): ...
def get_frame_lvar_size(ea): ...
def get_frame_regs_size(ea): ...
def get_frame_args_size(ea): ...
def get_frame_size(ea): ...
def set_frame_size(ea, lvsize, frregs, argsize): ...
def get_spd(ea): ...
def get_sp_delta(ea): ...
def add_auto_stkpnt(func_ea, ea, delta): ...
add_user_stkpnt = ida_frame.add_user_stkpnt

def del_stkpnt(func_ea, ea): ...
def get_min_spd_ea(func_ea): ...
recalc_spd = ida_frame.recalc_spd
get_entry_qty = ida_entry.get_entry_qty
add_entry = ida_entry.add_entry
get_entry_ordinal = ida_entry.get_entry_ordinal
get_entry = ida_entry.get_entry
get_entry_name = ida_entry.get_entry_name
rename_entry = ida_entry.rename_entry
get_next_fixup_ea = ida_fixup.get_next_fixup_ea
get_prev_fixup_ea = ida_fixup.get_prev_fixup_ea

def get_fixup_target_type(ea): ...

FIXUP_OFF8: int
FIXUP_OFF16: int
FIXUP_SEG16: int
FIXUP_PTR32: int
FIXUP_OFF32: int
FIXUP_PTR48: int
FIXUP_HI8: int
FIXUP_HI16: int
FIXUP_LOW8: int
FIXUP_LOW16: int
FIXUP_OFF64: int
FIXUP_CUSTOM: int

def get_fixup_target_flags(ea): ...

FIXUPF_REL: int
FIXUPF_EXTDEF: int
FIXUPF_UNUSED: int
FIXUPF_CREATED: int

def get_fixup_target_sel(ea): ...
def get_fixup_target_off(ea): ...
def get_fixup_target_dis(ea): ...
def set_fixup(ea, fixuptype, fixupflags, targetsel, targetoff, displ) -> None: ...
del_fixup = ida_fixup.del_fixup
put_bookmark = ida_idc.mark_position
get_bookmark = ida_idc.get_marked_pos
get_bookmark_desc = ida_idc.get_mark_comment
get_struc_qty = ida_struct.get_struc_qty
get_first_struc_idx = ida_struct.get_first_struc_idx
get_last_struc_idx = ida_struct.get_last_struc_idx
get_next_struc_idx = ida_struct.get_next_struc_idx
get_prev_struc_idx = ida_struct.get_prev_struc_idx
get_struc_idx = ida_struct.get_struc_idx
get_struc_by_idx = ida_struct.get_struc_by_idx
get_struc_id = ida_struct.get_struc_id
get_struc_name = ida_struct.get_struc_name
get_struc_cmt = ida_struct.get_struc_cmt
get_struc_size = ida_struct.get_struc_size

def get_member_qty(sid): ...
def get_member_id(sid, member_offset): ...
def get_prev_offset(sid, offset): ...
def get_next_offset(sid, offset): ...
def get_first_member(sid): ...
def get_last_member(sid): ...
def get_member_offset(sid, member_name): ...
def get_member_name(sid, member_offset): ...
def get_member_cmt(sid, member_offset, repeatable): ...
def get_member_size(sid, member_offset): ...
def get_member_flag(sid, member_offset): ...
def get_member_strid(sid, member_offset): ...
def is_union(sid): ...
def add_struc(index, name, is_union): ...
def del_struc(sid): ...
def set_struc_idx(sid, index): ...
set_struc_name = ida_struct.set_struc_name
set_struc_cmt = ida_struct.set_struc_cmt

def add_struc_member(sid, name, offset, flag, typeid, nbytes, target: int = -1, tdelta: int = 0, reftype=...): ...

STRUC_ERROR_MEMBER_NAME: int
STRUC_ERROR_MEMBER_OFFSET: int
STRUC_ERROR_MEMBER_SIZE: int
STRUC_ERROR_MEMBER_TINFO: int
STRUC_ERROR_MEMBER_STRUCT: int
STRUC_ERROR_MEMBER_UNIVAR: int
STRUC_ERROR_MEMBER_VARLAST: int

def del_struc_member(sid, member_offset): ...
def set_member_name(sid, member_offset, name): ...
def set_member_type(sid, member_offset, flag, typeid, nitems, target: int = -1, tdelta: int = 0, reftype=...): ...
def set_member_cmt(sid, member_offset, comment, repeatable): ...
def expand_struc(sid, offset, delta, recalc): ...
def get_fchunk_attr(ea, attr): ...
def set_fchunk_attr(ea, attr, value): ...
get_fchunk_referer = ida_funcs.get_fchunk_referer

def get_next_fchunk(ea): ...
def get_prev_fchunk(ea): ...
def append_func_tail(funcea, ea1, ea2): ...
def remove_fchunk(funcea, tailea): ...
def set_tail_owner(tailea, funcea): ...
def first_func_chunk(funcea): ...
def next_func_chunk(funcea, tailea): ...
get_enum_qty = ida_enum.get_enum_qty
getn_enum = ida_enum.getn_enum
get_enum_idx = ida_enum.get_enum_idx
get_enum = ida_enum.get_enum
get_enum_name = ida_enum.get_enum_name
get_enum_cmt = ida_enum.get_enum_cmt
get_enum_size = ida_enum.get_enum_size
get_enum_width = ida_enum.get_enum_width
get_enum_flag = ida_enum.get_enum_flag
get_enum_member_by_name = ida_enum.get_enum_member_by_name
get_enum_member_value = ida_enum.get_enum_member_value
get_enum_member_bmask = ida_enum.get_enum_member_bmask
get_enum_member_enum = ida_enum.get_enum_member_enum

def get_enum_member(enum_id, value, serial, bmask): ...
get_first_bmask = ida_enum.get_first_bmask
get_last_bmask = ida_enum.get_last_bmask
get_next_bmask = ida_enum.get_next_bmask
get_prev_bmask = ida_enum.get_prev_bmask

def get_bmask_name(enum_id, bmask): ...
def get_bmask_cmt(enum_id, bmask, repeatable): ...
def set_bmask_name(enum_id, bmask, name): ...
def set_bmask_cmt(enum_id, bmask, cmt, repeatable): ...
def get_first_enum_member(enum_id, bmask): ...
def get_last_enum_member(enum_id, bmask): ...
def get_next_enum_member(enum_id, value, bmask): ...
def get_prev_enum_member(enum_id, value, bmask): ...
def get_enum_member_name(const_id): ...
def get_enum_member_cmt(const_id, repeatable): ...
def add_enum(idx, name, flag): ...
del_enum = ida_enum.del_enum
set_enum_idx = ida_enum.set_enum_idx
set_enum_name = ida_enum.set_enum_name
set_enum_cmt = ida_enum.set_enum_cmt
set_enum_flag = ida_enum.set_enum_flag
set_enum_bf = ida_enum.set_enum_bf
set_enum_width = ida_enum.set_enum_width
is_bf = ida_enum.is_bf

def add_enum_member(enum_id, name, value, bmask): ...

ENUM_MEMBER_ERROR_NAME: Incomplete
ENUM_MEMBER_ERROR_VALUE: Incomplete
ENUM_MEMBER_ERROR_ENUM: Incomplete
ENUM_MEMBER_ERROR_MASK: Incomplete
ENUM_MEMBER_ERROR_ILLV: Incomplete

def del_enum_member(enum_id, value, serial, bmask): ...
set_enum_member_name = ida_enum.set_enum_member_name
set_enum_member_cmt = ida_enum.set_enum_member_cmt
_IDC_ARRAY_PREFIX: str

def __l2m1(v): ...
def __m1tol(v): ...

AR_LONG: Incomplete
AR_STR: Incomplete

class __dummy_netnode:
    def rename(self, *args): ...
    def kill(self, *args) -> None: ...
    def index(self, *args): ...
    def altset(self, *args): ...
    def supset(self, *args): ...
    def altval(self, *args): ...
    def supval(self, *args): ...
    def altdel(self, *args): ...
    def supdel(self, *args): ...
    def altfirst(self, *args): ...
    def supfirst(self, *args): ...
    def altlast(self, *args): ...
    def suplast(self, *args): ...
    def altnext(self, *args): ...
    def supnext(self, *args): ...
    def altprev(self, *args): ...
    def supprev(self, *args): ...
    def hashset(self, *args): ...
    def hashval(self, *args): ...
    def hashstr(self, *args): ...
    def hashstr_buf(self, *args): ...
    def hashset_idx(self, *args): ...
    def hashset_buf(self, *args): ...
    def hashval_long(self, *args): ...
    def hashdel(self, *args): ...
    def hashfirst(self, *args): ...
    def hashnext(self, *args): ...
    def hashprev(self, *args): ...
    def hashlast(self, *args): ...

def __GetArrayById(array_id): ...
def create_array(name): ...
def get_array_id(name): ...
def rename_array(array_id, newname): ...
def delete_array(array_id) -> None: ...
def set_array_long(array_id, idx, value): ...
def set_array_string(array_id, idx, value): ...
def get_array_element(tag, array_id, idx): ...
def del_array_element(tag, array_id, idx): ...
def get_first_index(tag, array_id): ...
def get_last_index(tag, array_id): ...
def get_next_index(tag, array_id, idx): ...
def get_prev_index(tag, array_id, idx): ...
def set_hash_long(hash_id, key, value): ...
def get_hash_long(hash_id, key): ...
def set_hash_string(hash_id, key, value): ...
def get_hash_string(hash_id, key): ...
def del_hash_string(hash_id, key): ...
def get_first_hash_key(hash_id): ...
def get_last_hash_key(hash_id): ...
def get_next_hash_key(hash_id, key): ...
def get_prev_hash_key(hash_id, key): ...
add_sourcefile = ida_lines.add_sourcefile
get_sourcefile = ida_lines.get_sourcefile
del_sourcefile = ida_lines.del_sourcefile
set_source_linnum = ida_nalt.set_source_linnum
get_source_linnum = ida_nalt.get_source_linnum
del_source_linnum = ida_nalt.del_source_linnum

def add_default_til(name): ...
def import_type(idx, type_name): ...
def get_type(ea): ...
def sizeof(typestr): ...
SizeOf = sizeof

def get_tinfo(ea): ...
def get_local_tinfo(ordinal): ...
def guess_type(ea): ...

TINFO_GUESSED: int
TINFO_DEFINITE: int
TINFO_DELAYFUNC: int

def apply_type(ea, py_type, flags=...): ...

PT_SIL: Incomplete
PT_NDC: Incomplete
PT_TYP: Incomplete
PT_VAR: Incomplete
PT_PACKMASK: Incomplete
PT_HIGH: Incomplete
PT_LOWER: Incomplete
PT_REPLACE: Incomplete
PT_RAWARGS: Incomplete
PT_SILENT = PT_SIL
PT_PAKDEF: int
PT_PAK1: int
PT_PAK2: int
PT_PAK4: int
PT_PAK8: int
PT_PAK16: int
PT_FILE: int

def SetType(ea, newtype): ...
def parse_decl(inputtype, flags): ...
def parse_decls(inputtype, flags: int = 0): ...
def print_decls(ordinals, flags): ...

PDF_INCL_DEPS: int
PDF_DEF_FWD: int
PDF_DEF_BASE: int
PDF_HEADER_CMT: int

def get_ordinal_qty(): ...
def set_local_type(ordinal, input, flags): ...
def GetLocalType(ordinal, flags): ...

PRTYPE_1LINE: int
PRTYPE_MULTI: int
PRTYPE_TYPE: int
PRTYPE_PRAGMA: int
PRTYPE_SEMI: int
PRTYPE_CPP: int
PRTYPE_DEF: int
PRTYPE_NOARGS: int
PRTYPE_NOARRS: int
PRTYPE_NORES: int
PRTYPE_RESTORE: int
PRTYPE_NOREGEX: int
PRTYPE_COLORED: int
PRTYPE_METHODS: int
PRTYPE_1LINCMT: int

def get_numbered_type_name(ordinal): ...
add_hidden_range = ida_bytes.add_hidden_range

def update_hidden_range(ea, visible): ...
del_hidden_range = ida_bytes.del_hidden_range
load_debugger = ida_dbg.load_debugger
start_process = ida_dbg.start_process
exit_process = ida_dbg.exit_process
suspend_process = ida_dbg.suspend_process
get_processes = ida_dbg.get_processes
attach_process = ida_dbg.attach_process
detach_process = ida_dbg.detach_process
get_thread_qty = ida_dbg.get_thread_qty
getn_thread = ida_dbg.getn_thread
get_current_thread = ida_dbg.get_current_thread
getn_thread_name = ida_dbg.getn_thread_name
select_thread = ida_dbg.select_thread
suspend_thread = ida_dbg.suspend_thread
resume_thread = ida_dbg.resume_thread

def _get_modules() -> Generator[Incomplete, None, None]: ...
def get_first_module(): ...
def get_next_module(base): ...
def get_module_name(base): ...
def get_module_size(base): ...
step_into = ida_dbg.step_into
step_over = ida_dbg.step_over
run_to = ida_dbg.run_to
step_until_ret = ida_dbg.step_until_ret
wait_for_next_event = ida_dbg.wait_for_next_event

def resume_process(): ...
def send_dbg_command(cmd): ...

WFNE_ANY: int
WFNE_SUSP: int
WFNE_SILENT: int
WFNE_CONT: int
WFNE_NOWAIT: int
NOTASK: int
DBG_ERROR: int
DBG_TIMEOUT: int
PROCESS_STARTED: int
PROCESS_EXITED: int
THREAD_STARTED: int
THREAD_EXITED: int
BREAKPOINT: int
STEP: int
EXCEPTION: int
LIB_LOADED: int
LIB_UNLOADED: int
INFORMATION: int
PROCESS_ATTACHED: int
PROCESS_DETACHED: int
PROCESS_SUSPENDED: int
refresh_debugger_memory = ida_dbg.refresh_debugger_memory
take_memory_snapshot = ida_segment.take_memory_snapshot
get_process_state = ida_dbg.get_process_state
DSTATE_SUSP: int
DSTATE_NOTASK: int
DSTATE_RUN: int
DSTATE_RUN_WAIT_ATTACH: int
DSTATE_RUN_WAIT_END: int

def get_event_id(): ...
def get_event_pid(): ...
def get_event_tid(): ...
def get_event_ea(): ...
def is_event_handled(): ...
def get_event_module_name(): ...
def get_event_module_base(): ...
def get_event_module_size(): ...
def get_event_exit_code(): ...
def get_event_info(): ...
def get_event_bpt_hea(): ...
def get_event_exc_code(): ...
def get_event_exc_ea(): ...
def can_exc_continue(): ...
def get_event_exc_info(): ...
set_debugger_options = ida_dbg.set_debugger_options
DOPT_SEGM_MSGS: int
DOPT_START_BPT: int
DOPT_THREAD_MSGS: int
DOPT_THREAD_BPT: int
DOPT_BPT_MSGS: int
DOPT_LIB_MSGS: int
DOPT_LIB_BPT: int
DOPT_INFO_MSGS: int
DOPT_INFO_BPT: int
DOPT_REAL_MEMORY: int
DOPT_REDO_STACK: int
DOPT_ENTRY_BPT: int
DOPT_EXCDLG: int
EXCDLG_NEVER: int
EXCDLG_UNKNOWN: int
EXCDLG_ALWAYS: int
DOPT_LOAD_DINFO: int
get_debugger_event_cond = ida_dbg.get_debugger_event_cond
set_debugger_event_cond = ida_dbg.set_debugger_event_cond
set_remote_debugger = ida_dbg.set_remote_debugger
define_exception = ida_dbg.define_exception
EXC_BREAK: int
EXC_HANDLE: int
get_reg_value = ida_dbg.get_reg_val

def set_reg_value(value, name): ...
get_bpt_qty = ida_dbg.get_bpt_qty

def get_bpt_ea(n): ...
def get_bpt_attr(ea, bptattr): ...

BPTATTR_EA: int
BPTATTR_SIZE: int
BPTATTR_TYPE: int
BPT_WRITE: int
BPT_RDWR: int
BPT_SOFT: int
BPT_EXEC: int
BPT_DEFAULT = BPT_SOFT | BPT_EXEC
BPTATTR_COUNT: int
BPTATTR_FLAGS: int
BPT_BRK: int
BPT_TRACE: int
BPT_UPDMEM: int
BPT_ENABLED: int
BPT_LOWCND: int
BPT_TRACEON: int
BPT_TRACE_INSN: int
BPT_TRACE_FUNC: int
BPT_TRACE_BBLK: int
BPTATTR_COND: int
BPTATTR_PID: int
BPTATTR_TID: int
BPLT_ABS: int
BPLT_REL: int
BPLT_SYM: int

def set_bpt_attr(address, bptattr, value): ...
def set_bpt_cond(ea, cnd, is_lowcnd: int = 0): ...
add_bpt = ida_dbg.add_bpt
del_bpt = ida_dbg.del_bpt
enable_bpt = ida_dbg.enable_bpt
check_bpt = ida_dbg.check_bpt
BPTCK_NONE: int
BPTCK_NO: int
BPTCK_YES: int
BPTCK_ACT: int

def enable_tracing(trace_level, enable): ...

TRACE_STEP: int
TRACE_INSN: int
TRACE_FUNC: int
get_step_trace_options = ida_dbg.get_step_trace_options
set_step_trace_options = ida_dbg.set_step_trace_options
ST_OVER_DEBUG_SEG: int
ST_OVER_LIB_FUNC: int
ST_ALREADY_LOGGED: int
ST_SKIP_LOOPS: int
load_trace_file = ida_dbg.load_trace_file
save_trace_file = ida_dbg.save_trace_file
is_valid_trace_file = ida_dbg.is_valid_trace_file
diff_trace_file = ida_dbg.diff_trace_file

def clear_trace(filename): ...
get_trace_file_desc = ida_dbg.get_trace_file_desc
set_trace_file_desc = ida_dbg.set_trace_file_desc
get_tev_qty = ida_dbg.get_tev_qty
get_tev_ea = ida_dbg.get_tev_ea
TEV_NONE: int
TEV_INSN: int
TEV_CALL: int
TEV_RET: int
TEV_BPT: int
TEV_MEM: int
TEV_EVENT: int
get_tev_type = ida_dbg.get_tev_type
get_tev_tid = ida_dbg.get_tev_tid
get_tev_reg = ida_dbg.get_tev_reg_val
get_tev_mem_qty = ida_dbg.get_tev_reg_mem_qty
get_tev_mem = ida_dbg.get_tev_reg_mem
get_tev_mem_ea = ida_dbg.get_tev_reg_mem_ea
get_call_tev_callee = ida_dbg.get_call_tev_callee
get_ret_tev_return = ida_dbg.get_ret_tev_return
get_bpt_tev_ea = ida_dbg.get_bpt_tev_ea

def get_color(ea, what): ...

CIC_ITEM: int
CIC_FUNC: int
CIC_SEGM: int
DEFCOLOR: int

def set_color(ea, what, color): ...
def force_bl_jump(ea): ...
def force_bl_call(ea): ...
def set_flag(off, bit, value) -> None: ...
def here(): ...
def is_mapped(ea): ...

ARGV: Incomplete
