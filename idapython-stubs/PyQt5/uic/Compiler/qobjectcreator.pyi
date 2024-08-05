# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from ..port_v2.as_string import as_string as as_string
from .indenter import write_code as write_code
from .qtproxies import Literal as Literal, QtGui as QtGui, QtWidgets as QtWidgets, strict_getattr as strict_getattr
from _typeshed import Incomplete

logger: Incomplete
DEBUG: Incomplete

class _QtWrapper:
    @classmethod
    def search(cls, name): ...

class _QtGuiWrapper(_QtWrapper):
    module = QtGui

class _QtWidgetsWrapper(_QtWrapper):
    module = QtWidgets

class _ModuleWrapper:
    _package: Incomplete
    _module: Incomplete
    _classes: Incomplete
    _used: bool
    def __init__(self, name, classes) -> None: ...
    def search(self, cls): ...
    def _writeImportCode(self) -> None: ...

class _CustomWidgetLoader:
    _widgets: Incomplete
    _usedWidgets: Incomplete
    def __init__(self) -> None: ...
    def addCustomWidget(self, widgetClass, baseClass, module) -> None: ...
    def _resolveBaseclass(self, baseClass): ...
    def search(self, cls): ...
    def _writeImportCode(self) -> None: ...

class CompilerCreatorPolicy:
    _modules: Incomplete
    def __init__(self) -> None: ...
    def createQtGuiWidgetsWrappers(self): ...
    def createModuleWrapper(self, name, classes): ...
    def createCustomWidgetLoader(self): ...
    def instantiate(self, clsObject, objectname, ctor_args, is_attribute: bool = True, no_instantiation: bool = False): ...
    def invoke(self, rname, method, args): ...
    def getSlot(self, object, slotname): ...
    def asString(self, s): ...
    def _writeOutImports(self) -> None: ...