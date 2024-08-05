# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

BOOKMARKS_PROMPT_WITH_HINT_PREFIX: str
CURLOC_LIST: str
DEFAULT_CURSOR_Y: int
DEFAULT_LNNUM: int
LSEF_ALL: int
LSEF_PLACE: int
LSEF_PTYPE: int
LSEF_RINFO: int
MAX_MARK_SLOT: int
SWIG_PYTHON_LEGACY_BOOL: int
UNHID_FUNC: int
UNHID_RANGE: int
UNHID_SEGM: int

def bookmarks_t_erase(e, index, ud) -> bool: ...
def bookmarks_t_find_index(e, ud) -> uint32: ...
def bookmarks_t_get(*args, **kwargs): ...
def bookmarks_t_get_desc(e, index, ud) -> bool: ...
def bookmarks_t_get_dirtree_id(e, ud) -> dirtree_id_t: ...
def bookmarks_t_mark(e, index, title, desc, ud) -> uint32: ...
def bookmarks_t_size(e, ud) -> uint32: ...
def bookmarks_t_swigregister(*args, **kwargs): ...
def delete_graph_location_info_t(self) -> Any: ...
def delete_lochist_entry_t(self) -> Any: ...
def delete_lochist_t(self) -> Any: ...
def delete_renderer_info_pos_t(self) -> Any: ...
def delete_renderer_info_t(self) -> Any: ...
def delete_segm_move_info_t(self) -> Any: ...
def delete_segm_move_info_vec_t(self) -> Any: ...
def delete_segm_move_infos_t(self) -> Any: ...
def graph_location_info_t___eq__(self, r) -> bool: ...
def graph_location_info_t___ne__(self, r) -> bool: ...
def graph_location_info_t_orgx_get(self) -> double: ...
def graph_location_info_t_orgx_set(self, orgx) -> Any: ...
def graph_location_info_t_orgy_get(self) -> double: ...
def graph_location_info_t_orgy_set(self, orgy) -> Any: ...
def graph_location_info_t_swiginit(*args, **kwargs): ...
def graph_location_info_t_swigregister(*args, **kwargs): ...
def graph_location_info_t_zoom_get(self) -> double: ...
def graph_location_info_t_zoom_set(self, zoom) -> Any: ...
def lochist_entry_t_acquire_place(self, in_p) -> Any: ...
def lochist_entry_t_is_valid(self) -> bool: ...
@overload
def lochist_entry_t_place(self) -> place_t: ...
@overload
def lochist_entry_t_place(self) -> place_t: ...
def lochist_entry_t_plce_get(self) -> place_t: ...
def lochist_entry_t_plce_set(self, plce) -> Any: ...
@overload
def lochist_entry_t_renderer_info(self) -> renderer_info_t: ...
@overload
def lochist_entry_t_renderer_info(self) -> renderer_info_t: ...
def lochist_entry_t_rinfo_get(self) -> renderer_info_t: ...
def lochist_entry_t_rinfo_set(self, rinfo) -> Any: ...
def lochist_entry_t_set_place(self, p) -> Any: ...
def lochist_entry_t_swiginit(*args, **kwargs): ...
def lochist_entry_t_swigregister(*args, **kwargs): ...
def lochist_t_back(self, cnt, try_to_unhide) -> bool: ...
def lochist_t_clear(self) -> Any: ...
def lochist_t_current_index(self) -> uint32: ...
def lochist_t_fwd(self, cnt, try_to_unhide) -> bool: ...
def lochist_t_get(self, out, index) -> bool: ...
def lochist_t_get_current(self) -> lochist_entry_t: ...
def lochist_t_get_place_id(self) -> int: ...
def lochist_t_get_template_place(self) -> place_t: ...
def lochist_t_init(self, stream_name, _defpos, _ud, _flags) -> bool: ...
def lochist_t_is_history_enabled(self) -> bool: ...
def lochist_t_jump(self, try_to_unhide, e) -> Any: ...
def lochist_t_netcode(self) -> nodeidx_t: ...
def lochist_t_save(self) -> Any: ...
def lochist_t_seek(self, index, try_to_unhide) -> bool: ...
def lochist_t_set(self, index, e) -> Any: ...
def lochist_t_set_current(self, e) -> Any: ...
def lochist_t_size(self) -> uint32: ...
def lochist_t_swiginit(*args, **kwargs): ...
def lochist_t_swigregister(*args, **kwargs): ...
def new_graph_location_info_t() -> graph_location_info_t: ...
def new_lochist_entry_t(other) -> lochist_entry_t: ...
def new_lochist_t() -> lochist_t: ...
def new_renderer_info_pos_t() -> renderer_info_pos_t: ...
def new_renderer_info_t(_rtype, cx, cy) -> renderer_info_t: ...
def new_segm_move_info_t(_from=..., _to=..., _sz=...) -> segm_move_info_t: ...
def new_segm_move_info_vec_t(x) -> segm_move_info_vec_t: ...
def new_segm_move_infos_t() -> segm_move_infos_t: ...
def renderer_info_pos_t___eq__(self, r) -> bool: ...
def renderer_info_pos_t___ne__(self, r) -> bool: ...
def renderer_info_pos_t_cx_get(self) -> short: ...
def renderer_info_pos_t_cx_set(self, cx) -> Any: ...
def renderer_info_pos_t_cy_get(self) -> short: ...
def renderer_info_pos_t_cy_set(self, cy) -> Any: ...
def renderer_info_pos_t_node_get(self) -> int: ...
def renderer_info_pos_t_node_set(self, node) -> Any: ...
def renderer_info_pos_t_swiginit(*args, **kwargs): ...
def renderer_info_pos_t_swigregister(*args, **kwargs): ...
def renderer_info_t___eq__(self, r) -> bool: ...
def renderer_info_t___ne__(self, r) -> bool: ...
def renderer_info_t_gli_get(self) -> graph_location_info_t: ...
def renderer_info_t_gli_set(self, gli) -> Any: ...
def renderer_info_t_pos_get(self) -> renderer_info_pos_t: ...
def renderer_info_t_pos_set(self, pos) -> Any: ...
def renderer_info_t_rtype_get(self) -> tcc_renderer_type_t: ...
def renderer_info_t_rtype_set(self, rtype) -> Any: ...
def renderer_info_t_swiginit(*args, **kwargs): ...
def renderer_info_t_swigregister(*args, **kwargs): ...
def segm_move_info_t___eq__(self, r) -> bool: ...
def segm_move_info_t___ne__(self, r) -> bool: ...
def segm_move_info_t__from_get(self) -> ea_t: ...
def segm_move_info_t__from_set(self, _from) -> Any: ...
def segm_move_info_t_size_get(self) -> size_t: ...
def segm_move_info_t_size_set(self, size) -> Any: ...
def segm_move_info_t_swiginit(*args, **kwargs): ...
def segm_move_info_t_swigregister(*args, **kwargs): ...
def segm_move_info_t_to_get(self) -> ea_t: ...
def segm_move_info_t_to_set(self, to) -> Any: ...
def segm_move_info_vec_t___eq__(self, r) -> bool: ...
def segm_move_info_vec_t___getitem__(self, i) -> segm_move_info_t: ...
def segm_move_info_vec_t___len__(self) -> size_t: ...
def segm_move_info_vec_t___ne__(self, r) -> bool: ...
def segm_move_info_vec_t___setitem__(self, i, v) -> Any: ...
def segm_move_info_vec_t__del(self, x) -> bool: ...
def segm_move_info_vec_t_add_unique(self, x) -> bool: ...
def segm_move_info_vec_t_at(self, _idx) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_begin(self) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_begin(self) -> segm_move_info_t: ...
def segm_move_info_vec_t_capacity(self) -> size_t: ...
def segm_move_info_vec_t_clear(self) -> Any: ...
def segm_move_info_vec_t_empty(self) -> bool: ...
@overload
def segm_move_info_vec_t_end(self) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_end(self) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_erase(self, it) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_erase(self, first, last) -> segm_move_info_t: ...
def segm_move_info_vec_t_extract(self) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_find(self, x) -> segm_move_info_t: ...
@overload
def segm_move_info_vec_t_find(self, x) -> segm_move_info_t: ...
def segm_move_info_vec_t_grow(self, x=...) -> Any: ...
def segm_move_info_vec_t_has(self, x) -> bool: ...
def segm_move_info_vec_t_inject(self, s, len) -> Any: ...
def segm_move_info_vec_t_insert(self, it, x) -> segm_move_info_t: ...
def segm_move_info_vec_t_pop_back(self) -> Any: ...
@overload
def segm_move_info_vec_t_push_back(self, x) -> Any: ...
@overload
def segm_move_info_vec_t_push_back(self) -> segm_move_info_t: ...
def segm_move_info_vec_t_qclear(self) -> Any: ...
def segm_move_info_vec_t_reserve(self, cnt) -> Any: ...
@overload
def segm_move_info_vec_t_resize(self, _newsize, x) -> Any: ...
@overload
def segm_move_info_vec_t_resize(self, _newsize) -> Any: ...
def segm_move_info_vec_t_size(self) -> size_t: ...
def segm_move_info_vec_t_swap(self, r) -> Any: ...
def segm_move_info_vec_t_swiginit(*args, **kwargs): ...
def segm_move_info_vec_t_swigregister(*args, **kwargs): ...
def segm_move_info_vec_t_truncate(self) -> Any: ...
def segm_move_infos_t_find(self, ea) -> segm_move_info_t: ...
def segm_move_infos_t_swiginit(*args, **kwargs): ...
def segm_move_infos_t_swigregister(*args, **kwargs): ...
