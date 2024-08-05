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

class excvec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'exception_info_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'exception_info_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'exception_info_t *': ...
    def inject(self, *args) -> None: ...
    def begin(self, *args) -> 'qvector< exception_info_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< exception_info_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< exception_info_t >::iterator': ...
    def erase(self, *args) -> 'qvector< exception_info_t >::iterator': ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'exception_info_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class procinfo_vec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'process_info_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'process_info_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'process_info_t *': ...
    def inject(self, *args) -> None: ...
    def begin(self, *args) -> 'qvector< process_info_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< process_info_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< process_info_t >::iterator': ...
    def erase(self, *args) -> 'qvector< process_info_t >::iterator': ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'process_info_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class call_stack_info_vec_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'call_stack_info_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'call_stack_info_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'call_stack_info_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< call_stack_info_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< call_stack_info_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< call_stack_info_t >::iterator': ...
    def erase(self, *args) -> 'qvector< call_stack_info_t >::iterator': ...
    def find(self, *args) -> 'qvector< call_stack_info_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'call_stack_info_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class meminfo_vec_template_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'memory_info_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'memory_info_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'memory_info_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< memory_info_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< memory_info_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< memory_info_t >::iterator': ...
    def erase(self, *args) -> 'qvector< memory_info_t >::iterator': ...
    def find(self, *args) -> 'qvector< memory_info_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'memory_info_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

