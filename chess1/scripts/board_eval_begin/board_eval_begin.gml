
var _board = argument0

var _w = 8
var _h = 8

for (var _x = 0; _x < _w; ++_x)
{
	for (var _y = 0; _y < _h; ++_y)
	{
		var _tile = _board[# _x, _y]
		
		if _tile != -1
		{
			_tile[tile.value] = tile_eval(_board, _x, _y, _tile)
			
			_board[# _x, _y] = _tile
		}
	}
}
