
var _board = argument0
var _x = argument1
var _y = argument2
if _x < 0 or ds_grid_width(_board) <= _x { return ds_list_create() }
if _y < 0 or ds_grid_height(_board) <= _y { return ds_list_create() }

var _tile = _board[# _x, _y]
var _moves = ds_list_create()

if _tile != -1 and _tile != undefined
{
	var _color = _tile[tile.color]
	
	switch _tile[tile.piece]
	{
		case piece.pawn:
			
			var _y1 = _y - (1 - 2 * _color)
			
			if tile_get_color(_board, _x, _y1) == -1
			{
				ds_list_add(_moves, [_x, _y1])
				
				if _color == color.white and _y == 1
				and tile_get_color(_board, _x, 3) == -1
				{
					ds_list_add(_moves, [_x, 3])
				}
			
				if _color == color.black and _y == 6
				and tile_get_color(_board, _x, 4) == -1
				{
					ds_list_add(_moves, [_x, 4])
				}
			}
			
			var col_p = tile_get_color(_board, _x + 1, _y1)
			var col_n = tile_get_color(_board, _x - 1, _y1)
			
			if col_p != -1 and col_p != undefined and col_p != _color
			{
				ds_list_add(_moves, [_x + 1, _y1])
			}
			
			if col_n != -1 and col_n != undefined and col_n != _color
			{
				ds_list_add(_moves, [_x - 1, _y1])
			}
			
			break
		
		case piece.knight:

			add_moves(_board, _x, _y, _color, _moves, [-1, 1, 2, 2, 1, -1, -2, -2], [-2, -2, -1, 1, 2, 2, 1, -1], 8, 1)
			
			break
		
		case piece.bishop:

			add_moves(_board, _x, _y, _color, _moves, [-1, -1, 1, 1], [-1, 1, -1, 1], 4, 7)
			
			break
		
		case piece.rook:

			add_moves(_board, _x, _y, _color, _moves, [-1, 1, 0, 0], [0, 0, -1, 1], 4, 7)
			
			break
		
		case piece.queen:

			add_moves(_board, _x, _y, _color, _moves, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 7)
			
			break
			
		case piece.king:

			add_moves(_board, _x, _y, _color, _moves, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 1)
			
			break
	}
}

return _moves