class regvals_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def push_back(self, *args) -> 'regval_t &': ...
    def pop_back(self, *args) -> None: ...
    def size(self, *args) -> size_t: ...
    def empty(self, *args) -> bool: ...
    def at(self, *args) -> 'regval_t const &': ...
    def qclear(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def resize(self, *args) -> None: ...
    def grow(self, *args) -> None: ...
    def capacity(self, *args) -> size_t: ...
    def reserve(self, *args) -> None: ...
    def truncate(self, *args) -> None: ...
    def swap(self, *args) -> None: ...
    def extract(self, *args) -> 'regval_t *': ...
    def inject(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def begin(self, *args) -> 'qvector< regval_t >::const_iterator': ...
    def end(self, *args) -> 'qvector< regval_t >::const_iterator': ...
    def insert(self, *args) -> 'qvector< regval_t >::iterator': ...
    def erase(self, *args) -> 'qvector< regval_t >::iterator': ...
    def find(self, *args) -> 'qvector< regval_t >::const_iterator': ...
    def has(self, *args) -> bool: ...
    def add_unique(self, *args) -> bool: ...
    def _del(self, *args) -> bool: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'regval_t const &': ...
    def __setitem__(self, *args) -> None: ...
    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator

IDD_INTERFACE_VERSION: Incomplete
NO_THREAD: Incomplete

class process_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    pid: Incomplete
    name: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class debapp_attrs_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    cbsize: Incomplete
    addrsize: Incomplete
    platform: Incomplete
    is_be: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

DEF_ADDRSIZE: Incomplete

class register_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    name: Incomplete
    flags: Incomplete
    register_class: Incomplete
    dtype: Incomplete
    default_bit_strings_mask: Incomplete
    def __get_bit_strings(self, *args) -> 'PyObject *': ...
    bit_strings: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

REGISTER_READONLY: Incomplete
REGISTER_IP: Incomplete
REGISTER_SP: Incomplete
REGISTER_FP: Incomplete
REGISTER_ADDRESS: Incomplete
REGISTER_CS: Incomplete
REGISTER_SS: Incomplete
REGISTER_NOLF: Incomplete
REGISTER_CUSTFMT: Incomplete

class memory_info_t(ida_range.range_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    name: Incomplete
    sclass: Incomplete
    sbase: Incomplete
    bitness: Incomplete
    perm: Incomplete
    def __init__(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    __swig_destroy__: Incomplete

class meminfo_vec_t(meminfo_vec_template_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class scattered_segm_t(ida_range.range_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    name: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class launch_env_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    merge: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

NO_EVENT: Incomplete
PROCESS_STARTED: Incomplete
PROCESS_EXITED: Incomplete
THREAD_STARTED: Incomplete
THREAD_EXITED: Incomplete
BREAKPOINT: Incomplete
STEP: Incomplete
EXCEPTION: Incomplete
LIB_LOADED: Incomplete
LIB_UNLOADED: Incomplete
INFORMATION: Incomplete
PROCESS_ATTACHED: Incomplete
PROCESS_DETACHED: Incomplete
PROCESS_SUSPENDED: Incomplete
TRACE_FULL: Incomplete

def set_debug_event_code(*args) -> None: ...

class modinfo_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    name: Incomplete
    base: Incomplete
    size: Incomplete
    rebase_to: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class bptaddr_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    hea: Incomplete
    kea: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class excinfo_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    code: Incomplete
    can_cont: Incomplete
    ea: Incomplete
    info: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class debug_event_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    pid: Incomplete
    tid: Incomplete
    ea: Incomplete
    handled: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete
    def copy(self, *args) -> 'debug_event_t &': ...
    def clear(self, *args) -> None: ...
    def clear_all(self, *args) -> None: ...
    def eid(self, *args) -> event_id_t: ...
    def set_eid(self, *args) -> None: ...
    def modinfo(self, *args) -> 'modinfo_t const &': ...
    def exit_code(self, *args) -> 'int const &': ...
    def info(self, *args) -> 'qstring const &': ...
    def bpt(self, *args) -> 'bptaddr_t const &': ...
    def exc(self, *args) -> 'excinfo_t const &': ...
    def set_modinfo(self, *args) -> 'modinfo_t &': ...
    def set_exit_code(self, *args) -> None: ...
    def set_info(self, *args) -> 'qstring &': ...
    def set_bpt(self, *args) -> 'bptaddr_t &': ...
    def set_exception(self, *args) -> 'excinfo_t &': ...
    def bpt_ea(self, *args) -> ea_t: ...

class exception_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    code: Incomplete
    flags: Incomplete
    def break_on(self, *args) -> bool: ...
    def handle(self, *args) -> bool: ...
    name: Incomplete
    desc: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

cvar: Incomplete
BPT_WRITE: Incomplete
BPT_READ: Incomplete
BPT_RDWR: Incomplete
BPT_SOFT: Incomplete
BPT_EXEC: Incomplete
BPT_DEFAULT: Incomplete
EXC_BREAK: Incomplete
EXC_HANDLE: Incomplete
EXC_MSG: Incomplete
EXC_SILENT: Incomplete

class regval_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    rvtype: Incomplete
    ival: Incomplete
    fval: Incomplete
    __swig_destroy__: Incomplete
    def __init__(self, *args) -> None: ...
    def clear(self, *args) -> None: ...
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def swap(self, *args) -> None: ...
    def set_int(self, *args) -> None: ...
    def set_float(self, *args) -> None: ...
    def set_bytes(self, *args) -> 'bytevec_t &': ...
    def set_unavailable(self, *args) -> None: ...
    def bytes(self, *args) -> 'bytevec_t const &': ...
    def get_data(self, *args) -> 'void const *': ...
    def get_data_size(self, *args) -> size_t: ...
    def set_pyval(self, *args) -> bool: ...
    def pyval(self, *args) -> 'PyObject *': ...

RVT_INT: Incomplete
RVT_FLOAT: Incomplete
RVT_UNAVAILABLE: Incomplete

class call_stack_info_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    callea: Incomplete
    funcea: Incomplete
    fp: Incomplete
    funcok: Incomplete
    def __eq__(self, *args) -> bool: ...
    def __ne__(self, *args) -> bool: ...
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

class call_stack_t(call_stack_info_vec_t):
    thisown: Incomplete
    __repr__ = _swig_repr
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

def dbg_appcall(*args) -> error_t: ...
def cleanup_appcall(*args) -> error_t: ...

class thread_name_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    tid: Incomplete
    name: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

RESMOD_NONE: Incomplete
RESMOD_INTO: Incomplete
RESMOD_OVER: Incomplete
RESMOD_OUT: Incomplete
RESMOD_SRCINTO: Incomplete
RESMOD_SRCOVER: Incomplete
RESMOD_SRCOUT: Incomplete
RESMOD_USER: Incomplete
RESMOD_HANDLE: Incomplete
RESMOD_MAX: Incomplete
STEP_TRACE: Incomplete
INSN_TRACE: Incomplete
FUNC_TRACE: Incomplete
BBLK_TRACE: Incomplete
DRC_EVENTS: Incomplete
DRC_CRC: Incomplete
DRC_OK: Incomplete
DRC_NONE: Incomplete
DRC_FAILED: Incomplete
DRC_NETERR: Incomplete
DRC_NOFILE: Incomplete
DRC_IDBSEG: Incomplete
DRC_NOPROC: Incomplete
DRC_NOCHG: Incomplete
DRC_ERROR: Incomplete

class debugger_t:
    thisown: Incomplete
    __repr__ = _swig_repr
    version: Incomplete
    name: Incomplete
    id: Incomplete
    processor: Incomplete
    flags: Incomplete
    flags2: Incomplete
    def is_remote(self, *args) -> bool: ...
    def must_have_hostname(self, *args) -> bool: ...
    def can_continue_from_bpt(self, *args) -> bool: ...
    def may_disturb(self, *args) -> bool: ...
    def is_safe(self, *args) -> bool: ...
    def use_sregs(self, *args) -> bool: ...
    def cache_block_size(self, *args) -> size_t: ...
    def use_memregs(self, *args) -> bool: ...
    def may_take_exit_snapshot(self, *args) -> bool: ...
    def virtual_threads(self, *args) -> bool: ...
    def supports_lowcnds(self, *args) -> bool: ...
    def supports_debthread(self, *args) -> bool: ...
    def can_debug_standalone_dlls(self, *args) -> bool: ...
    def fake_memory(self, *args) -> bool: ...
    def has_get_processes(self, *args) -> bool: ...
    def has_attach_process(self, *args) -> bool: ...
    def has_detach_process(self, *args) -> bool: ...
    def has_request_pause(self, *args) -> bool: ...
    def has_set_exception_info(self, *args) -> bool: ...
    def has_thread_suspend(self, *args) -> bool: ...
    def has_thread_continue(self, *args) -> bool: ...
    def has_set_resume_mode(self, *args) -> bool: ...
    def has_thread_get_sreg_base(self, *args) -> bool: ...
    def has_check_bpt(self, *args) -> bool: ...
    def has_open_file(self, *args) -> bool: ...
    def has_update_call_stack(self, *args) -> bool: ...
    def has_appcall(self, *args) -> bool: ...
    def has_rexec(self, *args) -> bool: ...
    def has_map_address(self, *args) -> bool: ...
    def has_soft_bpt(self, *args) -> bool: ...
    default_regclasses: Incomplete
    def regs(self, *args) -> 'register_info_t &': ...
    memory_page_size: Incomplete
    bpt_size: Incomplete
    filetype: Incomplete
    resume_modes: Incomplete
    def is_resmod_avail(self, *args) -> bool: ...
    ev_init_debugger: Incomplete
    ev_term_debugger: Incomplete
    ev_get_processes: Incomplete
    ev_start_process: Incomplete
    ev_attach_process: Incomplete
    ev_detach_process: Incomplete
    ev_get_debapp_attrs: Incomplete
    ev_rebase_if_required_to: Incomplete
    ev_request_pause: Incomplete
    ev_exit_process: Incomplete
    ev_get_debug_event: Incomplete
    ev_resume: Incomplete
    ev_set_exception_info: Incomplete
    ev_suspended: Incomplete
    ev_thread_suspend: Incomplete
    ev_thread_continue: Incomplete
    ev_set_resume_mode: Incomplete
    ev_read_registers: Incomplete
    ev_write_register: Incomplete
    ev_thread_get_sreg_base: Incomplete
    ev_get_memory_info: Incomplete
    ev_read_memory: Incomplete
    ev_write_memory: Incomplete
    ev_check_bpt: Incomplete
    ev_update_bpts: Incomplete
    ev_update_lowcnds: Incomplete
    ev_open_file: Incomplete
    ev_close_file: Incomplete
    ev_read_file: Incomplete
    ev_write_file: Incomplete
    ev_map_address: Incomplete
    ev_get_debmod_extensions: Incomplete
    ev_update_call_stack: Incomplete
    ev_appcall: Incomplete
    ev_cleanup_appcall: Incomplete
    ev_eval_lowcnd: Incomplete
    ev_send_ioctl: Incomplete
    ev_dbg_enable_trace: Incomplete
    ev_is_tracing_enabled: Incomplete
    ev_rexec: Incomplete
    ev_get_srcinfo_path: Incomplete
    ev_bin_search: Incomplete
    def init_debugger(self, *args) -> bool: ...
    def term_debugger(self, *args) -> bool: ...
    def get_processes(self, *args) -> drc_t: ...
    def start_process(self, *args) -> drc_t: ...
    def attach_process(self, *args) -> drc_t: ...
    def detach_process(self, *args) -> drc_t: ...
    def get_debapp_attrs(self, *args) -> bool: ...
    def rebase_if_required_to(self, *args) -> None: ...
    def request_pause(self, *args) -> drc_t: ...
    def exit_process(self, *args) -> drc_t: ...
    def get_debug_event(self, *args) -> gdecode_t: ...
    def resume(self, *args) -> drc_t: ...
    def set_exception_info(self, *args) -> None: ...
    def suspended(self, *args) -> None: ...
    def thread_suspend(self, *args) -> drc_t: ...
    def thread_continue(self, *args) -> drc_t: ...
    def set_resume_mode(self, *args) -> drc_t: ...
    def read_registers(self, *args) -> drc_t: ...
    def write_register(self, *args) -> drc_t: ...
    def thread_get_sreg_base(self, *args) -> drc_t: ...
    def get_memory_info(self, *args) -> drc_t: ...
    def read_memory(self, *args) -> drc_t: ...
    def write_memory(self, *args) -> drc_t: ...
    def check_bpt(self, *args) -> drc_t: ...
    def update_bpts(self, *args) -> drc_t: ...
    def update_lowcnds(self, *args) -> drc_t: ...
    def open_file(self, *args) -> int: ...
    def close_file(self, *args) -> None: ...
    def read_file(self, *args) -> ssize_t: ...
    def write_file(self, *args) -> ssize_t: ...
    def map_address(self, *args) -> ea_t: ...
    def get_debmod_extensions(self, *args) -> 'void const *': ...
    def update_call_stack(self, *args) -> drc_t: ...
    def cleanup_appcall(self, *args) -> drc_t: ...
    def eval_lowcnd(self, *args) -> drc_t: ...
    def send_ioctl(self, *args) -> drc_t: ...
    def dbg_enable_trace(self, *args) -> bool: ...
    def is_tracing_enabled(self, *args) -> bool: ...
    def rexec(self, *args) -> int: ...
    def get_srcinfo_path(self, *args) -> bool: ...
    def bin_search(self, *args) -> drc_t: ...
    def __get_registers(self, *args) -> 'dynamic_wrapped_array_t< register_info_t >': ...
    def __get_nregs(self, *args) -> int: ...
    def __get_regclasses(self, *args) -> 'PyObject *': ...
    def __get_bpt_bytes(self, *args) -> bytevec_t: ...
    registers: Incomplete
    nregs: Incomplete
    regclasses: Incomplete
    bpt_bytes: Incomplete
    def __init__(self, *args) -> None: ...
    __swig_destroy__: Incomplete

DEBUGGER_ID_X86_IA32_WIN32_USER: Incomplete
DEBUGGER_ID_X86_IA32_LINUX_USER: Incomplete
DEBUGGER_ID_X86_IA32_MACOSX_USER: Incomplete
DEBUGGER_ID_ARM_IPHONE_USER: Incomplete
DEBUGGER_ID_X86_IA32_BOCHS: Incomplete
DEBUGGER_ID_6811_EMULATOR: Incomplete
DEBUGGER_ID_GDB_USER: Incomplete
DEBUGGER_ID_WINDBG: Incomplete
DEBUGGER_ID_X86_DOSBOX_EMULATOR: Incomplete
DEBUGGER_ID_ARM_LINUX_USER: Incomplete
DEBUGGER_ID_TRACE_REPLAYER: Incomplete
DEBUGGER_ID_X86_PIN_TRACER: Incomplete
DEBUGGER_ID_DALVIK_USER: Incomplete
DEBUGGER_ID_XNU_USER: Incomplete
DEBUGGER_ID_ARM_MACOS_USER: Incomplete
DBG_FLAG_REMOTE: Incomplete
DBG_FLAG_NOHOST: Incomplete
DBG_FLAG_FAKE_ATTACH: Incomplete
DBG_FLAG_HWDATBPT_ONE: Incomplete
DBG_FLAG_CAN_CONT_BPT: Incomplete
DBG_FLAG_NEEDPORT: Incomplete
DBG_FLAG_DONT_DISTURB: Incomplete
DBG_FLAG_SAFE: Incomplete
DBG_FLAG_CLEAN_EXIT: Incomplete
DBG_FLAG_USE_SREGS: Incomplete
DBG_FLAG_NOSTARTDIR: Incomplete
DBG_FLAG_NOPARAMETERS: Incomplete
DBG_FLAG_NOPASSWORD: Incomplete
DBG_FLAG_CONNSTRING: Incomplete
DBG_FLAG_SMALLBLKS: Incomplete
DBG_FLAG_MANMEMINFO: Incomplete
DBG_FLAG_EXITSHOTOK: Incomplete
DBG_FLAG_VIRTHREADS: Incomplete
DBG_FLAG_LOWCNDS: Incomplete
DBG_FLAG_DEBTHREAD: Incomplete
DBG_FLAG_DEBUG_DLL: Incomplete
DBG_FLAG_FAKE_MEMORY: Incomplete
DBG_FLAG_ANYSIZE_HWBPT: Incomplete
DBG_FLAG_TRACER_MODULE: Incomplete
DBG_FLAG_PREFER_SWBPTS: Incomplete
DBG_FLAG_LAZY_WATCHPTS: Incomplete
DBG_FLAG_FAST_STEP: Incomplete
DBG_FLAG_ADD_ENVS: Incomplete
DBG_FLAG_MERGE_ENVS: Incomplete
DBG_HAS_GET_PROCESSES: Incomplete
DBG_HAS_ATTACH_PROCESS: Incomplete
DBG_HAS_DETACH_PROCESS: Incomplete
DBG_HAS_REQUEST_PAUSE: Incomplete
DBG_HAS_SET_EXCEPTION_INFO: Incomplete
DBG_HAS_THREAD_SUSPEND: Incomplete
DBG_HAS_THREAD_CONTINUE: Incomplete
DBG_HAS_SET_RESUME_MODE: Incomplete
DBG_HAS_THREAD_GET_SREG_BASE: Incomplete
DBG_HAS_CHECK_BPT: Incomplete
DBG_HAS_OPEN_FILE: Incomplete
DBG_HAS_UPDATE_CALL_STACK: Incomplete
DBG_HAS_APPCALL: Incomplete
DBG_HAS_REXEC: Incomplete
DBG_HAS_MAP_ADDRESS: Incomplete
DBG_RESMOD_STEP_INTO: Incomplete
DBG_RESMOD_STEP_OVER: Incomplete
DBG_RESMOD_STEP_OUT: Incomplete
DBG_RESMOD_STEP_SRCINTO: Incomplete
DBG_RESMOD_STEP_SRCOVER: Incomplete
DBG_RESMOD_STEP_SRCOUT: Incomplete
DBG_RESMOD_STEP_USER: Incomplete
DBG_RESMOD_STEP_HANDLE: Incomplete
DBG_PROC_IS_DLL: Incomplete
DBG_PROC_IS_GUI: Incomplete
DBG_PROC_32BIT: Incomplete
DBG_PROC_64BIT: Incomplete
DBG_NO_TRACE: Incomplete
DBG_HIDE_WINDOW: Incomplete
DBG_SUSPENDED: Incomplete
DBG_NO_ASLR: Incomplete
BPT_OK: Incomplete
BPT_INTERNAL_ERR: Incomplete
BPT_BAD_TYPE: Incomplete
BPT_BAD_ALIGN: Incomplete
BPT_BAD_ADDR: Incomplete
BPT_BAD_LEN: Incomplete
BPT_TOO_MANY: Incomplete
BPT_READ_ERROR: Incomplete
BPT_WRITE_ERROR: Incomplete
BPT_SKIP: Incomplete
BPT_PAGE_OK: Incomplete
APPCALL_MANUAL: Incomplete
APPCALL_DEBEV: Incomplete
APPCALL_TIMEOUT: Incomplete
RQ_MASKING: Incomplete
RQ_SUSPEND: Incomplete
RQ_NOSUSP: Incomplete
RQ_IGNWERR: Incomplete
RQ_SILENT: Incomplete
RQ_VERBOSE: Incomplete
RQ_SWSCREEN: Incomplete
RQ__NOTHRRF: Incomplete
RQ_PROCEXIT: Incomplete
RQ_IDAIDLE: Incomplete
RQ_SUSPRUN: Incomplete
RQ_RESUME: Incomplete
RQ_RESMOD: Incomplete
RQ_RESMOD_SHIFT: Incomplete

class dyn_register_info_array:
    thisown: Incomplete
    __repr__ = _swig_repr
    data: Incomplete
    count: Incomplete
    def __init__(self, *args) -> None: ...
    def __len__(self, *args) -> size_t: ...
    def __getitem__(self, *args) -> 'register_info_t const &': ...
    def __setitem__(self, *args) -> None: ...
    __iter__ = ida_idaapi._bounded_getitem_iterator
    __swig_destroy__: Incomplete

def get_dbg(*args) -> 'debugger_t *': ...
def dbg_get_registers(*args) -> 'PyObject *': ...
def dbg_get_thread_sreg_base(*args) -> 'PyObject *': ...
def dbg_read_memory(*args) -> 'PyObject *': ...
def dbg_write_memory(*args) -> 'PyObject *': ...
def dbg_get_name(*args) -> 'PyObject *': ...
def dbg_get_memory_info(*args) -> 'PyObject *': ...
def appcall(*args) -> 'PyObject *': ...
def get_event_module_name(*args) -> size_t: ...
def get_event_module_base(*args) -> ea_t: ...
def get_event_module_size(*args) -> asize_t: ...
def get_event_exc_info(*args) -> size_t: ...
def get_event_info(*args) -> size_t: ...
def get_event_bpt_hea(*args) -> ea_t: ...
def get_event_exc_code(*args) -> uint: ...
def get_event_exc_ea(*args) -> ea_t: ...
def can_exc_continue(*args) -> bool: ...

NO_PROCESS: int
dbg_can_query: Incomplete

class Appcall_array__:
    __type: Incomplete
    def __init__(self, tp) -> None: ...
    __size: Incomplete
    __typedobj: Incomplete
    def pack(self, L): ...
    def try_to_convert_to_list(self, obj): ...
    def unpack(self, buf, as_list: bool = True): ...

class Appcall_callable__:
    __ea: Incomplete
    __tif: Incomplete
    __type: Incomplete
    __fields: Incomplete
    __options: Incomplete
    __timeout: Incomplete
    def __init__(self, ea, tinfo_or_typestr: Incomplete | None = None, fields: Incomplete | None = None) -> None: ...
    def __get_timeout(self): ...
    def __set_timeout(self, v) -> None: ...
    timeout: Incomplete
    def __get_options(self): ...
    def __set_options(self, v) -> None: ...
    options: Incomplete
    def __call__(self, *args): ...
    def __get_ea(self): ...
    def __set_ea(self, val) -> None: ...
    ea: Incomplete
    def __get_tif(self): ...
    tif: Incomplete
    def __get_size(self): ...
    size: Incomplete
    def __get_type(self): ...
    type: Incomplete
    def __get_fields(self): ...
    fields: Incomplete
    def retrieve(self, src: Incomplete | None = None, flags: int = 0): ...
    def store(self, obj, dest_ea: Incomplete | None = None, base_ea: int = 0, flags: int = 0): ...

class Appcall_consts__:
    __default: Incomplete
    def __init__(self, default: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...

class Appcall__:
    APPCALL_MANUAL: int
    APPCALL_DEBEV: int
    APPCALL_TIMEOUT: int
    __name__: str
    __consts: Incomplete
    def __init__(self) -> None: ...
    def __get_consts(self): ...
    Consts: Incomplete
    @staticmethod
    def __name_or_ea(name_or_ea): ...
    @staticmethod
    def __typedecl_or_tinfo(typedecl_or_tinfo, flags: Incomplete | None = None): ...
    @staticmethod
    def proto(name_or_ea, proto_or_tinfo, flags: Incomplete | None = None): ...
    def __getattr__(self, name_or_ea): ...
    def __getitem__(self, idx): ...
    @staticmethod
    def valueof(name, default: int = 0): ...
    @staticmethod
    def int64(v): ...
    @staticmethod
    def byref(val): ...
    @staticmethod
    def buffer(str: Incomplete | None = None, size: int = 0, fill: str = '\x00'): ...
    @staticmethod
    def obj(**kwds): ...
    @staticmethod
    def cstr(val): ...
    @staticmethod
    def UTF16(s): ...
    unicode = UTF16
    @staticmethod
    def array(type_name): ...
    @staticmethod
    def typedobj(typedecl_or_tinfo, ea: Incomplete | None = None): ...
    @staticmethod
    def set_appcall_options(opt): ...
    @staticmethod
    def get_appcall_options(): ...
    @staticmethod
    def cleanup_appcall(tid: int = 0): ...

Appcall: Incomplete