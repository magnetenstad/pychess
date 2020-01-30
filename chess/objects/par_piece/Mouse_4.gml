ds_grid_clear(global.board_options, 0)
global.selected_x = tile_x
global.selected_y = tile_y
if piece_type = "pawn" {
	if ds_grid_get(global.board, tile_x, tile_y - 1) = 0 ds_grid_set(global.board_options, tile_x, tile_y - 1, 1)
	if not moved {
		ds_grid_set(global.board_options, tile_x, tile_y - 2, 1)
	}
}