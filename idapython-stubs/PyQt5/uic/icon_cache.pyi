# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from _typeshed import Incomplete

class IconCache:
    _object_factory: Incomplete
    _qtgui_module: Incomplete
    _base_dir: str
    _cache: Incomplete
    def __init__(self, object_factory, qtgui_module) -> None: ...
    def set_base_dir(self, base_dir) -> None: ...
    def get_icon(self, iconset): ...

class _IconSet:
    _fallback: Incomplete
    _use_fallback: bool
    _roles: Incomplete
    icon: Incomplete
    def __init__(self, iconset, base_dir) -> None: ...
    @staticmethod
    def _file_name(fname, base_dir): ...
    def set_icon(self, icon, qtgui_module) -> None: ...
    def __eq__(self, other): ...
