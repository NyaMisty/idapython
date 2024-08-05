# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

DIRTREE_BPTS: int
DIRTREE_END: int
DIRTREE_ENUMS: int
DIRTREE_ENUMS_BOOKMARKS: int
DIRTREE_FUNCS: int
DIRTREE_IDAPLACE_BOOKMARKS: int
DIRTREE_IMPORTS: int
DIRTREE_LOCAL_TYPES: int
DIRTREE_NAMES: int
DIRTREE_STRUCTS: int
DIRTREE_STRUCTS_BOOKMARKS: int
DTE_ALREADY_EXISTS: int
DTE_BAD_PATH: int
DTE_CANT_RENAME: int
DTE_LAST: int
DTE_MAX_DIR: int
DTE_NOT_DIRECTORY: int
DTE_NOT_EMPTY: int
DTE_NOT_FOUND: int
DTE_OK: int
DTE_OWN_CHILD: int
DTN_DISPLAY_NAME: int
DTN_FULL_NAME: int
SWIG_PYTHON_LEGACY_BOOL: int
direntry_t_BADIDX: int
direntry_t_ROOTIDX: int
dirspec_t_DSF_INODE_EA: int
dirspec_t_DSF_ORDERABLE: int
dirspec_t_DSF_PRIVRANGE: int

