"""
Black Jack simulator by Suryaa Kumara Relan

Instructions:
step 1: open Terminal or Cmd 
step 2: navigate to the directory which holds both black_jack.py and play_game.py
step 3: run play_game.py

"""

import random
import copy


class black_jack():
	'''
	class who's object would be used to simulate game
	'''
	def __init__(self):
		kinds = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		house = ['Spades','Hearts','Clubs','Dimonds']
		self.cards = [h+'_'+k for h in house for k in kinds]
		self.game_state = 0 # 0 for player0 and 1 for player1		
		self.player0 = []
		self.player1 = []
		self.player0_active = True
		self.player1_active = True
		self.i = 0

	def shuffle(self):
		'''
		Shuffles the cards
			Args: None
			Returns: None
		'''
		random.shuffle(self.cards)

	def hit(self):
		'''
		assign the card to the active player
			Args: None
			Returns: None
		'''
		holder = self.cards[self.i]
		self.i += 1

		if self.game_state == 0 and self.player0_active:
			self.player0.append(holder)
		elif self.game_state == 1 and self.player1_active:
			self.player1.append(holder)

		self.cards.remove(holder)

	def stay(self):
		'''
		simulates a stay 
			Args: None
			Returns: None
		'''
		if self.game_state == 0:
			self.player0_active = False
		elif self.game_state == 1:
			self.player1_active = False
	
	def is_game_active(self):
		'''
		Lets us know the status of the game
			Args: None
			Returns: bool
		'''
		return True if self.player1_active or self.player0_active else False	

	def current_player_value(self):
		'''
		Tells us the value of current player
			Args: None
			Returns: int
		'''	
		number_of_aces = 0
		current_sum = 0
		if self.game_state == 0:
			p = copy.copy(self.player0)
		else:
			p = copy.copy(self.player1)

		p = [ n.split('_')[1] for n in p]
		
		for card in p:
			if card.isdigit():
				current_sum += int(card)
			else:
				if card in ['K','Q','J']:
					current_sum += 10
				else:
					number_of_aces += 1

		while number_of_aces > 0:
			number_of_aces -= 1
			if current_sum+11 <= 21 - number_of_aces:
				current_sum+= 11
			else:
				current_sum += 1

		return current_sum

	def show_player_hand(self):
		'''
		shows current players hand
			Args: None
			Returns: str
		'''
		if self.game_state == 0:
			p = copy.copy(self.player0)
		else:
			p = copy.copy(self.player1)
		return "player{0} has hand: {1}".format(self.game_state,p)

	def _change_player_state(self):
		'''
		changes active player
			Args: None
			Returns: None
		'''
		if self.game_state == 0:
			self.game_state = 1
		else:
			self.game_state = 0


def play_game():
	final_result = [0,0]
	game = black_jack()
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