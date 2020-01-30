room_speed = 60

draw_set_font(font0)

global.board_update = true
global.selected_x = -1
global.selected_y = -1
global.tile_width = 16
global.tile_height = 16
global.grid_width = 8
global.grid_height = 8
global.board = ds_grid_create(global.grid_width, global.grid_height)
global.board_options = ds_grid_create(global.grid_width, global.grid_height)