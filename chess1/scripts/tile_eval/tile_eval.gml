
var _board = argument0
var _x = argument1
var _y = argument2
var _tile = argument3

var _value = 0
var _color = _tile[tile.color]
var _piece = _tile[tile.piece]

_value -= obj_game.value[| _piece] * (1 - 2 * _color)

_value -= (0.08 - 0.1 * (_piece == piece.queen) - 0.1 * (_piece == piece.king)) * tile_get_control(_board, _x, _y) * (1 - 2 * _color)

if _piece == piece.pawn { _value += 0.05 * (_y - 3.5) + 0.08 * point_distance(_x, _y, 3.5, 3.5) * (1 - 2 * _color) }

return _value
