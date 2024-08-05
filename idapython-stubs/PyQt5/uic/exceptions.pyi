# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

class NoSuchClassError(Exception):
    def __str__(self) -> str: ...

class NoSuchWidgetError(Exception):
    def __str__(self) -> str: ...

class UnsupportedPropertyError(Exception): ...
class WidgetPluginError(Exception): ...
