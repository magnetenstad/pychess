
randomize()

value = ds_list_create()

value[| piece.pawn] = 1
value[| piece.knight] = 3
value[| piece.bishop] = 3
value[| piece.rook] = 5
value[| piece.queen] = 9
value[| piece.king] = 5

board_w = 8
board_h = 8

tile_size = 64

board = ds_grid_create(board_w, board_h)

ds_grid_clear(board, -1)

board_reset()

view_enabled = true
view_visible = true

var _width = (board_w + 2) * tile_size
var _height = board_h * tile_size

camera_set_view_size(view_camera[0], _width, _height)
window_set_size(_width, _height)
surface_resize(application_surface, _width, _height)

turn = 1

tile_select = -1
play_move = false
