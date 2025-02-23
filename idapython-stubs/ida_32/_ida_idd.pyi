# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

APPCALL_DEBEV: int
APPCALL_MANUAL: int
APPCALL_TIMEOUT: int
BBLK_TRACE: int
BPT_BAD_ADDR: int
BPT_BAD_ALIGN: int
BPT_BAD_LEN: int
BPT_BAD_TYPE: int
BPT_INTERNAL_ERR: int
BPT_OK: int
BPT_PAGE_OK: int
BPT_READ_ERROR: int
BPT_SKIP: int
BPT_TOO_MANY: int
BPT_WRITE_ERROR: int
BREAKPOINT: int
DBG_FLAG_ADD_ENVS: int
DBG_FLAG_ANYSIZE_HWBPT: int
DBG_FLAG_CAN_CONT_BPT: int
DBG_FLAG_CLEAN_EXIT: int
DBG_FLAG_CONNSTRING: int
DBG_FLAG_DEBTHREAD: int
DBG_FLAG_DEBUG_DLL: int
DBG_FLAG_DONT_DISTURB: int
DBG_FLAG_EXITSHOTOK: int
DBG_FLAG_FAKE_ATTACH: int
DBG_FLAG_FAKE_MEMORY: int
DBG_FLAG_FAST_STEP: int
DBG_FLAG_HWDATBPT_ONE: int
DBG_FLAG_LAZY_WATCHPTS: int
DBG_FLAG_LOWCNDS: int
DBG_FLAG_MANMEMINFO: int
DBG_FLAG_MERGE_ENVS: int
DBG_FLAG_NEEDPORT: int
DBG_FLAG_NOHOST: int
DBG_FLAG_NOPARAMETERS: int
DBG_FLAG_NOPASSWORD: int
DBG_FLAG_NOSTARTDIR: int
DBG_FLAG_PREFER_SWBPTS: int
DBG_FLAG_REMOTE: int
DBG_FLAG_SAFE: int
DBG_FLAG_SMALLBLKS: int
DBG_FLAG_TRACER_MODULE: int
DBG_FLAG_USE_SREGS: int
DBG_FLAG_VIRTHREADS: int
DBG_HAS_APPCALL: int
DBG_HAS_ATTACH_PROCESS: int
DBG_HAS_CHECK_BPT: int
DBG_HAS_DETACH_PROCESS: int
DBG_HAS_GET_PROCESSES: int
DBG_HAS_MAP_ADDRESS: int
DBG_HAS_OPEN_FILE: int
DBG_HAS_REQUEST_PAUSE: int
DBG_HAS_REXEC: int
DBG_HAS_SET_EXCEPTION_INFO: int
DBG_HAS_SET_RESUME_MODE: int
DBG_HAS_THREAD_CONTINUE: int
DBG_HAS_THREAD_GET_SREG_BASE: int
DBG_HAS_THREAD_SUSPEND: int
DBG_HAS_UPDATE_CALL_STACK: int
DBG_HIDE_WINDOW: int
DBG_NO_ASLR: int
DBG_NO_TRACE: int
DBG_PROC_32BIT: int
DBG_PROC_64BIT: int
DBG_PROC_IS_DLL: int
DBG_PROC_IS_GUI: int
DBG_RESMOD_STEP_HANDLE: int
DBG_RESMOD_STEP_INTO: int
DBG_RESMOD_STEP_OUT: int
DBG_RESMOD_STEP_OVER: int
DBG_RESMOD_STEP_SRCINTO: int
DBG_RESMOD_STEP_SRCOUT: int
DBG_RESMOD_STEP_SRCOVER: int
DBG_RESMOD_STEP_USER: int
DBG_SUSPENDED: int
DEBUGGER_ID_6811_EMULATOR: int
DEBUGGER_ID_ARM_IPHONE_USER: int
DEBUGGER_ID_ARM_LINUX_USER: int
DEBUGGER_ID_ARM_MACOS_USER: int
DEBUGGER_ID_DALVIK_USER: int
DEBUGGER_ID_GDB_USER: int
DEBUGGER_ID_TRACE_REPLAYER: int
DEBUGGER_ID_WINDBG: int
DEBUGGER_ID_X86_DOSBOX_EMULATOR: int
DEBUGGER_ID_X86_IA32_BOCHS: int
DEBUGGER_ID_X86_IA32_LINUX_USER: int
DEBUGGER_ID_X86_IA32_MACOSX_USER: int
DEBUGGER_ID_X86_IA32_WIN32_USER: int
DEBUGGER_ID_X86_PIN_TRACER: int
DEBUGGER_ID_XNU_USER: int
DEF_ADDRSIZE: int
DRC_CRC: int
DRC_ERROR: int
DRC_EVENTS: int
DRC_FAILED: int
DRC_IDBSEG: int
DRC_NETERR: int
DRC_NOCHG: int
DRC_NOFILE: int
DRC_NONE: int
DRC_NOPROC: int
DRC_OK: int
EXCEPTION: int
EXC_BREAK: int
EXC_HANDLE: int
EXC_MSG: int
EXC_SILENT: int
FUNC_TRACE: int
IDD_INTERFACE_VERSION: int
INFORMATION: int
INSN_TRACE: int
LIB_LOADED: int
LIB_UNLOADED: int
NO_EVENT: int
NO_THREAD: int
PROCESS_ATTACHED: int
PROCESS_DETACHED: int
PROCESS_EXITED: int
PROCESS_STARTED: int
PROCESS_SUSPENDED: int
REGISTER_ADDRESS: int
REGISTER_CS: int
REGISTER_CUSTFMT: int
REGISTER_FP: int
REGISTER_IP: int
REGISTER_NOLF: int
REGISTER_READONLY: int
REGISTER_SP: int
REGISTER_SS: int
RESMOD_HANDLE: int
RESMOD_INTO: int
RESMOD_MAX: int
RESMOD_NONE: int
RESMOD_OUT: int
RESMOD_OVER: int
RESMOD_SRCINTO: int
RESMOD_SRCOUT: int
RESMOD_SRCOVER: int
RESMOD_USER: int
RQ_IDAIDLE: int
RQ_IGNWERR: int
RQ_MASKING: int
RQ_NOSUSP: int
RQ_PROCEXIT: int
RQ_RESMOD: int
RQ_RESMOD_SHIFT: int
RQ_RESUME: int
RQ_SILENT: int
RQ_SUSPEND: int
RQ_SUSPRUN: int
RQ_SWSCREEN: int
RQ_VERBOSE: int
RQ__NOTHRRF: int
RVT_FLOAT: int
RVT_INT: int
RVT_UNAVAILABLE: int
STEP: int
STEP_TRACE: int
SWIG_PYTHON_LEGACY_BOOL: int
THREAD_EXITED: int
THREAD_STARTED: int
TRACE_FULL: int
cvar: Any
debugger_t_ev_appcall: int
debugger_t_ev_attach_process: int
debugger_t_ev_bin_search: int
debugger_t_ev_check_bpt: int
debugger_t_ev_cleanup_appcall: int
debugger_t_ev_close_file: int
debugger_t_ev_dbg_enable_trace: int
debugger_t_ev_detach_process: int
debugger_t_ev_eval_lowcnd: int
debugger_t_ev_exit_process: int
debugger_t_ev_get_debapp_attrs: int
debugger_t_ev_get_debmod_extensions: int
debugger_t_ev_get_debug_event: int
debugger_t_ev_get_memory_info: int
debugger_t_ev_get_processes: int
debugger_t_ev_get_srcinfo_path: int
debugger_t_ev_init_debugger: int
debugger_t_ev_is_tracing_enabled: int
debugger_t_ev_map_address: int
debugger_t_ev_open_file: int
debugger_t_ev_read_file: int
debugger_t_ev_read_memory: int
debugger_t_ev_read_registers: int
debugger_t_ev_rebase_if_required_to: int
debugger_t_ev_request_pause: int
debugger_t_ev_resume: int
debugger_t_ev_rexec: int
debugger_t_ev_send_ioctl: int
debugger_t_ev_set_exception_info: int
debugger_t_ev_set_resume_mode: int
debugger_t_ev_start_process: int
debugger_t_ev_suspended: int
debugger_t_ev_term_debugger: int
debugger_t_ev_thread_continue: int
debugger_t_ev_thread_get_sreg_base: int
debugger_t_ev_thread_suspend: int
debugger_t_ev_update_bpts: int
debugger_t_ev_update_call_stack: int
debugger_t_ev_update_lowcnds: int
debugger_t_ev_write_file: int
debugger_t_ev_write_memory: int
debugger_t_ev_write_register: int

