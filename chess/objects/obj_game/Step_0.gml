if global.board_update {
	with par_piece {
		ds_grid_clear(global.board, 0)
		tile_x = x/global.tile_width
		tile_y = y/global.tile_height
		ds_grid_set(global.board, tile_x, tile_y, self)
	}
	global.board_update = false
}
