# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from .driver import Driver as Driver
from .exceptions import NoSuchClassError as NoSuchClassError, NoSuchWidgetError as NoSuchWidgetError
from PyQt5 import QtCore as QtCore
from _typeshed import Incomplete

Version: Incomplete

def main() -> None: ...
