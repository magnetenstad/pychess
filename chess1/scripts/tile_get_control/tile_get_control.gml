
var _board = argument0
var _x = argument1
var _y = argument2
var _tile = _board[# _x, _y]
var _moves = 0

if _tile != -1 and _tile != undefined
{
	var _color = _tile[tile.color]

	switch _tile[tile.piece]
	{
		case piece.pawn:
			
			var _y1 = _y - (1 - 2 * _color)
			
			var _color_other = tile_get_color(_board, _x + 1, _y1)
			
			if _color_other != _color and _color_other != undefined
			{
				_moves++
			}
			
			var _color_other = tile_get_color(_board, _x - 1, _y1)
			
			if _color_other != _color and _color_other != undefined
			{
				_moves++
			}
			
			break
		
		case piece.knight:

			_moves += move_count(_board, _x, _y, _color, [-1, 1, 2, 2, 1, -1, -2, -2], [-2, -2, -1, 1, 2, 2, 1, -1], 8, 1)
			
			break
		
		case piece.bishop:

			_moves += move_count(_board, _x, _y, _color, [-1, -1, 1, 1], [-1, 1, -1, 1], 4, 7)
			
			break
		
		case piece.rook:

			_moves += move_count(_board, _x, _y, _color, [-1, 1, 0, 0], [0, 0, -1, 1], 4, 7)
			
			break
		
		case piece.queen:

			_moves += move_count(_board, _x, _y, _color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 7)
			
			break
			
		case piece.king:

			_moves += move_count(_board, _x, _y, _color, [-1, -1, 1, 1, -1, 1, 0, 0], [-1, 1, -1, 1, 0, 0, -1, 1], 8, 1)
			
			break
	}
}

return _moves