def appcall(*args, **kwargs): ...
def bptaddr_t_hea_get(self) -> ea_t: ...
def bptaddr_t_hea_set(self, hea) -> Any: ...
def bptaddr_t_kea_get(self) -> ea_t: ...
def bptaddr_t_kea_set(self, kea) -> Any: ...
def bptaddr_t_swiginit(*args, **kwargs): ...
def bptaddr_t_swigregister(*args, **kwargs): ...
def call_stack_info_t___eq__(self, r) -> bool: ...
def call_stack_info_t___ne__(self, r) -> bool: ...
def call_stack_info_t_callea_get(self) -> ea_t: ...
def call_stack_info_t_callea_set(self, callea) -> Any: ...
def call_stack_info_t_fp_get(self) -> ea_t: ...
def call_stack_info_t_fp_set(self, fp) -> Any: ...
def call_stack_info_t_funcea_get(self) -> ea_t: ...
def call_stack_info_t_funcea_set(self, funcea) -> Any: ...
def call_stack_info_t_funcok_get(self) -> bool: ...
def call_stack_info_t_funcok_set(self, funcok) -> Any: ...
def call_stack_info_t_swiginit(*args, **kwargs): ...
def call_stack_info_t_swigregister(*args, **kwargs): ...
def call_stack_info_vec_t___eq__(self, r) -> bool: ...
def call_stack_info_vec_t___getitem__(self, i) -> call_stack_info_t: ...
def call_stack_info_vec_t___len__(self) -> size_t: ...
def call_stack_info_vec_t___ne__(self, r) -> bool: ...
def call_stack_info_vec_t___setitem__(self, i, v) -> Any: ...
def call_stack_info_vec_t__del(self, x) -> bool: ...
def call_stack_info_vec_t_add_unique(self, x) -> bool: ...
def call_stack_info_vec_t_at(self, _idx) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_begin(self) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_begin(self) -> call_stack_info_t: ...
def call_stack_info_vec_t_capacity(self) -> size_t: ...
def call_stack_info_vec_t_clear(self) -> Any: ...
def call_stack_info_vec_t_empty(self) -> bool: ...
@overload
def call_stack_info_vec_t_end(self) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_end(self) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_erase(self, it) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_erase(self, first, last) -> call_stack_info_t: ...
def call_stack_info_vec_t_extract(self) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_find(self, x) -> call_stack_info_t: ...
@overload
def call_stack_info_vec_t_find(self, x) -> call_stack_info_t: ...
def call_stack_info_vec_t_grow(self, x=...) -> Any: ...
def call_stack_info_vec_t_has(self, x) -> bool: ...
def call_stack_info_vec_t_inject(self, s, len) -> Any: ...
def call_stack_info_vec_t_insert(self, it, x) -> call_stack_info_t: ...
def call_stack_info_vec_t_pop_back(self) -> Any: ...
@overload
def call_stack_info_vec_t_push_back(self, x) -> Any: ...
@overload
def call_stack_info_vec_t_push_back(self) -> call_stack_info_t: ...
def call_stack_info_vec_t_qclear(self) -> Any: ...
def call_stack_info_vec_t_reserve(self, cnt) -> Any: ...
@overload
def call_stack_info_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def call_stack_info_vec_t_resize(self, _newsize) -> Any: ...
def call_stack_info_vec_t_size(self) -> size_t: ...
def call_stack_info_vec_t_swap(self, r) -> Any: ...
def call_stack_info_vec_t_swiginit(*args, **kwargs): ...
def call_stack_info_vec_t_swigregister(*args, **kwargs): ...
def call_stack_info_vec_t_truncate(self) -> Any: ...
def call_stack_t_swiginit(*args, **kwargs): ...
def call_stack_t_swigregister(*args, **kwargs): ...
def can_exc_continue(ev) -> bool: ...
def cleanup_appcall(tid) -> error_t: ...
def dbg_appcall(retval, func_ea, tid, ptif, argv, argnum) -> error_t: ...
def dbg_get_memory_info(*args, **kwargs): ...
def dbg_get_name(*args, **kwargs): ...
def dbg_get_registers(*args, **kwargs): ...
def dbg_get_thread_sreg_base(*args, **kwargs): ...
def dbg_read_memory(*args, **kwargs): ...
def dbg_write_memory(*args, **kwargs): ...
def debapp_attrs_t_addrsize_get(self) -> int: ...
def debapp_attrs_t_addrsize_set(self, addrsize) -> Any: ...
def debapp_attrs_t_cbsize_get(self) -> int32: ...
def debapp_attrs_t_cbsize_set(self, cbsize) -> Any: ...
def debapp_attrs_t_is_be_get(self) -> int: ...
def debapp_attrs_t_is_be_set(self, is_be) -> Any: ...
def debapp_attrs_t_platform_get(*args, **kwargs): ...
def debapp_attrs_t_platform_set(self, platform) -> Any: ...
def debapp_attrs_t_swiginit(*args, **kwargs): ...
def debapp_attrs_t_swigregister(*args, **kwargs): ...
@overload
def debug_event_t_bpt(self) -> bptaddr_t: ...
@overload
def debug_event_t_bpt(self) -> bptaddr_t: ...
def debug_event_t_bpt_ea(self) -> ea_t: ...
def debug_event_t_clear(self) -> Any: ...
def debug_event_t_clear_all(self) -> Any: ...
def debug_event_t_copy(self, r) -> debug_event_t: ...
def debug_event_t_ea_get(self) -> ea_t: ...
def debug_event_t_ea_set(self, ea) -> Any: ...
def debug_event_t_eid(self) -> event_id_t: ...
@overload
def debug_event_t_exc(self) -> excinfo_t: ...
@overload
def debug_event_t_exc(self) -> excinfo_t: ...
def debug_event_t_exit_code(*args, **kwargs): ...
def debug_event_t_handled_get(self) -> bool: ...
def debug_event_t_handled_set(self, handled) -> Any: ...
def debug_event_t_info(self) -> qstring: ...
@overload
def debug_event_t_modinfo(self) -> modinfo_t: ...
@overload
def debug_event_t_modinfo(self) -> modinfo_t: ...
def debug_event_t_pid_get(self) -> pid_t: ...
def debug_event_t_pid_set(self, pid) -> Any: ...
def debug_event_t_set_bpt(self) -> bptaddr_t: ...
def debug_event_t_set_eid(self, id) -> Any: ...
def debug_event_t_set_exception(self) -> excinfo_t: ...
def debug_event_t_set_exit_code(self, id, code) -> Any: ...
def debug_event_t_set_info(*args, **kwargs): ...
def debug_event_t_set_modinfo(self, id) -> modinfo_t: ...
def debug_event_t_swiginit(*args, **kwargs): ...
def debug_event_t_swigregister(*args, **kwargs): ...
def debug_event_t_tid_get(self) -> thid_t: ...
def debug_event_t_tid_set(self, tid) -> Any: ...
def debugger_t___get_bpt_bytes(self) -> bytevec_t: ...
def debugger_t___get_nregs(self) -> int: ...
def debugger_t___get_regclasses(*args, **kwargs): ...
def debugger_t___get_registers(self) -> dyn_register_info_array: ...
def debugger_t_attach_process(self, pid, event_id, dbg_proc_flags) -> drc_t: ...
def debugger_t_bin_search(self, start_ea, end_ea, data, srch_flags) -> drc_t: ...
def debugger_t_bpt_size_get(self) -> uchar: ...
def debugger_t_bpt_size_set(self, bpt_size) -> Any: ...
def debugger_t_cache_block_size(self) -> size_t: ...
def debugger_t_can_continue_from_bpt(self) -> bool: ...
def debugger_t_can_debug_standalone_dlls(self) -> bool: ...
def debugger_t_check_bpt(self, bptvc, type, ea, len) -> drc_t: ...
def debugger_t_cleanup_appcall(self, tid) -> drc_t: ...
def debugger_t_close_file(self, fn) -> Any: ...
def debugger_t_dbg_enable_trace(self, tid, enable, trace_flags) -> bool: ...
def debugger_t_default_regclasses_get(self) -> int: ...
def debugger_t_default_regclasses_set(self, default_regclasses) -> Any: ...
def debugger_t_detach_process(self) -> drc_t: ...
def debugger_t_eval_lowcnd(self, tid, ea) -> drc_t: ...
def debugger_t_exit_process(self) -> drc_t: ...
def debugger_t_fake_memory(self) -> bool: ...
def debugger_t_filetype_get(self) -> uchar: ...
def debugger_t_filetype_set(self, filetype) -> Any: ...
def debugger_t_flags2_get(self) -> uint32: ...
def debugger_t_flags2_set(self, flags2) -> Any: ...
def debugger_t_flags_get(self) -> uint32: ...
def debugger_t_flags_set(self, flags) -> Any: ...
def debugger_t_get_debapp_attrs(self, out_pattrs) -> bool: ...
def debugger_t_get_debmod_extensions(*args, **kwargs): ...
def debugger_t_get_debug_event(self, event, timeout_ms) -> gdecode_t: ...
def debugger_t_get_memory_info(self, ranges) -> drc_t: ...
def debugger_t_get_processes(self, procs) -> drc_t: ...
def debugger_t_get_srcinfo_path(self, path, base) -> bool: ...
def debugger_t_has_appcall(self) -> bool: ...
def debugger_t_has_attach_process(self) -> bool: ...
def debugger_t_has_check_bpt(self) -> bool: ...
def debugger_t_has_detach_process(self) -> bool: ...
def debugger_t_has_get_processes(self) -> bool: ...
def debugger_t_has_map_address(self) -> bool: ...
def debugger_t_has_open_file(self) -> bool: ...
def debugger_t_has_request_pause(self) -> bool: ...
def debugger_t_has_rexec(self) -> bool: ...
def debugger_t_has_set_exception_info(self) -> bool: ...
def debugger_t_has_set_resume_mode(self) -> bool: ...
def debugger_t_has_soft_bpt(self) -> bool: ...
def debugger_t_has_thread_continue(self) -> bool: ...
def debugger_t_has_thread_get_sreg_base(self) -> bool: ...
def debugger_t_has_thread_suspend(self) -> bool: ...
def debugger_t_has_update_call_stack(self) -> bool: ...
def debugger_t_id_get(self) -> int: ...
def debugger_t_id_set(self, id) -> Any: ...
def debugger_t_init_debugger(self, hostname, portnum, password) -> bool: ...
def debugger_t_is_remote(self) -> bool: ...
def debugger_t_is_resmod_avail(self, resmod) -> bool: ...
def debugger_t_is_safe(self) -> bool: ...
def debugger_t_is_tracing_enabled(self, tid, tracebit) -> bool: ...
def debugger_t_map_address(self, off, regs, regnum) -> ea_t: ...
def debugger_t_may_disturb(self) -> bool: ...
def debugger_t_may_take_exit_snapshot(self) -> bool: ...
def debugger_t_memory_page_size_get(self) -> int: ...
def debugger_t_memory_page_size_set(self, memory_page_size) -> Any: ...
def debugger_t_must_have_hostname(self) -> bool: ...
def debugger_t_name_get(*args, **kwargs): ...
def debugger_t_name_set(self, name) -> Any: ...
def debugger_t_open_file(self, file, fsize, readonly) -> int: ...
def debugger_t_processor_get(*args, **kwargs): ...
def debugger_t_processor_set(self, processor) -> Any: ...
def debugger_t_read_file(self, fn, off, buf, size) -> ssize_t: ...
def debugger_t_read_memory(self, nbytes, ea, buffer, size) -> drc_t: ...
def debugger_t_read_registers(self, tid, clsmask, values) -> drc_t: ...
def debugger_t_rebase_if_required_to(self, new_base) -> Any: ...
def debugger_t_regs(self, idx) -> register_info_t: ...
def debugger_t_request_pause(self) -> drc_t: ...
def debugger_t_resume(self, event) -> drc_t: ...
def debugger_t_resume_modes_get(self) -> ushort: ...
def debugger_t_resume_modes_set(self, resume_modes) -> Any: ...
def debugger_t_rexec(self, cmdline) -> int: ...
def debugger_t_send_ioctl(self, fn, buf, poutbuf, poutsize) -> drc_t: ...
def debugger_t_set_exception_info(self, info, qty) -> Any: ...
def debugger_t_set_resume_mode(self, tid, resmod) -> drc_t: ...
def debugger_t_start_process(self, path, args, envs, startdir, dbg_proc_flags, input_path, input_file_crc32) -> drc_t: ...
def debugger_t_supports_debthread(self) -> bool: ...
def debugger_t_supports_lowcnds(self) -> bool: ...
def debugger_t_suspended(self, dlls_added, thr_names=...) -> Any: ...
def debugger_t_swiginit(*args, **kwargs): ...
def debugger_t_swigregister(*args, **kwargs): ...
def debugger_t_term_debugger(self) -> bool: ...
def debugger_t_thread_continue(self, tid) -> drc_t: ...
def debugger_t_thread_get_sreg_base(self, answer, tid, sreg_value) -> drc_t: ...
def debugger_t_thread_suspend(self, tid) -> drc_t: ...
def debugger_t_update_bpts(self, nbpts, bpts, nadd, ndel) -> drc_t: ...
def debugger_t_update_call_stack(self, tid, trace) -> drc_t: ...
def debugger_t_update_lowcnds(self, nupdated, lowcnds, nlowcnds) -> drc_t: ...
def debugger_t_use_memregs(self) -> bool: ...
def debugger_t_use_sregs(self) -> bool: ...
def debugger_t_version_get(self) -> int: ...
def debugger_t_version_set(self, version) -> Any: ...
def debugger_t_virtual_threads(self) -> bool: ...
def debugger_t_write_file(self, fn, off, buf) -> ssize_t: ...
def debugger_t_write_memory(self, nbytes, ea, buffer, size) -> drc_t: ...
def debugger_t_write_register(self, tid, regidx, value) -> drc_t: ...
def delete_bptaddr_t(self) -> Any: ...
def delete_call_stack_info_t(self) -> Any: ...
def delete_call_stack_info_vec_t(self) -> Any: ...
def delete_call_stack_t(self) -> Any: ...
def delete_debapp_attrs_t(self) -> Any: ...
def delete_debug_event_t(self) -> Any: ...
def delete_debugger_t(self) -> Any: ...
def delete_dyn_register_info_array(self) -> Any: ...
def delete_exception_info_t(self) -> Any: ...
def delete_excinfo_t(self) -> Any: ...
def delete_excvec_t(self) -> Any: ...
def delete_launch_env_t(self) -> Any: ...
def delete_meminfo_vec_t(self) -> Any: ...
def delete_meminfo_vec_template_t(self) -> Any: ...
def delete_memory_info_t(self) -> Any: ...
def delete_modinfo_t(self) -> Any: ...
def delete_process_info_t(self) -> Any: ...
def delete_procinfo_vec_t(self) -> Any: ...
def delete_register_info_t(self) -> Any: ...
def delete_regval_t(self) -> Any: ...
def delete_regvals_t(self) -> Any: ...
def delete_scattered_segm_t(self) -> Any: ...
def delete_thread_name_t(self) -> Any: ...
def dyn_register_info_array___getitem__(self, i) -> register_info_t: ...
def dyn_register_info_array___len__(self) -> size_t: ...
def dyn_register_info_array___setitem__(self, i, v) -> Any: ...
def dyn_register_info_array_count_get(self) -> size_t: ...
def dyn_register_info_array_data_get(self) -> register_info_t: ...
def dyn_register_info_array_swiginit(*args, **kwargs): ...
def dyn_register_info_array_swigregister(*args, **kwargs): ...
def exception_info_t_break_on(self) -> bool: ...
def exception_info_t_code_get(self) -> uint: ...
def exception_info_t_code_set(self, code) -> Any: ...
def exception_info_t_desc_get(*args, **kwargs): ...
def exception_info_t_desc_set(self, desc) -> Any: ...
def exception_info_t_flags_get(self) -> uint32: ...
def exception_info_t_flags_set(self, flags) -> Any: ...
def exception_info_t_handle(self) -> bool: ...
def exception_info_t_name_get(*args, **kwargs): ...
def exception_info_t_name_set(self, name) -> Any: ...
def exception_info_t_swiginit(*args, **kwargs): ...
def exception_info_t_swigregister(*args, **kwargs): ...
def excinfo_t_can_cont_get(self) -> bool: ...
def excinfo_t_can_cont_set(self, can_cont) -> Any: ...
def excinfo_t_code_get(self) -> uint32: ...
def excinfo_t_code_set(self, code) -> Any: ...
def excinfo_t_ea_get(self) -> ea_t: ...
def excinfo_t_ea_set(self, ea) -> Any: ...
def excinfo_t_info_get(*args, **kwargs): ...
def excinfo_t_info_set(self, info) -> Any: ...
def excinfo_t_swiginit(*args, **kwargs): ...
def excinfo_t_swigregister(*args, **kwargs): ...
def excvec_t___getitem__(self, i) -> exception_info_t: ...
def excvec_t___len__(self) -> size_t: ...
def excvec_t___setitem__(self, i, v) -> Any: ...
def excvec_t_at(self, _idx) -> exception_info_t: ...
@overload
def excvec_t_begin(self) -> exception_info_t: ...
@overload
def excvec_t_begin(self) -> exception_info_t: ...
def excvec_t_capacity(self) -> size_t: ...
def excvec_t_clear(self) -> Any: ...
def excvec_t_empty(self) -> bool: ...
@overload
def excvec_t_end(self) -> exception_info_t: ...
@overload
def excvec_t_end(self) -> exception_info_t: ...
@overload
def excvec_t_erase(self, it) -> exception_info_t: ...
@overload
def excvec_t_erase(self, first, last) -> exception_info_t: ...
def excvec_t_extract(self) -> exception_info_t: ...
def excvec_t_grow(self, x=...) -> Any: ...
def excvec_t_inject(self, s, len) -> Any: ...
def excvec_t_insert(self, it, x) -> exception_info_t: ...
def excvec_t_pop_back(self) -> Any: ...
@overload
def excvec_t_push_back(self, x) -> Any: ...
@overload
def excvec_t_push_back(self) -> exception_info_t: ...
def excvec_t_qclear(self) -> Any: ...
def excvec_t_reserve(self, cnt) -> Any: ...
@overload
def excvec_t_resize(self, _newsize, x) -> Any: ...
@overload
def excvec_t_resize(self, _newsize) -> Any: ...
def excvec_t_size(self) -> size_t: ...
def excvec_t_swap(self, r) -> Any: ...
def excvec_t_swiginit(*args, **kwargs): ...
def excvec_t_swigregister(*args, **kwargs): ...
def excvec_t_truncate(self) -> Any: ...
def get_dbg() -> debugger_t: ...
def get_event_bpt_hea(ev) -> ea_t: ...
def get_event_exc_code(ev) -> uint: ...
def get_event_exc_ea(ev) -> ea_t: ...
def get_event_exc_info(ev) -> char: ...
def get_event_info(ev) -> char: ...
def get_event_module_base(ev) -> ea_t: ...
def get_event_module_name(ev) -> char: ...
def get_event_module_size(ev) -> asize_t: ...
def launch_env_t_merge_get(self) -> bool: ...
def launch_env_t_merge_set(self, merge) -> Any: ...
def launch_env_t_swiginit(*args, **kwargs): ...
def launch_env_t_swigregister(*args, **kwargs): ...
def meminfo_vec_t_swiginit(*args, **kwargs): ...
def meminfo_vec_t_swigregister(*args, **kwargs): ...
def meminfo_vec_template_t___eq__(self, r) -> bool: ...
def meminfo_vec_template_t___getitem__(self, i) -> memory_info_t: ...
def meminfo_vec_template_t___len__(self) -> size_t: ...
def meminfo_vec_template_t___ne__(self, r) -> bool: ...
def meminfo_vec_template_t___setitem__(self, i, v) -> Any: ...
def meminfo_vec_template_t__del(self, x) -> bool: ...
def meminfo_vec_template_t_add_unique(self, x) -> bool: ...
def meminfo_vec_template_t_at(self, _idx) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_begin(self) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_begin(self) -> memory_info_t: ...
def meminfo_vec_template_t_capacity(self) -> size_t: ...
def meminfo_vec_template_t_clear(self) -> Any: ...
def meminfo_vec_template_t_empty(self) -> bool: ...
@overload
def meminfo_vec_template_t_end(self) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_end(self) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_erase(self, it) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_erase(self, first, last) -> memory_info_t: ...
def meminfo_vec_template_t_extract(self) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_find(self, x) -> memory_info_t: ...
@overload
def meminfo_vec_template_t_find(self, x) -> memory_info_t: ...
def meminfo_vec_template_t_grow(self, x=...) -> Any: ...
def meminfo_vec_template_t_has(self, x) -> bool: ...
def meminfo_vec_template_t_inject(self, s, len) -> Any: ...
def meminfo_vec_template_t_insert(self, it, x) -> memory_info_t: ...
def meminfo_vec_template_t_pop_back(self) -> Any: ...
@overload
def meminfo_vec_template_t_push_back(self, x) -> Any: ...
@overload
def meminfo_vec_template_t_push_back(self) -> memory_info_t: ...
def meminfo_vec_template_t_qclear(self) -> Any: ...
def meminfo_vec_template_t_reserve(self, cnt) -> Any: ...
@overload
def meminfo_vec_template_t_resize(self, _newsize, x) -> Any: ...
@overload
def meminfo_vec_template_t_resize(self, _newsize) -> Any: ...
def meminfo_vec_template_t_size(self) -> size_t: ...
def meminfo_vec_template_t_swap(self, r) -> Any: ...
def meminfo_vec_template_t_swiginit(*args, **kwargs): ...
def meminfo_vec_template_t_swigregister(*args, **kwargs): ...
def meminfo_vec_template_t_truncate(self) -> Any: ...
def memory_info_t___eq__(self, r) -> bool: ...
def memory_info_t___ne__(self, r) -> bool: ...
def memory_info_t_bitness_get(self) -> uchar: ...
def memory_info_t_bitness_set(self, bitness) -> Any: ...
def memory_info_t_name_get(*args, **kwargs): ...
def memory_info_t_name_set(self, name) -> Any: ...
def memory_info_t_perm_get(self) -> uchar: ...
def memory_info_t_perm_set(self, perm) -> Any: ...
def memory_info_t_sbase_get(self) -> ea_t: ...
def memory_info_t_sbase_set(self, sbase) -> Any: ...
def memory_info_t_sclass_get(*args, **kwargs): ...
def memory_info_t_sclass_set(self, sclass) -> Any: ...
def memory_info_t_swiginit(*args, **kwargs): ...
def memory_info_t_swigregister(*args, **kwargs): ...
def modinfo_t_base_get(self) -> ea_t: ...
def modinfo_t_base_set(self, base) -> Any: ...
def modinfo_t_name_get(*args, **kwargs): ...
def modinfo_t_name_set(self, name) -> Any: ...
def modinfo_t_rebase_to_get(self) -> ea_t: ...
def modinfo_t_rebase_to_set(self, rebase_to) -> Any: ...
def modinfo_t_size_get(self) -> asize_t: ...
def modinfo_t_size_set(self, size) -> Any: ...
def modinfo_t_swiginit(*args, **kwargs): ...
def modinfo_t_swigregister(*args, **kwargs): ...
def new_bptaddr_t() -> bptaddr_t: ...
def new_call_stack_info_t() -> call_stack_info_t: ...
def new_call_stack_info_vec_t(x) -> call_stack_info_vec_t: ...
def new_call_stack_t() -> call_stack_t: ...
def new_debapp_attrs_t() -> debapp_attrs_t: ...
def new_debug_event_t(r) -> debug_event_t: ...
def new_debugger_t() -> debugger_t: ...
def new_dyn_register_info_array(_data, _count) -> dyn_register_info_array: ...
def new_exception_info_t(_code, _flags, _name, _desc) -> exception_info_t: ...
def new_excinfo_t() -> excinfo_t: ...
def new_excvec_t(x) -> excvec_t: ...
def new_launch_env_t() -> launch_env_t: ...
def new_meminfo_vec_t() -> meminfo_vec_t: ...
def new_meminfo_vec_template_t(x) -> meminfo_vec_template_t: ...
def new_memory_info_t() -> memory_info_t: ...
def new_modinfo_t() -> modinfo_t: ...
def new_process_info_t() -> process_info_t: ...
def new_procinfo_vec_t(x) -> procinfo_vec_t: ...
def new_register_info_t() -> register_info_t: ...
def new_regval_t(r) -> regval_t: ...
def new_regvals_t(x) -> regvals_t: ...
def new_scattered_segm_t() -> scattered_segm_t: ...
def new_thread_name_t() -> thread_name_t: ...
def process_info_t_name_get(*args, **kwargs): ...
def process_info_t_name_set(self, name) -> Any: ...
def process_info_t_pid_get(self) -> pid_t: ...
def process_info_t_pid_set(self, pid) -> Any: ...
def process_info_t_swiginit(*args, **kwargs): ...
def process_info_t_swigregister(*args, **kwargs): ...
def procinfo_vec_t___getitem__(self, i) -> process_info_t: ...
def procinfo_vec_t___len__(self) -> size_t: ...
def procinfo_vec_t___setitem__(self, i, v) -> Any: ...
def procinfo_vec_t_at(self, _idx) -> process_info_t: ...
@overload
def procinfo_vec_t_begin(self) -> process_info_t: ...
@overload
def procinfo_vec_t_begin(self) -> process_info_t: ...
def procinfo_vec_t_capacity(self) -> size_t: ...
def procinfo_vec_t_clear(self) -> Any: ...
def procinfo_vec_t_empty(self) -> bool: ...
@overload
def procinfo_vec_t_end(self) -> process_info_t: ...
@overload
def procinfo_vec_t_end(self) -> process_info_t: ...
@overload
def procinfo_vec_t_erase(self, it) -> process_info_t: ...
@overload
def procinfo_vec_t_erase(self, first, last) -> process_info_t: ...
def procinfo_vec_t_extract(self) -> process_info_t: ...
def procinfo_vec_t_grow(self, x=...) -> Any: ...
def procinfo_vec_t_inject(self, s, len) -> Any: ...
def procinfo_vec_t_insert(self, it, x) -> process_info_t: ...
def procinfo_vec_t_pop_back(self) -> Any: ...
@overload
def procinfo_vec_t_push_back(self, x) -> Any: ...
@overload
def procinfo_vec_t_push_back(self) -> process_info_t: ...
def procinfo_vec_t_qclear(self) -> Any: ...
def procinfo_vec_t_reserve(self, cnt) -> Any: ...
@overload
def procinfo_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def procinfo_vec_t_resize(self, _newsize) -> Any: ...
def procinfo_vec_t_size(self) -> size_t: ...
def procinfo_vec_t_swap(self, r) -> Any: ...
def procinfo_vec_t_swiginit(*args, **kwargs): ...
def procinfo_vec_t_swigregister(*args, **kwargs): ...
def procinfo_vec_t_truncate(self) -> Any: ...
def register_info_t___get_bit_strings(*args, **kwargs): ...
def register_info_t_default_bit_strings_mask_get(self) -> uval_t: ...
def register_info_t_default_bit_strings_mask_set(self, default_bit_strings_mask) -> Any: ...
def register_info_t_dtype_get(self) -> op_dtype_t: ...
def register_info_t_dtype_set(self, dtype) -> Any: ...
def register_info_t_flags_get(self) -> uint32: ...
def register_info_t_flags_set(self, flags) -> Any: ...
def register_info_t_name_get(*args, **kwargs): ...
def register_info_t_name_set(self, name) -> Any: ...
def register_info_t_register_class_get(self) -> register_class_t: ...
def register_info_t_register_class_set(self, register_class) -> Any: ...
def register_info_t_swiginit(*args, **kwargs): ...
def register_info_t_swigregister(*args, **kwargs): ...
def regval_t___eq__(self, r) -> bool: ...
def regval_t___ne__(self, r) -> bool: ...
def regval_t_bytes(self) -> bytevec_t: ...
def regval_t_clear(self) -> Any: ...
def regval_t_fval_get(self) -> fpvalue_t: ...
def regval_t_fval_set(self, fval) -> Any: ...
def regval_t_get_data(self) -> Any: ...
def regval_t_get_data_size(self) -> size_t: ...
def regval_t_ival_get(self) -> uint64: ...
def regval_t_ival_set(self, ival) -> Any: ...
def regval_t_pyval(*args, **kwargs): ...
def regval_t_rvtype_get(self) -> int32: ...
def regval_t_rvtype_set(self, rvtype) -> Any: ...
@overload
def regval_t_set_bytes(self, data, size) -> Any: ...
@overload
def regval_t_set_bytes(self, v) -> Any: ...
def regval_t_set_float(self, x) -> Any: ...
def regval_t_set_int(self, x) -> Any: ...
def regval_t_set_pyval(self, o, dtype) -> bool: ...
def regval_t_set_unavailable(self) -> Any: ...
def regval_t_swap(self, r) -> Any: ...
def regval_t_swiginit(*args, **kwargs): ...
def regval_t_swigregister(*args, **kwargs): ...
def regvals_t___eq__(self, r) -> bool: ...
def regvals_t___getitem__(self, i) -> regval_t: ...
def regvals_t___len__(self) -> size_t: ...
def regvals_t___ne__(self, r) -> bool: ...
def regvals_t___setitem__(self, i, v) -> Any: ...
def regvals_t__del(self, x) -> bool: ...
def regvals_t_add_unique(self, x) -> bool: ...
def regvals_t_at(self, _idx) -> regval_t: ...
@overload
def regvals_t_begin(self) -> regval_t: ...
@overload
def regvals_t_begin(self) -> regval_t: ...
def regvals_t_capacity(self) -> size_t: ...
def regvals_t_clear(self) -> Any: ...
def regvals_t_empty(self) -> bool: ...
@overload
def regvals_t_end(self) -> regval_t: ...
@overload
def regvals_t_end(self) -> regval_t: ...
@overload
def regvals_t_erase(self, it) -> regval_t: ...
@overload
def regvals_t_erase(self, first, last) -> regval_t: ...
def regvals_t_extract(self) -> regval_t: ...
@overload
def regvals_t_find(self, x) -> regval_t: ...
@overload
def regvals_t_find(self, x) -> regval_t: ...
def regvals_t_grow(self, x=...) -> Any: ...
def regvals_t_has(self, x) -> bool: ...
def regvals_t_inject(self, s, len) -> Any: ...
def regvals_t_insert(self, it, x) -> regval_t: ...
def regvals_t_pop_back(self) -> Any: ...
@overload
def regvals_t_push_back(self, x) -> Any: ...
@overload
def regvals_t_push_back(self) -> regval_t: ...
def regvals_t_qclear(self) -> Any: ...
def regvals_t_reserve(self, cnt) -> Any: ...
@overload
def regvals_t_resize(self, _newsize, x) -> Any: ...
@overload
def regvals_t_resize(self, _newsize) -> Any: ...
def regvals_t_size(self) -> size_t: ...
def regvals_t_swap(self, r) -> Any: ...
def regvals_t_swiginit(*args, **kwargs): ...
def regvals_t_swigregister(*args, **kwargs): ...
def regvals_t_truncate(self) -> Any: ...
def scattered_segm_t_name_get(*args, **kwargs): ...
def scattered_segm_t_name_set(self, name) -> Any: ...
def scattered_segm_t_swiginit(*args, **kwargs): ...
def scattered_segm_t_swigregister(*args, **kwargs): ...
def set_debug_event_code(ev, id) -> Any: ...
def thread_name_t_name_get(*args, **kwargs): ...
def thread_name_t_name_set(self, name) -> Any: ...
def thread_name_t_swiginit(*args, **kwargs): ...
def thread_name_t_swigregister(*args, **kwargs): ...
def thread_name_t_tid_get(self) -> thid_t: ...
def thread_name_t_tid_set(self, tid) -> Any: ...
