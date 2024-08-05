# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from . import compileUi as compileUi, loadUi as loadUi
from _typeshed import Incomplete

class Driver:
    LOGGER_NAME: str
    _opts: Incomplete
    _ui_file: Incomplete
    def __init__(self, opts, ui_file) -> None: ...
    def invoke(self): ...
    def _preview(self): ...
    def _generate(self) -> None: ...
    def on_IOError(self, e) -> None: ...
    def on_SyntaxError(self, e) -> None: ...
    def on_NoSuchClassError(self, e) -> None: ...
    def on_NoSuchWidgetError(self, e) -> None: ...
    def on_Exception(self, e) -> None: ...