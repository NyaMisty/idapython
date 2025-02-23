from typing import Any

SWIG_PYTHON_LEGACY_BOOL: int

def delete_qfile_t(self) -> Any: ...
def new_qfile_t(pycapsule=...) -> qfile_t: ...
def qfile_t___idc_cvt_id___get(self) -> int: ...
def qfile_t___idc_cvt_id___set(self, __idc_cvt_id__) -> Any: ...
def qfile_t_close(self) -> Any: ...
def qfile_t_filename(*args, **kwargs): ...
def qfile_t_flush(self) -> int: ...
def qfile_t_from_capsule(pycapsule) -> qfile_t: ...
def qfile_t_from_fp(fp) -> qfile_t: ...
def qfile_t_get_byte(*args, **kwargs): ...
def qfile_t_get_fp(*args, **kwargs): ...
def qfile_t_gets(*args, **kwargs): ...
def qfile_t_open(self, filename, mode) -> bool: ...
def qfile_t_opened(self) -> bool: ...
def qfile_t_put_byte(self, chr) -> int: ...
def qfile_t_puts(self, str) -> int: ...
def qfile_t_read(*args, **kwargs): ...
def qfile_t_readbytes(*args, **kwargs): ...
def qfile_t_seek(self, offset, whence=...) -> int: ...
def qfile_t_size(self) -> int64: ...
def qfile_t_swiginit(*args, **kwargs): ...
def qfile_t_swigregister(*args, **kwargs): ...
def qfile_t_tell(self) -> int64: ...
def qfile_t_tmpfile() -> qfile_t: ...
def qfile_t_write(self, py_buf) -> int: ...
def qfile_t_writebytes(self, py_buf, big_endian) -> int: ...
# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"