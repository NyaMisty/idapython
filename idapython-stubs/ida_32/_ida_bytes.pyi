# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

ALOPT_APPEND: int
ALOPT_IGNCLT: int
ALOPT_IGNHEADS: int
ALOPT_IGNPRINT: int
ALOPT_MAX4K: int
ALOPT_ONLYTERM: int
BIN_SEARCH_BACKWARD: int
BIN_SEARCH_BITMASK: int
BIN_SEARCH_CASE: int
BIN_SEARCH_FORWARD: int
BIN_SEARCH_INITED: int
BIN_SEARCH_NOBREAK: int
BIN_SEARCH_NOCASE: int
BIN_SEARCH_NOSHOW: int
DELIT_DELNAMES: int
DELIT_EXPAND: int
DELIT_KEEPFUNC: int
DELIT_NOCMT: int
DELIT_NOTRUNC: int
DELIT_NOUNAME: int
DELIT_SIMPLE: int
DTP_NODUP: int
DT_TYPE: int
FF_0CHAR: int
FF_0CUST: int
FF_0ENUM: int
FF_0FLT: int
FF_0FOP: int
FF_0NUMB: int
FF_0NUMD: int
FF_0NUMH: int
FF_0NUMO: int
FF_0OFF: int
FF_0SEG: int
FF_0STK: int
FF_0STRO: int
FF_0VOID: int
FF_1CHAR: int
FF_1CUST: int
FF_1ENUM: int
FF_1FLT: int
FF_1FOP: int
FF_1NUMB: int
FF_1NUMD: int
FF_1NUMH: int
FF_1NUMO: int
FF_1OFF: int
FF_1SEG: int
FF_1STK: int
FF_1STRO: int
FF_1VOID: int
FF_ALIGN: int
FF_ANYNAME: int
FF_BNOT: int
FF_BYTE: int
FF_CODE: int
FF_COMM: int
FF_CUSTOM: int
FF_DATA: int
FF_DOUBLE: int
FF_DWORD: int
FF_FLOAT: int
FF_FLOW: int
FF_FUNC: int
FF_IMMD: int
FF_IVL: int
FF_JUMP: int
FF_LABL: int
FF_LINE: int
FF_NAME: int
FF_N_CHAR: int
FF_N_CUST: int
FF_N_ENUM: int
FF_N_FLT: int
FF_N_FOP: int
FF_N_NUMB: int
FF_N_NUMD: int
FF_N_NUMH: int
FF_N_NUMO: int
FF_N_OFF: int
FF_N_SEG: int
FF_N_STK: int
FF_N_STRO: int
FF_N_VOID: int
FF_OWORD: int
FF_PACKREAL: int
FF_QWORD: int
FF_REF: int
FF_SIGN: int
FF_STRLIT: int
FF_STRUCT: int
FF_TAIL: int
FF_TBYTE: int
FF_UNK: int
FF_UNUSED: int
FF_WORD: int
FF_YWORD: int
FF_ZWORD: int
GFE_IDB_VALUE: int
GFE_VALUE: int
GMB_READALL: int
GMB_WAITBOX: int
ITEM_END_CANCEL: int
ITEM_END_FIXUP: int
ITEM_END_INITED: int
ITEM_END_NAME: int
ITEM_END_XREF: int
MS_0TYPE: int
MS_1TYPE: int
MS_CLS: int
MS_CODE: int
MS_COMM: int
MS_N_TYPE: int
MS_VAL: int
OPND_ALL: int
OPND_MASK: int
OPND_OUTER: int
PBSENC_ALL: int
PBSENC_DEF1BPU: int
PSTF_ATTRIB: int
PSTF_ENC: int
PSTF_HOTKEY: int
PSTF_ONLY_ENC: int
PSTF_TBRIEF: int
PSTF_TINLIN: int
PSTF_TMASK: int
PSTF_TNORM: int
STRCONV_ESCAPE: int
STRCONV_INCLLEN: int
STRCONV_REPLCHAR: int
SWIG_PYTHON_LEGACY_BOOL: int

