# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from ..Compiler.proxy_metaclass import ProxyMetaclass as ProxyMetaclass

class ProxyBase(metaclass=ProxyMetaclass): ...
