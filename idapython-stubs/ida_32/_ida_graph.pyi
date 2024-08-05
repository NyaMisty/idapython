# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from typing import Any, overload

COLLAPSED_NODE: int
GLICTL_CENTER: int
MTG_DOT_NODE: int
MTG_GROUP_NODE: int
MTG_NON_DISPLAYABLE_NODE: int
NIFF_SHOW_CONTENTS: int
NIF_ALL: int
NIF_BG_COLOR: int
NIF_EA: int
NIF_FLAGS: int
NIF_FRAME_COLOR: int
NIF_TEXT: int
SWIG_PYTHON_LEGACY_BOOL: int
cvar: Any
edge_back: int
edge_cross: int
edge_error: int
edge_forward: int
edge_subgraph: int
edge_tree: int
git_edge: int
git_elp: int
git_node: int
git_none: int
git_text: int
git_tool: int
grcode_attach_menu_item: int
grcode_calculating_layout: int
grcode_center_on: int
grcode_change_group_visibility: int
grcode_changed_graph: int
grcode_clear: int
grcode_clicked: int
grcode_create_circle_layout: int
grcode_create_digraph_layout: int
grcode_create_disasm_graph1: int
grcode_create_disasm_graph2: int
grcode_create_graph_viewer: int
grcode_create_group: int
grcode_create_mutable_graph: int
grcode_create_tree_layout: int
grcode_create_user_graph_place: int
grcode_creating_group: int
grcode_dblclicked: int
grcode_del_custom_layout: int
grcode_del_node_info: int
grcode_delete_group: int
grcode_delete_mutable_graph: int
grcode_deleting_group: int
grcode_destroyed: int
grcode_edge_infos_wrapper_clear: int
grcode_edge_infos_wrapper_copy: int
grcode_empty: int
grcode_find_subgraph_node: int
grcode_fit_window: int
grcode_get_curnode: int
grcode_get_custom_layout: int
grcode_get_gli: int
grcode_get_graph_groups: int
grcode_get_graph_viewer: int
grcode_get_node_info: int
grcode_get_node_representative: int
grcode_get_selection: int
grcode_get_viewer_graph: int
grcode_gotfocus: int
grcode_group_visibility: int
grcode_is_visible_node: int
grcode_layout_calculated: int
grcode_lostfocus: int
grcode_node_qty: int
grcode_nrect: int
grcode_refresh_viewer: int
grcode_reserved: int
grcode_reserved2: int
grcode_set_custom_layout: int
grcode_set_edge: int
grcode_set_gli: int
grcode_set_graph_groups: int
grcode_set_node_info: int
grcode_set_titlebar_height: int
grcode_set_viewer_graph: int
grcode_user_draw: int
grcode_user_hint: int
grcode_user_refresh: int
grcode_user_size: int
grcode_user_text: int
grcode_user_title: int
grcode_viewer_create_groups: int
grcode_viewer_create_groups_vec: int
grcode_viewer_delete_groups: int
grcode_viewer_delete_groups_vec: int
grcode_viewer_groups_visibility: int
grcode_viewer_groups_visibility_vec: int

