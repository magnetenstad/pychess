
if keyboard_check_pressed(vk_space) or play_move
{
	var _eval = board_eval_next(obj_game.board, 3, turn)
	var _move = _eval[0]
	
	show_debug_message("TURN: " + string(turn) + ", EVAL:" + string(_eval[1]))
	
	tile_move(obj_game.board, _move[0], _move[1], _move[2], _move[3])
	
	turn += 1
	play_move = false
}
