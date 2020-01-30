for (var a = 0; a < global.grid_width; a++) {
	for (var b = 0; b < global.grid_height; b++) {
		if ds_grid_get(global.board_options, a, b) draw_sprite(sprite15, 0, a*global.tile_width, b*global.tile_height)
	}
}
if global.selected_x draw_sprite(sprite12, 0, global.selected_x*global.tile_width, global.selected_y*global.tile_height)