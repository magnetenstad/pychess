
var _board = argument0
var _depth = argument1 - 1
var _turn = argument2 + 1

var _w = ds_grid_width(_board)
var _h = ds_grid_height(_board)

var _board_other = ds_grid_create(_w, _h)
var _value = undefined

for (var _x = 0; _x < _w; ++_x)
{
	for (var _y = 0; _y < _h; ++_y)
	{
		var _tile = _board[# _x, _y]
		
		if _tile != -1 and _tile[tile.color] != _turn mod 2
		{
			var _moves = tile_get_moves(_board, _x, _y)
			var _size = ds_list_size(_moves)
			
			for (var i = 0; i < _size; ++i)
			{
				ds_grid_copy(_board_other, _board)
				
				var _move = _moves[| i]
					
				tile_move(_board_other, _x, _y, _move[0], _move[1])
				
				var _eval_move = board_eval_move(_board_other, _x, _y, _move[0], _move[1])
				
				if _depth > 0 { var _eval = board_eval_next(_board_other, _depth, _turn) }
				else { var _eval = [[_x, _y, _move[0], _move[1]], _eval_move] }
				
				if _value == undefined
				or (_turn mod 2 and _eval[1] < _value[1])
				or ((_turn + 1) mod 2 and _eval[1] > _value[1])
				{
					_value = [[_x, _y, _move[0], _move[1]], _eval[1]]
				}
			}
		}
		
		if _depth = 2 { show_debug_message(100*(_h*_x + _y)/(_w*_h)) }
	}
}

ds_grid_destroy(_board_other)

return _value