def add_byte(ea, value) -> Any: ...
def add_dword(ea, value) -> Any: ...
def add_hidden_range(ea1, ea2, description, header, footer, color=...) -> bool: ...
def add_mapping(_from, to, size) -> bool: ...
def add_qword(ea, value) -> Any: ...
def add_word(ea, value) -> Any: ...
def align_flag() -> flags64_t: ...
def append_cmt(ea, str, rptble) -> bool: ...
def attach_custom_data_format(dtid, dfid) -> bool: ...
def bin_flag() -> flags64_t: ...
@overload
def bin_search(start_ea, end_ea, data, flags) -> ea_t: ...
@overload
def bin_search(start_ea, end_ea, image, imask, step, flags) -> ea_t: ...
def bin_search3(start_ea, end_ea, data, flags) -> ea_t: ...
def byte_flag() -> flags64_t: ...
def bytesize(ea) -> int: ...
def calc_def_align(ea, mina, maxa) -> int: ...
def calc_dflags(f, force) -> flags64_t: ...
def calc_max_align(endea) -> int: ...
def calc_max_item_end(ea, how=...) -> ea_t: ...
def calc_min_align(length) -> int: ...
def can_define_item(ea, length, flags) -> bool: ...
def change_storage_type(start_ea, end_ea, stt) -> error_t: ...
def char_flag() -> flags64_t: ...
def chunk_size(ea) -> asize_t: ...
def chunk_start(ea) -> ea_t: ...
def clr_lzero(ea, n) -> bool: ...
def clr_op_type(ea, n) -> bool: ...
def code_flag() -> flags64_t: ...
def combine_flags(F) -> flags64_t: ...
def compiled_binpat_t___eq__(self, r) -> bool: ...
def compiled_binpat_t___ne__(self, r) -> bool: ...
def compiled_binpat_t_all_bytes_defined(self) -> bool: ...
def compiled_binpat_t_bytes_get(*args, **kwargs): ...
def compiled_binpat_t_bytes_set(self, bytes) -> Any: ...
def compiled_binpat_t_encidx_get(self) -> int: ...
def compiled_binpat_t_encidx_set(self, encidx) -> Any: ...
def compiled_binpat_t_mask_get(*args, **kwargs): ...
def compiled_binpat_t_mask_set(self, mask) -> Any: ...
def compiled_binpat_t_qclear(self) -> Any: ...
def compiled_binpat_t_strlits_get(self) -> rangevec_t: ...
def compiled_binpat_t_strlits_set(self, strlits) -> Any: ...
def compiled_binpat_t_swiginit(*args, **kwargs): ...
def compiled_binpat_t_swigregister(*args, **kwargs): ...
def compiled_binpat_vec_t___eq__(self, r) -> bool: ...
def compiled_binpat_vec_t___getitem__(self, i) -> compiled_binpat_t: ...
def compiled_binpat_vec_t___len__(self) -> size_t: ...
def compiled_binpat_vec_t___ne__(self, r) -> bool: ...
def compiled_binpat_vec_t___setitem__(self, i, v) -> Any: ...
def compiled_binpat_vec_t__del(self, x) -> bool: ...
def compiled_binpat_vec_t_add_unique(self, x) -> bool: ...
def compiled_binpat_vec_t_at(self, _idx) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_begin(self) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_begin(self) -> compiled_binpat_t: ...
def compiled_binpat_vec_t_capacity(self) -> size_t: ...
def compiled_binpat_vec_t_clear(self) -> Any: ...
def compiled_binpat_vec_t_empty(self) -> bool: ...
@overload
def compiled_binpat_vec_t_end(self) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_end(self) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_erase(self, it) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_erase(self, first, last) -> compiled_binpat_t: ...
def compiled_binpat_vec_t_extract(self) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_find(self, x) -> compiled_binpat_t: ...
@overload
def compiled_binpat_vec_t_find(self, x) -> compiled_binpat_t: ...
def compiled_binpat_vec_t_grow(self, x=...) -> Any: ...
def compiled_binpat_vec_t_has(self, x) -> bool: ...
def compiled_binpat_vec_t_inject(self, s, len) -> Any: ...
def compiled_binpat_vec_t_insert(self, it, x) -> compiled_binpat_t: ...
def compiled_binpat_vec_t_pop_back(self) -> Any: ...
@overload
def compiled_binpat_vec_t_push_back(self, x) -> Any: ...
@overload
def compiled_binpat_vec_t_push_back(self) -> compiled_binpat_t: ...
def compiled_binpat_vec_t_qclear(self) -> Any: ...
def compiled_binpat_vec_t_reserve(self, cnt) -> Any: ...
@overload
def compiled_binpat_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def compiled_binpat_vec_t_resize(self, _newsize) -> Any: ...
def compiled_binpat_vec_t_size(self) -> size_t: ...
def compiled_binpat_vec_t_swap(self, r) -> Any: ...
def compiled_binpat_vec_t_swiginit(*args, **kwargs): ...
def compiled_binpat_vec_t_swigregister(*args, **kwargs): ...
def compiled_binpat_vec_t_truncate(self) -> Any: ...
def create_16bit_data(ea, length) -> bool: ...
def create_32bit_data(ea, length) -> bool: ...
def create_align(ea, length, alignment) -> bool: ...
def create_byte(ea, length, force=...) -> bool: ...
def create_custdata(ea, length, dtid, fid, force=...) -> bool: ...
def create_data(ea, dataflag, size, tid) -> bool: ...
def create_double(ea, length, force=...) -> bool: ...
def create_dword(ea, length, force=...) -> bool: ...
def create_float(ea, length, force=...) -> bool: ...
def create_oword(ea, length, force=...) -> bool: ...
def create_packed_real(ea, length, force=...) -> bool: ...
def create_qword(ea, length, force=...) -> bool: ...
def create_strlit(start, len, strtype) -> bool: ...
def create_struct(ea, length, tid, force=...) -> bool: ...
def create_tbyte(ea, length, force=...) -> bool: ...
def create_word(ea, length, force=...) -> bool: ...
def create_yword(ea, length, force=...) -> bool: ...
def create_zword(ea, length, force=...) -> bool: ...
def cust_flag() -> flags64_t: ...
def custfmt_flag() -> flags64_t: ...
def data_format_t___get_id(self) -> int: ...
def data_format_t_hotkey_get(*args, **kwargs): ...
def data_format_t_hotkey_set(self, hotkey) -> Any: ...
def data_format_t_is_present_in_menus(self) -> bool: ...
def data_format_t_menu_name_get(*args, **kwargs): ...
def data_format_t_menu_name_set(self, menu_name) -> Any: ...
def data_format_t_name_get(*args, **kwargs): ...
def data_format_t_name_set(self, name) -> Any: ...
def data_format_t_props_get(self) -> int: ...
def data_format_t_props_set(self, props) -> Any: ...
def data_format_t_swiginit(*args, **kwargs): ...
def data_format_t_swigregister(*args, **kwargs): ...
def data_format_t_text_width_get(self) -> int32: ...
def data_format_t_text_width_set(self, text_width) -> Any: ...
def data_format_t_value_size_get(self) -> asize_t: ...
def data_format_t_value_size_set(self, value_size) -> Any: ...
def data_type_t___get_id(self) -> int: ...
def data_type_t_asm_keyword_get(*args, **kwargs): ...
def data_type_t_asm_keyword_set(self, asm_keyword) -> Any: ...
def data_type_t_hotkey_get(*args, **kwargs): ...
def data_type_t_hotkey_set(self, hotkey) -> Any: ...
def data_type_t_is_present_in_menus(self) -> bool: ...
def data_type_t_menu_name_get(*args, **kwargs): ...
def data_type_t_menu_name_set(self, menu_name) -> Any: ...
def data_type_t_name_get(*args, **kwargs): ...
def data_type_t_name_set(self, name) -> Any: ...
def data_type_t_props_get(self) -> int: ...
def data_type_t_props_set(self, props) -> Any: ...
def data_type_t_swiginit(*args, **kwargs): ...
def data_type_t_swigregister(*args, **kwargs): ...
def data_type_t_value_size_get(self) -> asize_t: ...
def data_type_t_value_size_set(self, value_size) -> Any: ...
def dec_flag() -> flags64_t: ...
def del_hidden_range(ea) -> bool: ...
def del_items(ea, flags=..., nbytes=..., may_destroy=...) -> bool: ...
def del_mapping(ea) -> Any: ...
def del_value(ea) -> Any: ...
def delete_compiled_binpat_t(self) -> Any: ...
def delete_compiled_binpat_vec_t(self) -> Any: ...
def delete_data_format_t(self) -> Any: ...
def delete_data_type_t(self) -> Any: ...
def delete_hidden_range_t(self) -> Any: ...
def delete_octet_generator_t(self) -> Any: ...
def detach_custom_data_format(dtid, dfid) -> bool: ...
def disable_flags(start_ea, end_ea) -> error_t: ...
def double_flag() -> flags64_t: ...
def dword_flag() -> flags64_t: ...
def enable_flags(start_ea, end_ea, stt) -> error_t: ...
def enum_flag() -> flags64_t: ...
def equal_bytes(ea, image, mask, len, bin_search_flags) -> bool: ...
def f_has_cmt(f, arg2) -> bool: ...
def f_has_dummy_name(f, arg2) -> bool: ...
def f_has_extra_cmts(f, arg2) -> bool: ...
def f_has_name(f, arg2) -> bool: ...
def f_has_user_name(F, arg2) -> bool: ...
def f_has_xref(f, arg2) -> bool: ...
def f_is_align(F, arg2) -> bool: ...
def f_is_byte(F, arg2) -> bool: ...
def f_is_code(F, arg2) -> bool: ...
def f_is_custom(F, arg2) -> bool: ...
def f_is_data(F, arg2) -> bool: ...
def f_is_double(F, arg2) -> bool: ...
def f_is_dword(F, arg2) -> bool: ...
def f_is_float(F, arg2) -> bool: ...
def f_is_head(F, arg2) -> bool: ...
def f_is_not_tail(F, arg2) -> bool: ...
def f_is_oword(F, arg2) -> bool: ...
def f_is_pack_real(F, arg2) -> bool: ...
def f_is_qword(F, arg2) -> bool: ...
def f_is_strlit(F, arg2) -> bool: ...
def f_is_struct(F, arg2) -> bool: ...
def f_is_tail(F, arg2) -> bool: ...
def f_is_tbyte(F, arg2) -> bool: ...
def f_is_word(F, arg2) -> bool: ...
def f_is_yword(F, arg2) -> bool: ...
def find_byte(sEA, size, value, bin_search_flags) -> ea_t: ...
def find_byter(sEA, size, value, bin_search_flags) -> ea_t: ...
def find_custom_data_format(name) -> int: ...
def find_custom_data_type(name) -> int: ...
def find_free_chunk(start, size, alignment) -> ea_t: ...
def float_flag() -> flags64_t: ...
def flt_flag() -> flags64_t: ...
def free_chunk(bottom, size, step) -> ea_t: ...
def get_16bit(ea) -> uint32: ...
def get_32bit(ea) -> uint32: ...
def get_64bit(ea) -> uint64: ...
def get_8bit(*args, **kwargs): ...
def get_byte(ea) -> uchar: ...
def get_bytes(*args, **kwargs): ...
def get_bytes_and_mask(*args, **kwargs): ...
def get_cmt(ea, rptble) -> ssize_t: ...
def get_custom_data_format(dfid) -> data_format_t: ...
def get_custom_data_formats(out, dtid) -> int: ...
def get_custom_data_type(dtid) -> data_type_t: ...
def get_custom_data_types(out, min_size=..., max_size=...) -> int: ...
def get_data_elsize(ea, F, ti=...) -> asize_t: ...
def get_data_value(v, ea, size) -> bool: ...
def get_db_byte(ea) -> uchar: ...
def get_default_radix() -> int: ...
def get_dword(ea) -> uint32: ...
def get_enum_id(ea, n) -> enum_t: ...
def get_first_hidden_range() -> hidden_range_t: ...
def get_flags(ea) -> flags64_t: ...
def get_flags_by_size(size) -> flags64_t: ...
def get_flags_ex(ea, how) -> flags64_t: ...
def get_forced_operand(ea, n) -> ssize_t: ...
def get_full_data_elsize(ea, F, ti=...) -> asize_t: ...
def get_full_flags(ea) -> flags64_t: ...
def get_hidden_range(ea) -> hidden_range_t: ...
def get_hidden_range_num(ea) -> int: ...
def get_hidden_range_qty() -> int: ...
def get_item_end(ea) -> ea_t: ...
def get_item_flag(_from, n, ea, appzero) -> flags64_t: ...
def get_item_head(ea) -> ea_t: ...
def get_item_refinfo(ri, ea, n) -> bool: ...
def get_item_size(ea) -> asize_t: ...
def get_last_hidden_range() -> hidden_range_t: ...
def get_manual_insn(ea) -> ssize_t: ...
def get_mapping(n) -> bool: ...
def get_mappings_qty() -> size_t: ...
def get_max_strlit_length(ea, strtype, options=...) -> size_t: ...
def get_next_hidden_range(ea) -> hidden_range_t: ...
def get_octet(*args, **kwargs): ...
def get_octet2(ogen) -> bool: ...
def get_operand_flag(typebits, n) -> flags64_t: ...
def get_operand_type_shift(n) -> int: ...
def get_opinfo(buf, ea, n, flags) -> opinfo_t: ...
def get_optype_flags0(F) -> flags64_t: ...
def get_optype_flags1(F) -> flags64_t: ...
def get_original_byte(ea) -> uint64: ...
def get_original_dword(ea) -> uint64: ...
def get_original_qword(ea) -> uint64: ...
def get_original_word(ea) -> uint64: ...
def get_possible_item_varsize(ea, tif) -> asize_t: ...
def get_predef_insn_cmt(ins) -> ssize_t: ...
def get_prev_hidden_range(ea) -> hidden_range_t: ...
def get_qword(ea) -> uint64: ...
def get_radix(F, n) -> int: ...
def get_strlit_contents(*args, **kwargs): ...
def get_stroff_path(path, delta, ea, n) -> int: ...
def get_wide_byte(ea) -> uint64: ...
def get_wide_dword(ea) -> uint64: ...
def get_wide_word(ea) -> uint64: ...
def get_word(ea) -> ushort: ...
def get_zero_ranges(zranges, range) -> bool: ...
def getn_hidden_range(n) -> hidden_range_t: ...
def has_any_name(F) -> bool: ...
def has_auto_name(F) -> bool: ...
def has_cmt(F) -> bool: ...
def has_dummy_name(F) -> bool: ...
def has_extra_cmts(F) -> bool: ...
def has_immd(F) -> bool: ...
def has_name(F) -> bool: ...
def has_user_name(F) -> bool: ...
def has_value(F) -> bool: ...
def has_xref(F) -> bool: ...
def hex_flag() -> flags64_t: ...
def hidden_range_t_color_get(self) -> bgcolor_t: ...
def hidden_range_t_color_set(self, color) -> Any: ...
def hidden_range_t_description_get(*args, **kwargs): ...
def hidden_range_t_description_set(self, description) -> Any: ...
def hidden_range_t_footer_get(*args, **kwargs): ...
def hidden_range_t_footer_set(self, footer) -> Any: ...
def hidden_range_t_header_get(*args, **kwargs): ...
def hidden_range_t_header_set(self, header) -> Any: ...
def hidden_range_t_swiginit(*args, **kwargs): ...
def hidden_range_t_swigregister(*args, **kwargs): ...
def hidden_range_t_visible_get(self) -> bool: ...
def hidden_range_t_visible_set(self, visible) -> Any: ...
def is_align(F) -> bool: ...
def is_attached_custom_data_format(dtid, dfid) -> bool: ...
def is_bnot(ea, F, n) -> bool: ...
def is_byte(F) -> bool: ...
def is_char(F, n) -> bool: ...
def is_char0(F) -> bool: ...
def is_char1(F) -> bool: ...
def is_code(F) -> bool: ...
def is_custfmt(F, n) -> bool: ...
def is_custfmt0(F) -> bool: ...
def is_custfmt1(F) -> bool: ...
def is_custom(F) -> bool: ...
def is_data(F) -> bool: ...
def is_defarg(F, n) -> bool: ...
def is_defarg0(F) -> bool: ...
def is_defarg1(F) -> bool: ...
def is_double(F) -> bool: ...
def is_dword(F) -> bool: ...
def is_enum(F, n) -> bool: ...
def is_enum0(F) -> bool: ...
def is_enum1(F) -> bool: ...
def is_flag_for_operand(F, typebits, n) -> bool: ...
def is_float(F) -> bool: ...
def is_float0(F) -> bool: ...
def is_float1(F) -> bool: ...
def is_flow(F) -> bool: ...
def is_fltnum(F, n) -> bool: ...
def is_forced_operand(ea, n) -> bool: ...
def is_func(F) -> bool: ...
def is_head(F) -> bool: ...
def is_invsign(ea, F, n) -> bool: ...
def is_loaded(ea) -> bool: ...
def is_lzero(ea, n) -> bool: ...
def is_manual(F, n) -> bool: ...
def is_manual_insn(ea) -> bool: ...
def is_mapped(ea) -> bool: ...
def is_not_tail(F) -> bool: ...
def is_numop(F, n) -> bool: ...
def is_numop0(F) -> bool: ...
def is_numop1(F) -> bool: ...
def is_off(F, n) -> bool: ...
def is_off0(F) -> bool: ...
def is_off1(F) -> bool: ...
def is_oword(F) -> bool: ...
def is_pack_real(F) -> bool: ...
def is_qword(F) -> bool: ...
def is_same_data_type(F1, F2) -> bool: ...
def is_seg(F, n) -> bool: ...
def is_seg0(F) -> bool: ...
def is_seg1(F) -> bool: ...
def is_stkvar(F, n) -> bool: ...
def is_stkvar0(F) -> bool: ...
def is_stkvar1(F) -> bool: ...
def is_strlit(F) -> bool: ...
def is_stroff(F, n) -> bool: ...
def is_stroff0(F) -> bool: ...
def is_stroff1(F) -> bool: ...
def is_struct(F) -> bool: ...
def is_suspop(ea, F, n) -> bool: ...
def is_tail(F) -> bool: ...
def is_tbyte(F) -> bool: ...
def is_unknown(F) -> bool: ...
def is_varsize_item(ea, F, ti=..., itemsize=...) -> int: ...
def is_word(F) -> bool: ...
def is_yword(F) -> bool: ...
def is_zword(F) -> bool: ...
def leading_zero_important(ea, n) -> bool: ...
def nbits(ea) -> int: ...
def new_compiled_binpat_t() -> compiled_binpat_t: ...
def new_compiled_binpat_vec_t(x) -> compiled_binpat_vec_t: ...
def new_data_format_t(_self, name, value_size=..., menu_name=..., props=..., hotkey=..., text_width=...) -> data_format_t: ...
def new_data_type_t(_self, name, value_size=..., menu_name=..., hotkey=..., asm_keyword=..., props=...) -> data_type_t: ...
def new_hidden_range_t() -> hidden_range_t: ...
def new_octet_generator_t(_ea) -> octet_generator_t: ...
def next_addr(ea) -> ea_t: ...
def next_chunk(ea) -> ea_t: ...
def next_head(ea, maxea) -> ea_t: ...
def next_inited(ea, maxea) -> ea_t: ...
def next_not_tail(ea) -> ea_t: ...
def next_that(ea, maxea, testf) -> ea_t: ...
def next_unknown(ea, maxea) -> ea_t: ...
def next_visea(ea) -> ea_t: ...
def num_flag() -> flags64_t: ...
def oct_flag() -> flags64_t: ...
def octet_generator_t_avail_bits_get(self) -> int: ...
def octet_generator_t_avail_bits_set(self, avail_bits) -> Any: ...
def octet_generator_t_ea_get(self) -> ea_t: ...
def octet_generator_t_ea_set(self, ea) -> Any: ...
def octet_generator_t_high_byte_first_get(self) -> bool: ...
def octet_generator_t_high_byte_first_set(self, high_byte_first) -> Any: ...
def octet_generator_t_invert_byte_order(self) -> Any: ...
def octet_generator_t_swiginit(*args, **kwargs): ...
def octet_generator_t_swigregister(*args, **kwargs): ...
def octet_generator_t_value_get(self) -> uint64: ...
def octet_generator_t_value_set(self, value) -> Any: ...
def off_flag() -> flags64_t: ...
def op_adds_xrefs(F, n) -> bool: ...
def op_based_stroff(insn, n, opval, base) -> bool: ...
def op_bin(ea, n) -> bool: ...
def op_chr(ea, n) -> bool: ...
def op_custfmt(ea, n, fid) -> bool: ...
def op_dec(ea, n) -> bool: ...
def op_enum(ea, n, id, serial=...) -> bool: ...
def op_flt(ea, n) -> bool: ...
def op_hex(ea, n) -> bool: ...
def op_num(ea, n) -> bool: ...
def op_oct(ea, n) -> bool: ...
def op_seg(ea, n) -> bool: ...
def op_stkvar(ea, n) -> bool: ...
@overload
def op_stroff(insn, n, path, path_len, delta) -> bool: ...
@overload
def op_stroff(insn, n, path, delta) -> bool: ...
def oword_flag() -> flags64_t: ...
def packreal_flag() -> flags64_t: ...
def parse_binpat_str(out, ea, _in, radix, strlits_encoding=...) -> bool: ...
def patch_byte(ea, x) -> bool: ...
def patch_bytes(ea, buf) -> Any: ...
def patch_dword(ea, x) -> bool: ...
def patch_qword(ea, x) -> bool: ...
def patch_word(ea, x) -> bool: ...
def prev_addr(ea) -> ea_t: ...
def prev_chunk(ea) -> ea_t: ...
def prev_head(ea, minea) -> ea_t: ...
def prev_inited(ea, minea) -> ea_t: ...
def prev_not_tail(ea) -> ea_t: ...
def prev_that(ea, minea, testf) -> ea_t: ...
def prev_unknown(ea, minea) -> ea_t: ...
def prev_visea(ea) -> ea_t: ...
def print_strlit_type(*args, **kwargs): ...
def put_byte(ea, x) -> bool: ...
def put_bytes(ea, buf) -> Any: ...
def put_dword(ea, x) -> Any: ...
def put_qword(ea, x) -> Any: ...
def put_word(ea, x) -> Any: ...
def qword_flag() -> flags64_t: ...
def register_custom_data_format(py_df) -> int: ...
def register_custom_data_type(py_dt) -> int: ...
def revert_byte(ea) -> bool: ...
def seg_flag() -> flags64_t: ...
def set_cmt(ea, comm, rptble) -> bool: ...
def set_forced_operand(ea, n, op) -> bool: ...
def set_immd(ea) -> bool: ...
def set_lzero(ea, n) -> bool: ...
def set_manual_insn(ea, manual_insn) -> Any: ...
def set_op_type(ea, type, n) -> bool: ...
def set_opinfo(ea, n, flag, ti, suppress_events=...) -> bool: ...
def stkvar_flag() -> flags64_t: ...
def strlit_flag() -> flags64_t: ...
def stroff_flag() -> flags64_t: ...
def stru_flag() -> flags64_t: ...
def tbyte_flag() -> flags64_t: ...
def toggle_bnot(ea, n) -> bool: ...
def toggle_lzero(ea, n) -> bool: ...
def toggle_sign(ea, n) -> bool: ...
def unregister_custom_data_format(dfid) -> bool: ...
def unregister_custom_data_type(dtid) -> bool: ...
def update_hidden_range(ha) -> bool: ...
def use_mapping(ea) -> ea_t: ...
def visit_patched_bytes(ea1, ea2, py_callable) -> int: ...
def word_flag() -> flags64_t: ...
def yword_flag() -> flags64_t: ...
def zword_flag() -> flags64_t: ...