def delete_direntry_t(self) -> Any: ...
def delete_direntry_vec_t(self) -> Any: ...
def delete_dirspec_t(self) -> Any: ...
def delete_dirtree_cursor_t(self) -> Any: ...
def delete_dirtree_cursor_vec_t(self) -> Any: ...
def delete_dirtree_iterator_t(self) -> Any: ...
def delete_dirtree_selection_t(self) -> Any: ...
def delete_dirtree_t(self) -> Any: ...
def delete_dirtree_visitor_t(self) -> Any: ...
def direntry_t___eq__(self, r) -> bool: ...
def direntry_t___lt__(self, r) -> bool: ...
def direntry_t___ne__(self, r) -> bool: ...
def direntry_t_idx_get(self) -> uval_t: ...
def direntry_t_idx_set(self, idx) -> Any: ...
def direntry_t_isdir_get(self) -> bool: ...
def direntry_t_isdir_set(self, isdir) -> Any: ...
def direntry_t_swiginit(*args, **kwargs): ...
def direntry_t_swigregister(*args, **kwargs): ...
def direntry_t_valid(self) -> bool: ...
def direntry_vec_t___eq__(self, r) -> bool: ...
def direntry_vec_t___getitem__(self, i) -> direntry_t: ...
def direntry_vec_t___len__(self) -> size_t: ...
def direntry_vec_t___ne__(self, r) -> bool: ...
def direntry_vec_t___setitem__(self, i, v) -> Any: ...
def direntry_vec_t__del(self, x) -> bool: ...
def direntry_vec_t_add_unique(self, x) -> bool: ...
def direntry_vec_t_at(self, _idx) -> direntry_t: ...
@overload
def direntry_vec_t_begin(self) -> direntry_t: ...
@overload
def direntry_vec_t_begin(self) -> direntry_t: ...
def direntry_vec_t_capacity(self) -> size_t: ...
def direntry_vec_t_clear(self) -> Any: ...
def direntry_vec_t_empty(self) -> bool: ...
@overload
def direntry_vec_t_end(self) -> direntry_t: ...
@overload
def direntry_vec_t_end(self) -> direntry_t: ...
@overload
def direntry_vec_t_erase(self, it) -> direntry_t: ...
@overload
def direntry_vec_t_erase(self, first, last) -> direntry_t: ...
def direntry_vec_t_extract(self) -> direntry_t: ...
@overload
def direntry_vec_t_find(self, x) -> direntry_t: ...
@overload
def direntry_vec_t_find(self, x) -> direntry_t: ...
def direntry_vec_t_grow(self, x=...) -> Any: ...
def direntry_vec_t_has(self, x) -> bool: ...
def direntry_vec_t_inject(self, s, len) -> Any: ...
def direntry_vec_t_insert(self, it, x) -> direntry_t: ...
def direntry_vec_t_pop_back(self) -> Any: ...
@overload
def direntry_vec_t_push_back(self, x) -> Any: ...
@overload
def direntry_vec_t_push_back(self) -> direntry_t: ...
def direntry_vec_t_qclear(self) -> Any: ...
def direntry_vec_t_reserve(self, cnt) -> Any: ...
@overload
def direntry_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def direntry_vec_t_resize(self, _newsize) -> Any: ...
def direntry_vec_t_size(self) -> size_t: ...
def direntry_vec_t_swap(self, r) -> Any: ...
def direntry_vec_t_swiginit(*args, **kwargs): ...
def direntry_vec_t_swigregister(*args, **kwargs): ...
def direntry_vec_t_truncate(self) -> Any: ...
def dirspec_t_flags_get(self) -> uint32: ...
def dirspec_t_flags_set(self, flags) -> Any: ...
def dirspec_t_get_attrs(self, inode) -> qstring: ...
def dirspec_t_get_inode(self, dirpath, name) -> inode_t: ...
def dirspec_t_get_name(self, inode, name_flags=...) -> bool: ...
def dirspec_t_id_get(*args, **kwargs): ...
def dirspec_t_id_set(self, id) -> Any: ...
def dirspec_t_is_orderable(self) -> bool: ...
def dirspec_t_rename_inode(self, inode, newname) -> bool: ...
def dirspec_t_swiginit(*args, **kwargs): ...
def dirspec_t_swigregister(*args, **kwargs): ...
def dirspec_t_unlink_inode(self, inode) -> Any: ...
def dirtree_cursor_t___eq__(self, r) -> bool: ...
def dirtree_cursor_t___ge__(self, r) -> bool: ...
def dirtree_cursor_t___gt__(self, r) -> bool: ...
def dirtree_cursor_t___le__(self, r) -> bool: ...
def dirtree_cursor_t___lt__(self, r) -> bool: ...
def dirtree_cursor_t___ne__(self, r) -> bool: ...
def dirtree_cursor_t_compare(self, r) -> int: ...
def dirtree_cursor_t_is_root_cursor(self) -> bool: ...
def dirtree_cursor_t_parent_get(self) -> diridx_t: ...
def dirtree_cursor_t_parent_set(self, parent) -> Any: ...
def dirtree_cursor_t_rank_get(self) -> size_t: ...
def dirtree_cursor_t_rank_set(self, rank) -> Any: ...
def dirtree_cursor_t_root_cursor() -> dirtree_cursor_t: ...
def dirtree_cursor_t_set_root_cursor(self) -> Any: ...
def dirtree_cursor_t_swiginit(*args, **kwargs): ...
def dirtree_cursor_t_swigregister(*args, **kwargs): ...
def dirtree_cursor_t_valid(self) -> bool: ...
def dirtree_cursor_vec_t___eq__(self, r) -> bool: ...
def dirtree_cursor_vec_t___getitem__(self, i) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t___len__(self) -> size_t: ...
def dirtree_cursor_vec_t___ne__(self, r) -> bool: ...
def dirtree_cursor_vec_t___setitem__(self, i, v) -> Any: ...
def dirtree_cursor_vec_t__del(self, x) -> bool: ...
def dirtree_cursor_vec_t_add_unique(self, x) -> bool: ...
def dirtree_cursor_vec_t_at(self, _idx) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_begin(self) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_begin(self) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t_capacity(self) -> size_t: ...
def dirtree_cursor_vec_t_clear(self) -> Any: ...
def dirtree_cursor_vec_t_empty(self) -> bool: ...
@overload
def dirtree_cursor_vec_t_end(self) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_end(self) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_erase(self, it) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_erase(self, first, last) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t_extract(self) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_find(self, x) -> dirtree_cursor_t: ...
@overload
def dirtree_cursor_vec_t_find(self, x) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t_grow(self, x=...) -> Any: ...
def dirtree_cursor_vec_t_has(self, x) -> bool: ...
def dirtree_cursor_vec_t_inject(self, s, len) -> Any: ...
def dirtree_cursor_vec_t_insert(self, it, x) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t_pop_back(self) -> Any: ...
@overload
def dirtree_cursor_vec_t_push_back(self, x) -> Any: ...
@overload
def dirtree_cursor_vec_t_push_back(self) -> dirtree_cursor_t: ...
def dirtree_cursor_vec_t_qclear(self) -> Any: ...
def dirtree_cursor_vec_t_reserve(self, cnt) -> Any: ...
@overload
def dirtree_cursor_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def dirtree_cursor_vec_t_resize(self, _newsize) -> Any: ...
def dirtree_cursor_vec_t_size(self) -> size_t: ...
def dirtree_cursor_vec_t_swap(self, r) -> Any: ...
def dirtree_cursor_vec_t_swiginit(*args, **kwargs): ...
def dirtree_cursor_vec_t_swigregister(*args, **kwargs): ...
def dirtree_cursor_vec_t_truncate(self) -> Any: ...
def dirtree_iterator_t_cursor_get(self) -> dirtree_cursor_t: ...
def dirtree_iterator_t_cursor_set(self, cursor) -> Any: ...
def dirtree_iterator_t_pattern_get(*args, **kwargs): ...
def dirtree_iterator_t_pattern_set(self, pattern) -> Any: ...
def dirtree_iterator_t_swiginit(*args, **kwargs): ...
def dirtree_iterator_t_swigregister(*args, **kwargs): ...
def dirtree_selection_t_swiginit(*args, **kwargs): ...
def dirtree_selection_t_swigregister(*args, **kwargs): ...
def dirtree_t_change_rank(self, path, rank_delta) -> dterr_t: ...
def dirtree_t_chdir(self, path) -> dterr_t: ...
def dirtree_t_errstr(*args, **kwargs): ...
def dirtree_t_find_entry(self, de) -> dirtree_cursor_t: ...
def dirtree_t_findfirst(self, ff, pattern) -> bool: ...
def dirtree_t_findnext(self, ff) -> bool: ...
@overload
def dirtree_t_get_abspath(self, cursor, name_flags=...) -> qstring: ...
@overload
def dirtree_t_get_abspath(self, relpath) -> qstring: ...
def dirtree_t_get_dir_size(self, diridx) -> ssize_t: ...
def dirtree_t_get_entry_attrs(self, de) -> qstring: ...
def dirtree_t_get_entry_name(self, de, name_flags=...) -> qstring: ...
def dirtree_t_get_id(*args, **kwargs): ...
def dirtree_t_get_parent_cursor(self, cursor) -> dirtree_cursor_t: ...
def dirtree_t_get_rank(self, diridx, de) -> ssize_t: ...
def dirtree_t_getcwd(self) -> qstring: ...
def dirtree_t_is_dir_ordered(self, diridx) -> bool: ...
def dirtree_t_is_orderable(self) -> bool: ...
@overload
def dirtree_t_isdir(de) -> bool: ...
@overload
def dirtree_t_isdir(path) -> bool: ...
@overload
def dirtree_t_isfile(de) -> bool: ...
@overload
def dirtree_t_isfile(path) -> bool: ...
@overload
def dirtree_t_link(self, path) -> dterr_t: ...
@overload
def dirtree_t_link(self, inode) -> dterr_t: ...
def dirtree_t_load(self) -> bool: ...
def dirtree_t_mkdir(self, path) -> dterr_t: ...
def dirtree_t_notify_dirtree(self, added, inode) -> Any: ...
def dirtree_t_rename(self, _from, to) -> dterr_t: ...
def dirtree_t_resolve_cursor(self, cursor) -> direntry_t: ...
def dirtree_t_resolve_path(self, path) -> direntry_t: ...
def dirtree_t_rmdir(self, path) -> dterr_t: ...
def dirtree_t_save(self) -> bool: ...
def dirtree_t_set_id(self, nm) -> Any: ...
def dirtree_t_set_natural_order(self, diridx, enable) -> bool: ...
def dirtree_t_swiginit(*args, **kwargs): ...
def dirtree_t_swigregister(*args, **kwargs): ...
def dirtree_t_traverse(self, v) -> ssize_t: ...
@overload
def dirtree_t_unlink(self, path) -> dterr_t: ...
@overload
def dirtree_t_unlink(self, inode) -> dterr_t: ...
def dirtree_visitor_t_swiginit(*args, **kwargs): ...
def dirtree_visitor_t_swigregister(*args, **kwargs): ...
def dirtree_visitor_t_visit(self, c, de) -> ssize_t: ...
def disown_dirspec_t(*args, **kwargs): ...
def disown_dirtree_visitor_t(*args, **kwargs): ...
def get_std_dirtree(id) -> dirtree_t: ...
def new_direntry_t(i=..., d=...) -> direntry_t: ...
def new_direntry_vec_t(x) -> direntry_vec_t: ...
def new_dirspec_t(_self, nm=..., f=...) -> dirspec_t: ...
def new_dirtree_cursor_t(_parent=..., _rank=...) -> dirtree_cursor_t: ...
def new_dirtree_cursor_vec_t(x) -> dirtree_cursor_vec_t: ...
def new_dirtree_iterator_t() -> dirtree_iterator_t: ...
def new_dirtree_selection_t() -> dirtree_selection_t: ...
def new_dirtree_t(ds) -> dirtree_t: ...
def new_dirtree_visitor_t(_self) -> dirtree_visitor_t: ...
