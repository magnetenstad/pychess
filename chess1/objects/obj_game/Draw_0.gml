
for (var _x = 0; _x < board_w; _x += 2)
{
	for (var _y = 0; _y < board_h; _y += 2)
	{
		draw_sprite(spr_tile, 0, _x * tile_size, _y * tile_size)
	}
}

for (var _x = 0; _x < board_w; ++_x)
{
	for (var _y = 0; _y < board_h; ++_y)
	{
		var _tile = board[# _x, _y]
		
		if _tile != -1 and _tile != undefined
		{
			draw_sprite_ext(spr_piece, _tile[tile.piece] + 6 * _tile[tile.color], _x * tile_size, _y * tile_size, 4, 4, 0, c_white, 1)
		}
	}
}

//draw_text(board_w * tile_size , 32, "EVAL: " + string(board_eval(obj_game.board)))

if mouse_check_button_pressed(mb_left)
{
	var _x = floor(mouse_x/tile_size)
	var _y = floor(mouse_y/tile_size)
	
	if tile_select == -1
	{
		tile_select = [_x, _y]
	}
	else
	{
		if _x == tile_select[0] and _y == tile_select[1]
		{
			tile_select = -1
		}
	}
	
	if tile_select != -1
	{
		var _moves = tile_get_moves(board, tile_select[0], tile_select[1])
		var _size = ds_list_size(_moves)
		
		for (var i = 0; i < _size; ++i)
		{
			var _move = _moves[| i]
		
			if _x == _move[0] and _y == _move[1]
			{
				tile_move(board, tile_select[0], tile_select[1], _x, _y)
				tile_select = -1
				turn += 1
				play_move = true
			}
		}
		
		ds_list_destroy(_moves)
	}
}

if tile_select != -1
{
	var _moves = tile_get_moves(board, tile_select[0], tile_select[1])
	var _size = ds_list_size(_moves)

	for (var i = 0; i < _size; ++i)
	{
		var _move = _moves[| i]
	
		draw_circle((_move[0] + 0.5) * tile_size, (_move[1] + 0.5) * tile_size, 4, false)
	}
	
	ds_list_destroy(_moves)
}
