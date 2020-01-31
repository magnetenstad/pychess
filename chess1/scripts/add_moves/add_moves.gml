var _board = argument0
var _x = argument1
var _y = argument2
var _color = argument3
var _moves = argument4
var _dx = argument5
var _dy = argument6
var _dlen = argument7
var _len = argument8

for (var i = 0; i < _dlen; ++i)
{
	for (var j = 1; j <= _len; ++j)
	{
		var _x1 = _x + _dx[i] * j
		var _y1 = _y + _dy[i] * j
		
		if _x1 < 0 or 8 <= _x1 { break }
		if _y1 < 0 or 8 <= _y1 { break }
		
		var _tile = _board[# _x1, _y1]

		if _tile == -1 or _tile[tile.color] != _color { ds_list_add(_moves, [_x1, _y1]) }

		if _tile != -1 { break }
	}
}
