
var _color = color.white
var _board = obj_game.board

for (var i = 0; i < 2; ++i)
{
    tile_set(_board, 0, i*7, _color, piece.rook)
	tile_set(_board, 1, i*7, _color, piece.knight)
	tile_set(_board, 2, i*7, _color, piece.bishop)
	tile_set(_board, 4, i*7, _color, piece.queen)
	tile_set(_board, 3, i*7, _color, piece.king)
	tile_set(_board, 5, i*7, _color, piece.bishop)
	tile_set(_board, 6, i*7, _color, piece.knight)
	tile_set(_board, 7, i*7, _color, piece.rook)
	
	for (var j = 0; j < 8; ++j)
	{
		tile_set(_board, j, 1 + i*5, _color, piece.pawn)
	}
	
	_color = color.black
}

board_eval_begin(obj_game.board)