def TPointDouble___eq__(self, r) -> bool: ...
def TPointDouble___ne__(self, r) -> bool: ...
def TPointDouble_add(self, r) -> Any: ...
def TPointDouble_negate(self) -> Any: ...
def TPointDouble_sub(self, r) -> Any: ...
def TPointDouble_swiginit(*args, **kwargs): ...
def TPointDouble_swigregister(*args, **kwargs): ...
def TPointDouble_x_get(self) -> double: ...
def TPointDouble_x_set(self, x) -> Any: ...
def TPointDouble_y_get(self) -> double: ...
def TPointDouble_y_set(self, y) -> Any: ...
def abstract_graph_t_callback_ud_get(*args, **kwargs): ...
def abstract_graph_t_callback_ud_set(self, callback_ud) -> Any: ...
def abstract_graph_t_circle_center_get(self) -> point_t: ...
def abstract_graph_t_circle_center_set(self, circle_center) -> Any: ...
def abstract_graph_t_circle_radius_get(self) -> int: ...
def abstract_graph_t_circle_radius_set(self, circle_radius) -> Any: ...
def abstract_graph_t_create_circle_layout(self, p, radius) -> bool: ...
def abstract_graph_t_create_tree_layout(self) -> bool: ...
def abstract_graph_t_current_layout_get(self) -> layout_type_t: ...
def abstract_graph_t_current_layout_set(self, current_layout) -> Any: ...
def abstract_graph_t_get_edge(self, e) -> edge_info_t: ...
def abstract_graph_t_grcall(self, code) -> ssize_t: ...
def abstract_graph_t_nrect(self, n) -> rect_t: ...
def abstract_graph_t_rect_edges_made_get(self) -> bool: ...
def abstract_graph_t_rect_edges_made_set(self, rect_edges_made) -> Any: ...
def abstract_graph_t_set_callback(self, _callback, _ud) -> Any: ...
def abstract_graph_t_swiginit(*args, **kwargs): ...
def abstract_graph_t_swigregister(*args, **kwargs): ...
def abstract_graph_t_title_get(*args, **kwargs): ...
def abstract_graph_t_title_set(self, title) -> Any: ...
def calc_dist(p, q) -> double: ...
def clr_node_info(gid, node, flags) -> Any: ...
@overload
def create_disasm_graph(ea) -> mutable_graph_t: ...
@overload
def create_disasm_graph(ranges) -> mutable_graph_t: ...
def create_graph_viewer(*args, **kwargs): ...
def create_mutable_graph(id) -> mutable_graph_t: ...
def create_user_graph_place(node, lnnum) -> user_graph_place_t: ...
def del_node_info(gid, node) -> Any: ...
def delete_TPointDouble(self) -> Any: ...
def delete_abstract_graph_t(self) -> Any: ...
def delete_edge_info_t(self) -> Any: ...
def delete_edge_layout_point_t(self) -> Any: ...
def delete_edge_segment_t(self) -> Any: ...
def delete_edge_t(self) -> Any: ...
def delete_graph_item_t(self) -> Any: ...
def delete_graph_node_visitor_t(self) -> Any: ...
def delete_graph_path_visitor_t(self) -> Any: ...
def delete_graph_visitor_t(self) -> Any: ...
def delete_group_crinfo_t(self) -> Any: ...
def delete_interval_t(self) -> Any: ...
def delete_mutable_graph(g) -> Any: ...
def delete_mutable_graph_t(self) -> Any: ...
def delete_node_info_t(self) -> Any: ...
def delete_node_layout_t(self) -> Any: ...
def delete_node_ordering_t(self) -> Any: ...
def delete_point_t(self) -> Any: ...
def delete_pointseq_t(self) -> Any: ...
def delete_pointvec_t(self) -> Any: ...
def delete_rect_t(self) -> Any: ...
def delete_row_info_t(self) -> Any: ...
def delete_screen_graph_selection_base_t(self) -> Any: ...
def delete_screen_graph_selection_t(self) -> Any: ...
def delete_selection_item_t(self) -> Any: ...
def delete_user_graph_place_t(self) -> Any: ...
def disown_abstract_graph_t(*args, **kwargs): ...
def disown_graph_node_visitor_t(*args, **kwargs): ...
def disown_graph_path_visitor_t(*args, **kwargs): ...
def disown_graph_visitor_t(*args, **kwargs): ...
def edge_info_t_color_get(self) -> bgcolor_t: ...
def edge_info_t_color_set(self, color) -> Any: ...
def edge_info_t_dstoff_get(self) -> int: ...
def edge_info_t_dstoff_set(self, dstoff) -> Any: ...
def edge_info_t_layout_get(self) -> pointseq_t: ...
def edge_info_t_layout_set(self, layout) -> Any: ...
def edge_info_t_reverse_layout(self) -> Any: ...
def edge_info_t_srcoff_get(self) -> int: ...
def edge_info_t_srcoff_set(self, srcoff) -> Any: ...
def edge_info_t_swiginit(*args, **kwargs): ...
def edge_info_t_swigregister(*args, **kwargs): ...
def edge_info_t_width_get(self) -> int: ...
def edge_info_t_width_set(self, width) -> Any: ...
def edge_infos_wrapper_t_clear(self) -> Any: ...
def edge_infos_wrapper_t_ptr_get(*args, **kwargs): ...
def edge_infos_wrapper_t_ptr_set(self, ptr) -> Any: ...
def edge_infos_wrapper_t_swigregister(*args, **kwargs): ...
def edge_layout_point_t___eq__(self, r) -> bool: ...
def edge_layout_point_t___ne__(self, r) -> bool: ...
def edge_layout_point_t_compare(self, r) -> int: ...
def edge_layout_point_t_e_get(self) -> edge_t: ...
def edge_layout_point_t_e_set(self, e) -> Any: ...
def edge_layout_point_t_pidx_get(self) -> int: ...
def edge_layout_point_t_pidx_set(self, pidx) -> Any: ...
def edge_layout_point_t_swiginit(*args, **kwargs): ...
def edge_layout_point_t_swigregister(*args, **kwargs): ...
def edge_segment_t___lt__(self, r) -> bool: ...
def edge_segment_t_e_get(self) -> edge_t: ...
def edge_segment_t_e_set(self, e) -> Any: ...
def edge_segment_t_length(self) -> size_t: ...
def edge_segment_t_nseg_get(self) -> int: ...
def edge_segment_t_nseg_set(self, nseg) -> Any: ...
def edge_segment_t_swiginit(*args, **kwargs): ...
def edge_segment_t_swigregister(*args, **kwargs): ...
def edge_segment_t_toright(self) -> bool: ...
def edge_segment_t_x0_get(self) -> int: ...
def edge_segment_t_x0_set(self, x0) -> Any: ...
def edge_segment_t_x1_get(self) -> int: ...
def edge_segment_t_x1_set(self, x1) -> Any: ...
def edge_t___eq__(self, y) -> bool: ...
def edge_t___lt__(self, y) -> bool: ...
def edge_t___ne__(self, y) -> bool: ...
def edge_t_dst_get(self) -> int: ...
def edge_t_dst_set(self, dst) -> Any: ...
def edge_t_src_get(self) -> int: ...
def edge_t_src_set(self, src) -> Any: ...
def edge_t_swiginit(*args, **kwargs): ...
def edge_t_swigregister(*args, **kwargs): ...
def get_graph_viewer(*args, **kwargs): ...
def get_node_info(out, gid, node) -> bool: ...
def get_viewer_graph(gv) -> mutable_graph_t: ...
def graph_item_t_b_get(self) -> int: ...
def graph_item_t_b_set(self, b) -> Any: ...
def graph_item_t_e_get(self) -> edge_t: ...
def graph_item_t_e_set(self, e) -> Any: ...
def graph_item_t_elp_get(self) -> edge_layout_point_t: ...
def graph_item_t_elp_set(self, elp) -> Any: ...
def graph_item_t_is_edge(self) -> bool: ...
def graph_item_t_is_node(self) -> bool: ...
def graph_item_t_n_get(self) -> int: ...
def graph_item_t_n_set(self, n) -> Any: ...
def graph_item_t_p_get(self) -> point_t: ...
def graph_item_t_p_set(self, p) -> Any: ...
def graph_item_t_swiginit(*args, **kwargs): ...
def graph_item_t_swigregister(*args, **kwargs): ...
def graph_item_t_type_get(self) -> graph_item_type_t: ...
def graph_item_t_type_set(self, type) -> Any: ...
def graph_node_visitor_t_is_forbidden_edge(self, arg0, arg1) -> bool: ...
def graph_node_visitor_t_is_visited(self, n) -> bool: ...
def graph_node_visitor_t_reinit(self) -> Any: ...
def graph_node_visitor_t_set_visited(self, n) -> Any: ...
def graph_node_visitor_t_swiginit(*args, **kwargs): ...
def graph_node_visitor_t_swigregister(*args, **kwargs): ...
def graph_node_visitor_t_visit_node(self, arg0) -> int: ...
def graph_path_visitor_t_path_get(*args, **kwargs): ...
def graph_path_visitor_t_path_set(self, path) -> Any: ...
def graph_path_visitor_t_prune_get(self) -> bool: ...
def graph_path_visitor_t_prune_set(self, prune) -> Any: ...
def graph_path_visitor_t_swiginit(*args, **kwargs): ...
def graph_path_visitor_t_swigregister(*args, **kwargs): ...
def graph_path_visitor_t_walk_backward(self, arg0) -> int: ...
def graph_path_visitor_t_walk_forward(self, arg0) -> int: ...
def graph_visitor_t_swiginit(*args, **kwargs): ...
def graph_visitor_t_swigregister(*args, **kwargs): ...
def graph_visitor_t_visit_edge(self, arg2, arg3) -> int: ...
def graph_visitor_t_visit_node(self, arg2, arg3) -> int: ...
def group_crinfo_t_nodes_get(*args, **kwargs): ...
def group_crinfo_t_nodes_set(self, nodes) -> Any: ...
def group_crinfo_t_swiginit(*args, **kwargs): ...
def group_crinfo_t_swigregister(*args, **kwargs): ...
def group_crinfo_t_text_get(*args, **kwargs): ...
def group_crinfo_t_text_set(self, text) -> Any: ...
def interval_t___eq__(self, r) -> bool: ...
def interval_t___ne__(self, r) -> bool: ...
def interval_t_contains(self, x) -> bool: ...
def interval_t_empty(self) -> bool: ...
def interval_t_intersect(self, r) -> Any: ...
def interval_t_length(self) -> int: ...
def interval_t_make_union(self, r) -> Any: ...
def interval_t_move_by(self, shift) -> Any: ...
def interval_t_swiginit(*args, **kwargs): ...
def interval_t_swigregister(*args, **kwargs): ...
def interval_t_x0_get(self) -> int: ...
def interval_t_x0_set(self, x0) -> Any: ...
def interval_t_x1_get(self) -> int: ...
def interval_t_x1_set(self, x1) -> Any: ...
def mutable_graph_t_add_edge(self, i, j, ei) -> bool: ...
def mutable_graph_t_add_node(self, r) -> int: ...
def mutable_graph_t_belongs_get(*args, **kwargs): ...
def mutable_graph_t_belongs_set(self, belongs) -> Any: ...
def mutable_graph_t_calc_group_ea(self, arg2) -> ea_t: ...
def mutable_graph_t_change_group_visibility(self, group, expand) -> bool: ...
def mutable_graph_t_create_digraph_layout(self) -> bool: ...
def mutable_graph_t_create_group(self, nodes) -> int: ...
def mutable_graph_t_del_custom_layout(self) -> Any: ...
def mutable_graph_t_del_edge(self, i, j) -> bool: ...
def mutable_graph_t_del_node(self, n) -> ssize_t: ...
def mutable_graph_t_delete_group(self, group) -> bool: ...
def mutable_graph_t_edges_get(self) -> edge_infos_wrapper_t: ...
def mutable_graph_t_edges_set(self, edges) -> Any: ...
def mutable_graph_t_empty(self) -> bool: ...
def mutable_graph_t_exists(self, node) -> bool: ...
def mutable_graph_t_get_custom_layout(self) -> bool: ...
def mutable_graph_t_get_first_subgraph_node(self, group) -> int: ...
def mutable_graph_t_get_graph_groups(self) -> bool: ...
def mutable_graph_t_get_next_subgraph_node(self, group, current) -> int: ...
def mutable_graph_t_get_node_group(self, node) -> int: ...
def mutable_graph_t_get_node_representative(self, node) -> int: ...
def mutable_graph_t_gid_get(self) -> uval_t: ...
def mutable_graph_t_gid_set(self, gid) -> Any: ...
def mutable_graph_t_is_collapsed_node(self, node) -> bool: ...
def mutable_graph_t_is_deleted_node(self, node) -> bool: ...
def mutable_graph_t_is_displayable_node(self, node) -> bool: ...
def mutable_graph_t_is_dot_node(self, node) -> bool: ...
def mutable_graph_t_is_group_node(self, node) -> bool: ...
def mutable_graph_t_is_simple_node(self, node) -> bool: ...
def mutable_graph_t_is_subgraph_node(self, node) -> bool: ...
def mutable_graph_t_is_uncollapsed_node(self, node) -> bool: ...
def mutable_graph_t_is_user_graph(self) -> bool: ...
def mutable_graph_t_is_visible_node(self, node) -> bool: ...
def mutable_graph_t_node_flags_get(*args, **kwargs): ...
def mutable_graph_t_node_flags_set(self, node_flags) -> Any: ...
def mutable_graph_t_node_qty(self) -> int: ...
def mutable_graph_t_nodes_get(self) -> node_layout_t: ...
def mutable_graph_t_nodes_set(self, nodes) -> Any: ...
def mutable_graph_t_npred(self, b) -> int: ...
def mutable_graph_t_nsucc(self, b) -> int: ...
def mutable_graph_t_org_preds_get(*args, **kwargs): ...
def mutable_graph_t_org_preds_set(self, org_preds) -> Any: ...
def mutable_graph_t_org_succs_get(*args, **kwargs): ...
def mutable_graph_t_org_succs_set(self, org_succs) -> Any: ...
def mutable_graph_t_pred(self, b, i) -> int: ...
def mutable_graph_t_preds_get(*args, **kwargs): ...
def mutable_graph_t_preds_set(self, preds) -> Any: ...
def mutable_graph_t_predset(*args, **kwargs): ...
def mutable_graph_t_redo_layout(self) -> bool: ...
def mutable_graph_t_refresh(self) -> bool: ...
def mutable_graph_t_replace_edge(self, i, j, x, y) -> bool: ...
def mutable_graph_t_reset(self) -> Any: ...
def mutable_graph_t_resize(self, n) -> Any: ...
def mutable_graph_t_set_custom_layout(self) -> Any: ...
def mutable_graph_t_set_deleted_node(self, node) -> Any: ...
def mutable_graph_t_set_edge(self, e, ei) -> bool: ...
def mutable_graph_t_set_graph_groups(self) -> Any: ...
def mutable_graph_t_set_node_group(self, node, group) -> Any: ...
def mutable_graph_t_set_nrect(self, n, r) -> bool: ...
def mutable_graph_t_size(self) -> int: ...
def mutable_graph_t_succ(self, b, i) -> int: ...
def mutable_graph_t_succs_get(*args, **kwargs): ...
def mutable_graph_t_succs_set(self, succs) -> Any: ...
def mutable_graph_t_succset(*args, **kwargs): ...
def mutable_graph_t_swigregister(*args, **kwargs): ...
def new_TPointDouble(r) -> TPointDouble: ...
def new_abstract_graph_t(_self) -> abstract_graph_t: ...
def new_edge_info_t() -> edge_info_t: ...
def new_edge_layout_point_t(_e, _pidx) -> edge_layout_point_t: ...
def new_edge_segment_t() -> edge_segment_t: ...
def new_edge_t(x, y) -> edge_t: ...
def new_graph_item_t() -> graph_item_t: ...
def new_graph_node_visitor_t(_self) -> graph_node_visitor_t: ...
def new_graph_path_visitor_t(_self) -> graph_path_visitor_t: ...
def new_graph_visitor_t(_self) -> graph_visitor_t: ...
def new_group_crinfo_t() -> group_crinfo_t: ...
def new_interval_t(s) -> interval_t: ...
def new_node_info_t() -> node_info_t: ...
def new_node_layout_t(x) -> node_layout_t: ...
def new_node_ordering_t() -> node_ordering_t: ...
def new_point_t(_x, _y) -> point_t: ...
def new_pointseq_t() -> pointseq_t: ...
def new_pointvec_t(x) -> pointvec_t: ...
def new_rect_t(p0, p1) -> rect_t: ...
def new_row_info_t() -> row_info_t: ...
def new_screen_graph_selection_base_t(x) -> screen_graph_selection_base_t: ...
def new_screen_graph_selection_t() -> screen_graph_selection_t: ...
def new_selection_item_t(e, idx) -> selection_item_t: ...
def node_info_t_bg_color_get(self) -> bgcolor_t: ...
def node_info_t_bg_color_set(self, bg_color) -> Any: ...
def node_info_t_ea_get(self) -> ea_t: ...
def node_info_t_ea_set(self, ea) -> Any: ...
def node_info_t_flags_get(self) -> uint32: ...
def node_info_t_flags_set(self, flags) -> Any: ...
def node_info_t_frame_color_get(self) -> bgcolor_t: ...
def node_info_t_frame_color_set(self, frame_color) -> Any: ...
def node_info_t_get_flags_for_valid(self) -> uint32: ...
def node_info_t_swiginit(*args, **kwargs): ...
def node_info_t_swigregister(*args, **kwargs): ...
def node_info_t_text_get(*args, **kwargs): ...
def node_info_t_text_set(self, text) -> Any: ...
def node_info_t_valid_bg_color(self) -> bool: ...
def node_info_t_valid_ea(self) -> bool: ...
def node_info_t_valid_flags(self) -> bool: ...
def node_info_t_valid_frame_color(self) -> bool: ...
def node_info_t_valid_text(self) -> bool: ...
def node_layout_t___eq__(self, r) -> bool: ...
def node_layout_t___getitem__(self, i) -> rect_t: ...
def node_layout_t___len__(self) -> size_t: ...
def node_layout_t___ne__(self, r) -> bool: ...
def node_layout_t___setitem__(self, i, v) -> Any: ...
def node_layout_t__del(self, x) -> bool: ...
def node_layout_t_add_unique(self, x) -> bool: ...
def node_layout_t_at(self, _idx) -> rect_t: ...
@overload
def node_layout_t_begin(self) -> rect_t: ...
@overload
def node_layout_t_begin(self) -> rect_t: ...
def node_layout_t_capacity(self) -> size_t: ...
def node_layout_t_clear(self) -> Any: ...
def node_layout_t_empty(self) -> bool: ...
@overload
def node_layout_t_end(self) -> rect_t: ...
@overload
def node_layout_t_end(self) -> rect_t: ...
@overload
def node_layout_t_erase(self, it) -> rect_t: ...
@overload
def node_layout_t_erase(self, first, last) -> rect_t: ...
def node_layout_t_extract(self) -> rect_t: ...
@overload
def node_layout_t_find(self, x) -> rect_t: ...
@overload
def node_layout_t_find(self, x) -> rect_t: ...
def node_layout_t_grow(self, x=...) -> Any: ...
def node_layout_t_has(self, x) -> bool: ...
def node_layout_t_inject(self, s, len) -> Any: ...
def node_layout_t_insert(self, it, x) -> rect_t: ...
def node_layout_t_pop_back(self) -> Any: ...
@overload
def node_layout_t_push_back(self, x) -> Any: ...
@overload
def node_layout_t_push_back(self) -> rect_t: ...
def node_layout_t_qclear(self) -> Any: ...
def node_layout_t_reserve(self, cnt) -> Any: ...
@overload
def node_layout_t_resize(self, _newsize, x) -> Any: ...
@overload
def node_layout_t_resize(self, _newsize) -> Any: ...
def node_layout_t_size(self) -> size_t: ...
def node_layout_t_swap(self, r) -> Any: ...
def node_layout_t_swiginit(*args, **kwargs): ...
def node_layout_t_swigregister(*args, **kwargs): ...
def node_layout_t_truncate(self) -> Any: ...
def node_ordering_t_clear(self) -> Any: ...
def node_ordering_t_clr(self, _node) -> bool: ...
def node_ordering_t_node(self, _order) -> int: ...
def node_ordering_t_order(self, _node) -> int: ...
def node_ordering_t_resize(self, n) -> Any: ...
def node_ordering_t_set(self, _node, num) -> Any: ...
def node_ordering_t_size(self) -> size_t: ...
def node_ordering_t_swiginit(*args, **kwargs): ...
def node_ordering_t_swigregister(*args, **kwargs): ...
def point_t___eq__(self, r) -> bool: ...
def point_t___ne__(self, r) -> bool: ...
def point_t_add(self, r) -> point_t: ...
def point_t_negate(self) -> Any: ...
def point_t_sub(self, r) -> point_t: ...
def point_t_swiginit(*args, **kwargs): ...
def point_t_swigregister(*args, **kwargs): ...
def point_t_x_get(self) -> int: ...
def point_t_x_set(self, x) -> Any: ...
def point_t_y_get(self) -> int: ...
def point_t_y_set(self, y) -> Any: ...
def pointseq_t_swiginit(*args, **kwargs): ...
def pointseq_t_swigregister(*args, **kwargs): ...
def pointvec_t___eq__(self, r) -> bool: ...
def pointvec_t___getitem__(self, i) -> point_t: ...
def pointvec_t___len__(self) -> size_t: ...
def pointvec_t___ne__(self, r) -> bool: ...
def pointvec_t___setitem__(self, i, v) -> Any: ...
def pointvec_t__del(self, x) -> bool: ...
def pointvec_t_add_unique(self, x) -> bool: ...
def pointvec_t_at(self, _idx) -> point_t: ...
@overload
def pointvec_t_begin(self) -> point_t: ...
@overload
def pointvec_t_begin(self) -> point_t: ...
def pointvec_t_capacity(self) -> size_t: ...
def pointvec_t_clear(self) -> Any: ...
def pointvec_t_empty(self) -> bool: ...
@overload
def pointvec_t_end(self) -> point_t: ...
@overload
def pointvec_t_end(self) -> point_t: ...
@overload
def pointvec_t_erase(self, it) -> point_t: ...
@overload
def pointvec_t_erase(self, first, last) -> point_t: ...
def pointvec_t_extract(self) -> point_t: ...
@overload
def pointvec_t_find(self, x) -> point_t: ...
@overload
def pointvec_t_find(self, x) -> point_t: ...
def pointvec_t_grow(self, x=...) -> Any: ...
def pointvec_t_has(self, x) -> bool: ...
def pointvec_t_inject(self, s, len) -> Any: ...
def pointvec_t_insert(self, it, x) -> point_t: ...
def pointvec_t_pop_back(self) -> Any: ...
@overload
def pointvec_t_push_back(self, x) -> Any: ...
@overload
def pointvec_t_push_back(self) -> point_t: ...
def pointvec_t_qclear(self) -> Any: ...
def pointvec_t_reserve(self, cnt) -> Any: ...
@overload
def pointvec_t_resize(self, _newsize, x) -> Any: ...
@overload
def pointvec_t_resize(self, _newsize) -> Any: ...
def pointvec_t_size(self) -> size_t: ...
def pointvec_t_swap(self, r) -> Any: ...
def pointvec_t_swiginit(*args, **kwargs): ...
def pointvec_t_swigregister(*args, **kwargs): ...
def pointvec_t_truncate(self) -> Any: ...
def pyg_close(_self) -> Any: ...
def pyg_select_node(_self, nid) -> Any: ...
def pyg_show(_self) -> bool: ...
def rect_t___eq__(self, r) -> bool: ...
def rect_t___ne__(self, r) -> bool: ...
def rect_t_area(self) -> int: ...
def rect_t_bottom_get(self) -> int: ...
def rect_t_bottom_set(self, bottom) -> Any: ...
def rect_t_bottomright(self) -> point_t: ...
def rect_t_center(self) -> point_t: ...
def rect_t_contains(self, p) -> bool: ...
def rect_t_empty(self) -> bool: ...
def rect_t_grow(self, delta) -> Any: ...
def rect_t_height(self) -> int: ...
def rect_t_intersect(self, r) -> Any: ...
def rect_t_is_intersection_empty(self, r) -> bool: ...
def rect_t_left_get(self) -> int: ...
def rect_t_left_set(self, left) -> Any: ...
def rect_t_make_union(self, r) -> Any: ...
def rect_t_move_by(self, p) -> Any: ...
def rect_t_move_to(self, p) -> Any: ...
def rect_t_right_get(self) -> int: ...
def rect_t_right_set(self, right) -> Any: ...
def rect_t_swiginit(*args, **kwargs): ...
def rect_t_swigregister(*args, **kwargs): ...
def rect_t_top_get(self) -> int: ...
def rect_t_top_set(self, top) -> Any: ...
def rect_t_topleft(self) -> point_t: ...
def rect_t_width(self) -> int: ...
def refresh_viewer(gv) -> Any: ...
def row_info_t_bottom_get(self) -> int: ...
def row_info_t_bottom_set(self, bottom) -> Any: ...
def row_info_t_height(self) -> int: ...
def row_info_t_nodes_get(*args, **kwargs): ...
def row_info_t_nodes_set(self, nodes) -> Any: ...
def row_info_t_swiginit(*args, **kwargs): ...
def row_info_t_swigregister(*args, **kwargs): ...
def row_info_t_top_get(self) -> int: ...
def row_info_t_top_set(self, top) -> Any: ...
def screen_graph_selection_base_t___eq__(self, r) -> bool: ...
def screen_graph_selection_base_t___getitem__(self, i) -> selection_item_t: ...
def screen_graph_selection_base_t___len__(self) -> size_t: ...
def screen_graph_selection_base_t___ne__(self, r) -> bool: ...
def screen_graph_selection_base_t___setitem__(self, i, v) -> Any: ...
def screen_graph_selection_base_t__del(self, x) -> bool: ...
def screen_graph_selection_base_t_add_unique(self, x) -> bool: ...
def screen_graph_selection_base_t_at(self, _idx) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_begin(self) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_begin(self) -> selection_item_t: ...
def screen_graph_selection_base_t_capacity(self) -> size_t: ...
def screen_graph_selection_base_t_clear(self) -> Any: ...
def screen_graph_selection_base_t_empty(self) -> bool: ...
@overload
def screen_graph_selection_base_t_end(self) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_end(self) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_erase(self, it) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_erase(self, first, last) -> selection_item_t: ...
def screen_graph_selection_base_t_extract(self) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_find(self, x) -> selection_item_t: ...
@overload
def screen_graph_selection_base_t_find(self, x) -> selection_item_t: ...
def screen_graph_selection_base_t_grow(self, x=...) -> Any: ...
def screen_graph_selection_base_t_has(self, x) -> bool: ...
def screen_graph_selection_base_t_inject(self, s, len) -> Any: ...
def screen_graph_selection_base_t_insert(self, it, x) -> selection_item_t: ...
def screen_graph_selection_base_t_pop_back(self) -> Any: ...
@overload
def screen_graph_selection_base_t_push_back(self, x) -> Any: ...
@overload
def screen_graph_selection_base_t_push_back(self) -> selection_item_t: ...
def screen_graph_selection_base_t_qclear(self) -> Any: ...
def screen_graph_selection_base_t_reserve(self, cnt) -> Any: ...
@overload
def screen_graph_selection_base_t_resize(self, _newsize, x) -> Any: ...
@overload
def screen_graph_selection_base_t_resize(self, _newsize) -> Any: ...
def screen_graph_selection_base_t_size(self) -> size_t: ...
def screen_graph_selection_base_t_swap(self, r) -> Any: ...
def screen_graph_selection_base_t_swiginit(*args, **kwargs): ...
def screen_graph_selection_base_t_swigregister(*args, **kwargs): ...
def screen_graph_selection_base_t_truncate(self) -> Any: ...
def screen_graph_selection_t_add(self, s) -> Any: ...
def screen_graph_selection_t_add_node(self, node) -> Any: ...
def screen_graph_selection_t_add_point(self, e, idx) -> Any: ...
def screen_graph_selection_t_del_node(self, node) -> Any: ...
def screen_graph_selection_t_del_point(self, e, idx) -> Any: ...
def screen_graph_selection_t_has(self, item) -> bool: ...
def screen_graph_selection_t_items_count(self, look_for_nodes) -> size_t: ...
def screen_graph_selection_t_nodes_count(self) -> size_t: ...
def screen_graph_selection_t_points_count(self) -> size_t: ...
def screen_graph_selection_t_sub(self, s) -> Any: ...
def screen_graph_selection_t_swiginit(*args, **kwargs): ...
def screen_graph_selection_t_swigregister(*args, **kwargs): ...
def selection_item_t___eq__(self, r) -> bool: ...
def selection_item_t___lt__(self, r) -> bool: ...
def selection_item_t___ne__(self, r) -> bool: ...
def selection_item_t_compare(self, r) -> int: ...
def selection_item_t_elp_get(self) -> edge_layout_point_t: ...
def selection_item_t_elp_set(self, elp) -> Any: ...
def selection_item_t_is_node_get(self) -> bool: ...
def selection_item_t_is_node_set(self, is_node) -> Any: ...
def selection_item_t_node_get(self) -> int: ...
def selection_item_t_node_set(self, node) -> Any: ...
def selection_item_t_swiginit(*args, **kwargs): ...
def selection_item_t_swigregister(*args, **kwargs): ...
def set_node_info(gid, node, ni, flags) -> Any: ...
def set_viewer_graph(gv, g) -> Any: ...
def user_graph_place_t_node_get(self) -> int: ...
def user_graph_place_t_node_set(self, node) -> Any: ...
def user_graph_place_t_swigregister(*args, **kwargs): ...
def viewer_attach_menu_item(g, name) -> bool: ...
def viewer_center_on(gv, node) -> Any: ...
def viewer_create_groups(gv, out_group_nodes, gi) -> bool: ...
def viewer_del_node_info(gv, n) -> Any: ...
def viewer_delete_groups(gv, groups, new_current=...) -> bool: ...
def viewer_fit_window(gv) -> Any: ...
def viewer_get_curnode(gv) -> int: ...
def viewer_get_gli(out, gv, flags=...) -> bool: ...
def viewer_get_node_info(gv, out, n) -> bool: ...
def viewer_get_selection(gv, sgs) -> bool: ...
def viewer_set_gli(gv, gli, flags=...) -> Any: ...
def viewer_set_groups_visibility(gv, groups, expand, new_current=...) -> bool: ...
def viewer_set_node_info(gv, n, ni, flags) -> Any: ...
def viewer_set_titlebar_height(gv, height) -> int: ...