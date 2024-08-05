# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from ..uiparser import UIParser as UIParser
from .qobjectcreator import LoaderCreatorPolicy as LoaderCreatorPolicy
from PyQt5 import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class DynamicUILoader(UIParser):
    def __init__(self, package) -> None: ...
    def createToplevelWidget(self, classname, widgetname): ...
    toplevelInst: Incomplete
    def loadUi(self, filename, toplevelInst, resource_suffix): ...
