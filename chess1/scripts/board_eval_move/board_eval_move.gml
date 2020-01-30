
var _board = argument0
var _move_x0 = argument1
var _move_y0 = argument2
var _move_x = argument3
var _move_y = argument4

var _w = 8
var _h = 8
var _value = 0

var _dx = [-1, -1, 1, 1, -1, 1, 0, 0]
var _dy = [-1, 1, -1, 1, 0, 0, -1, 1]

for (var i = 0; i < 8; ++i)
{
	for (var j = 1; j <= 7; ++j)
	{
		var _x = _move_x0 + _dx[i] * j;
		var _y = _move_y0 + _dy[i] * j;
		
		if _x < 0 or 8 <= _x { break }
		if _y < 0 or 8 <= _y { break }
		
		var _tile = _board[# _x, _y]
		
		if _tile != -1
		{	
			_tile[tile.value] = tile_eval(_board, _x, _y, _tile)
			
			_board[# _x, _y] = _tile
			
			break
		}
	}
	for (var j = 1; j <= 7; ++j)
	{
		var _x = _move_x + _dx[i] * j;
		var _y = _move_y + _dy[i] * j;
		
		if _x < 0 or 8 <= _x { break }
		if _y < 0 or 8 <= _y { break }
		
		var _tile = _board[# _x, _y]
		
		if _tile != -1
		{
			_tile[tile.value] = tile_eval(_board, _x, _y, _tile)
			
			_board[# _x, _y] = _tile
			
			break
		}
	}
}

for (var _x = 0; _x < _w; ++_x)
{
	for (var _y = 0; _y < _h; ++_y)
	{
		var _tile = _board[# _x, _y]
		
		if _tile != -1
		{
			if _tile[tile.piece] == piece.knight
			{
				_tile[tile.value] = tile_eval(_board, _x, _y, _tile)
				
				_board[# _x, _y] = _tile
			}
			
			_value += _tile[tile.value]
		}
	}
}

return _value
