"""
Black Jack simulator by Suryaa Kumara Relan

Instructions:
step 1: open Terminal or Cmd 
step 2: navigate to the directory which holds both black_jack.py and play_game.py
step 3: run play_game.py

To play:
> In the start the game runs and gives each player 2 cards
> Players procced in turn basis to either Hit or Stay
> One round of the game ends when either 1) both users say Stay, 2) One user gets busted.
> The winner is decided by seeing the total value of cards held by a user (if neither is busted).
> If one user gets busted the other wins.
"""

import black_jack


def play_game():
	'''
	Contains and Executes the logic of the game.
		Args: none
		Returns: str
	'''
	final_result = [0,0]
	game = black_jack.Game_class()
	game.shuffle()
	for s in range(0,4):
		game.hit()
		game._change_player_state()
	
	print game.show_player_hand()
	game._change_player_state()
	print game.show_player_hand()
	game._change_player_state()

	while game.is_game_active():
		user_input = ''
		if game.game_state == 0 and not game.player0_active:
			game._change_player_state()
			continue
		if game.game_state == 1 and not game.player1_active:
			game._change_player_state()
			continue

		while user_input == '':
			user_input = raw_input(
				"Does player{0} want to hit(h)/stay(s) ?".format(
				game.game_state))
			if not user_input in ['s','h','S','H']:
				user_input = ''
		if user_input.lower() == 'h':
			game.hit()
			print game.show_player_hand()
			value = game.current_player_value()
			if value > 21:
				print(
					"player{} has BUST! Game Over".format(
					game.game_state))
				game._change_player_state()
				return "player{0} wins!".format(game.game_state)
		else:
			game.stay()
		game._change_player_state()
	
	final_result[game.game_state] = game.current_player_value()
	game._change_player_state()
	final_result[game.game_state] = game.current_player_value()

	if final_result[0]>final_result[1]:
		return 'player0 wins'
	elif final_result[0]<final_result[1]:
		return 'player1 wins'
	else:
		return "draw"


if __name__ == '__main__':

	user_input = ''
	while user_input =='':
		print play_game()
		user_input = raw_input('Do you want to play again? enter y to continue:')
		if user_input.lower() == 'y':
			user_input = ''