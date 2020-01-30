
var _board = argument0
var _x = argument1
var _y = argument2

if _x < 0 or 8 <= _x { return undefined } //ds_grid_width(_board) <= _x { return undefined }
if _y < 0 or 8 <= _y { return undefined } //ds_grid_height(_board) <= _y { return undefined }

var _tile = _board[# _x, _y]

if _tile != -1
{
	return _tile[tile.color]
}

return -1
