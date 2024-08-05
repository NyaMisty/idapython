# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from . import qtproxies as qtproxies
from ..properties import Properties as Properties
from ..uiparser import UIParser as UIParser
from .indenter import createCodeIndenter as createCodeIndenter, getIndenter as getIndenter, write_code as write_code
from .qobjectcreator import CompilerCreatorPolicy as CompilerCreatorPolicy
from _typeshed import Incomplete

class UICompiler(UIParser):
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def setContext(self, context) -> None: ...
    def createToplevelWidget(self, classname, widgetname): ...
    def setDelayedProps(self) -> None: ...
    _resources: Incomplete
    def finalize(self) -> None: ...
    def compileUi(self, input_stream, output_stream, from_imports, resource_suffix, import_from): ...