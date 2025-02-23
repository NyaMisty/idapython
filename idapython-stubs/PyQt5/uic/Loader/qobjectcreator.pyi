# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from PyQt5 import QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class _QtWrapper:
    @classmethod
    def search(cls, name): ...

class _QtGuiWrapper(_QtWrapper):
    module = QtGui

class _QtWidgetsWrapper(_QtWrapper):
    module = QtWidgets

class _ModuleWrapper:
    _moduleName: Incomplete
    _module: Incomplete
    _classes: Incomplete
    def __init__(self, moduleName, classes) -> None: ...
    def search(self, cls): ...

class _CustomWidgetLoader:
    _widgets: Incomplete
    _modules: Incomplete
    _package: Incomplete
    def __init__(self, package) -> None: ...
    def addCustomWidget(self, widgetClass, baseClass, module) -> None: ...
    def search(self, cls): ...

class LoaderCreatorPolicy:
    _package: Incomplete
    def __init__(self, package) -> None: ...
    def createQtGuiWidgetsWrappers(self): ...
    def createModuleWrapper(self, moduleName, classes): ...
    def createCustomWidgetLoader(self): ...
    def instantiate(self, clsObject, objectName, ctor_args, is_attribute: bool = True): ...
    def invoke(self, rname, method, args): ...
    def getSlot(self, object, slotname): ...
    def asString(self, s): ...
