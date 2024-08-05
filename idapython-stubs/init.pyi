# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from idc import *
from idautils import *
import pydoc
from _typeshed import Incomplete
from idaapi import Appcall as Appcall, Form as Form, cvar as cvar, get_user_idadir as get_user_idadir

base: Incomplete
dllspath: Incomplete
i: Incomplete
IDAPYTHON_DYNLOAD_BASE: Incomplete
lib_dynload: Incomplete

class IDAPythonStdOut:
    encoding: str
    def write(self, text) -> None: ...
    def flush(self) -> None: ...
    def isatty(self): ...

def runscript(script): ...
def print_banner() -> None: ...

_orig_stdout: Incomplete
_orig_stderr: Incomplete

class IDAPythonHelpPrompter:
    def readline(self): ...

class IDAPythonHelp(pydoc.Helper):
    def __init__(self) -> None: ...
    def help(self, *args): ...

help: Incomplete
idausr_python_list: Incomplete
one: Incomplete
userrc: Incomplete
