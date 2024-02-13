"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os
from copy import deepcopy
import time	#imports the time module which allows us to delay the program
## to run: type python3 main.py into the terminal


'''
HELPER FUNCTIONS
The following 4 functions (horizontal_win,vertical_win,diagonal_up_win and diagonal_down_win) are functions that are used in the end_of_game function
'''

def check_for_win(board,player):

	"""
	Makes a copy of the board and simulates all the possible moves, until a winning move is found. 
	Then returns which column results in a winning move. 
	If there are no possible winning moves, return 0
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:param player: The current player who will be placing the pieces in the simulation
	:return: 0 if no possible winning moves, 1-7 if there is a possible winning column
	"""


	list_of_boards = []

	for column_check in range(len(board[0])):
		list_of_boards.append(deepcopy(board))
		
		drop_success = drop_piece(list_of_boards[column_check],player,column_check)

		if drop_success == True:
			#print_board(list_of_boards[column_check])
			if end_of_game(list_of_boards[column_check])== 1 or end_of_game(list_of_boards[column_check])==2:
				# that's a win 
				return column_check

	return 0


def horizontal_win(board):
	"""
	Checks if a horizontal - win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	for row in range(6): # check every row
		for starting_col in range(4): 
			# start from the LHS of the board and then move across by one column with each iteration
			if board[row][starting_col] == board[row][starting_col+1] == board[row][starting_col+2] == board[row][starting_col+3]!=0:
				# 4 in a row, player wins 
				winner = board[row][starting_col]
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0 

def vertical_win(board):
	"""
	Checks if a verical | win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	for col in range(7): # check every column
		for starting_row in range(3): # start at top row and shift down one with each iteration
			if board[starting_row][col] == board[starting_row+1][col] == board[starting_row+2][col] == board[starting_row+3][col]!=0:
				# 4 in a row, player wins 
				winner = board[starting_row][col]
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

def diagonal_up_win(board):
	"""
	Checks if a diagonal / win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	# the possible starting positions of a / diagonal win must be in the left 4 columns and the bottom 3 rows
	for start_row in range(3,6): # bottom 3 rows
		for start_col in range(0,4): # left 4 columns

		# move up and right when comparing board elements
			if board[start_row][start_col] == board[start_row-1][start_col+1] == board[start_row-2][start_col+2] ==board[start_row-3][start_col+3]!=0: 
				winner = board[start_row][start_col]
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

def diagonal_down_win(board):
	"""
	Checks if a diagonal \ win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	# the possible starting positions of a \ diagonal win must be in the left 4 columns and the top 3 rows
	for start_row in range(0,3): # top 3 rows
		for start_col in range(0,4): # left 4 columns

		# move down and right when comparing board elements
			if board[start_row][start_col] == board[start_row+1][start_col+1] == board[start_row+2][start_col+2] ==board[start_row+3][start_col+3]!=0:
				winner = board[start_row][start_col]
				return winner	
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

'''
End of helper functions
'''

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# Implement your solution below
	while True:
		currentResponse = input(prompt) # asks user to input something and saves this as currentResponse

		if currentResponse in valid_inputs: # checks if the input is one of the specified possibilities
			return currentResponse # returns the user's input as a string
		else:
			print("Invalid input, please try again.") # prints message, then continues back to start of while loop
	
	raise NotImplementedError 


def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# define parameters for our board
	rows = 6
	columns = 7
	defaultValue = 0 # fill the empty board with this value
	board = []
	
	for i in range(rows):
		board.append([]) # adds an element (row) to the list 
		for j in range(columns):
			board[i].append(defaultValue) # adds an element (column) to the list, inside the i row element
	
	return board
	raise NotImplementedError


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	rows = 6
	columns = 7
	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O\n")
	print("  1   2   3   4   5   6   7")
	print(" --- --- --- --- --- --- ---")

	for i in range(rows):
		for j in range(columns):
			if board[i][j] == 0:
				print(f"|   ",end='')
			elif board[i][j] == 1:
				print("| X ",end='')
			elif board[i][j] == 2:
				print("| O ",end='')

		print("|")
		print(" --- --- --- --- --- --- ---")
	print("=============================")

	return board
	
	# Implement your solution below
	raise NotImplementedError



def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# Implement your solution below
	if player>2 or player<1 or column < 1 or column > 7: #validate inputs (player must be 1 or 2, columnn must be 1-7)
		return False

	col_index = column-1; # python indexing starts at 0

	if board[0][col_index]!=0: # checks if the column they have selected is already full
		return False

	i = 5 # initialise the row index to start at the bottom row
	while i>=0: # while loop will run 6 times (since there are 6 rows), starts at the bottom row of the board array and moves up
		if board[i][col_index] == 0:
			board[i][col_index] = player # if the space is 'empty', change it to the player number 
			break
		i -=1 # then move up one row
		 
	return True 
	raise NotImplementedError



def execute_player_turn(player, board): # Task 5
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	valid_inputs = ["1", "2", "3", "4", "5", "6", "7"] # the list of allowed inputs (since there are 7 columns)
	prompt = "Player " + str(player) + ", please enter the column you would like to drop your piece into: " # create input prompt to change to match the current player

	while True: # keep going until the player has successfully placed a piece
		desired_column = int(validate_input(prompt,valid_inputs)) # validate the input and convert it to an integer 

		if drop_piece(board,player,desired_column): # check if the column is already full
			return desired_column # if the column is not full, player has successfully placed piece, and their turn is over
		else:
			print("That column is full, please try again.")

	
	raise NotImplementedError


def end_of_game(board): # Question 6
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	# Implement your solution below

	# save the results of all the win checking types (-,|,/,\)
	result  = [horizontal_win(board),vertical_win(board),diagonal_up_win(board),diagonal_down_win(board)]
	
	for i in range(len(result)):
		if result[i]!= 0: # if the result is 1 or 2, then someone has won and we will return the player number
			return result[i]
	

	# check if the board is full
	for col in range(7):
		if board[0][col]== 0:
			# this means the top spot of the column 'col' is empty
			return 0 # the game is not over
	
	# this part of the function is only reached if no one has won, and there are no spaces left in the top row (board is full)
	return 3 # the game is a draw

	raise NotImplementedError


def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	clear_screen()
	board = create_board()
	

	move_counter = 0
	last_player = 2
	player = 1
	last_dropped_col = 0

	while True:
		clear_screen()
		print_board(board)
		if move_counter>0: # print previous turn 
			print(f"Player {last_player} dropped a piece into column {last_dropped_col}")
		last_dropped_col = execute_player_turn(player,board)
		move_counter+=1 #one move has been played
		last_player = player
		player = move_counter%2 + 1
		

		if end_of_game(board)==0:
			continue
		else:
			result = end_of_game(board)
			break

	# this part of the function is only reached when the game is over 
	clear_screen()
	print_board(board)
	if result == 1:
		print(f"Player 1 wins. Congrats.\n")
	elif result == 2:
		print(f"Player 2 wins. Congrats.\n")
	else:
		print("It's a draw. Nobody wins :/")



def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	program_active = True	#initialising variable for loop
	while program_active == True:
		clear_screen()

		print("=============== Main Menu ===============")	#Prints main menu
		print("Welcome to Connect 4!")
		print("1. View Rules")
		print("2. Play a local 2 player game")
		print("3. Play a game against the computer")
		print("4. Exit")
		print("=========================================")

		selected_option = input("Please select an option: ")	#collects selected option
		if selected_option == "1":	#prints the rules and goes back to menu after 10 seconds
			clear_screen()
			print_rules()
			input("Press enter to return")
		elif selected_option == "2":	#starts a 2 player game, reverting to main menu 5 seconds after it ends
			local_2_player_game()
			time.sleep(5)
		elif selected_option == "3":	#starts a game against cpu, reverting to main meny 5 seconds after it ends
			game_against_cpu()
			time.sleep(5)
		elif selected_option == "4":	#exits the program
			exit()

def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	#raise NotImplementedError
	while True: #initialises cpu_easy
		column = random.randint(1, 7) # a completely random integer is dropped into a random column
		if drop_piece(board, player, column):
			return column # returns exactly where the piece was dropped in the board 

def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	# check if instant win is available for current player
	if check_for_win(board, player)!=0:
		column_to_play = check_for_win(board, player)
		drop_piece(board,player,column_to_play)
		return column_to_play
	
	# check if block is required
	elif (check_for_win(board,player%2+1)!=0):
		column_to_play = check_for_win(board,player%2+1)
		drop_piece(board,player,column_to_play)
		return column_to_play

	else: 
		while True:
			column_to_play = random.randint(1,7)
			if drop_piece(board,player,column_to_play)== True:
				return column_to_play

def check_for_traps(board, player):
	"""
	Checks for 'trap' columns
	For explanation on trap columns see: https://www.thesprucecrafts.com/how-to-win-at-connect-four-basic-strategy-tips-412539
	'Never Play Directly Below the Game-Ending Space'

	This function is intended as a helper for cpu_player_hard
	It creates a dummy board and anticipates if any move in the next turn will open up
	a winning or blocking move, then returns a list of such moves so that the AI does not
	fall into any 'traps'
	"""
	dummyboard = deepcopy(board) #creates a copy of the board to be manipulated without affecting the actual game board
	columns_to_avoid = [None] * 14 #list of 'trap' columns, these are:
	#columns that if added to will allow the other player to win or
	#block the current player from winning
	#the list is 14 long because it must allow for multiple columns to be traps
	#given that this function checks both players, 14 spaces have been allocated

	for i in range(7):
		dummy_column = (i+1) # column that will be checked
		drop_piece(dummyboard, player, dummy_column) #simulates dropping a piece into one column per loop, filling possible trap holes, player doesn't matter
		
		if check_for_win(dummyboard, player)!=0:	#checks if first player will win in the turn following either player dropping at position i
			columns_to_avoid[i] = check_for_win(dummyboard, player)
			print(columns_to_avoid)
	
		if (check_for_win(dummyboard,player%2+1)!=0):	#see above comment for second player
			columns_to_avoid[i+7] = check_for_win(dummyboard,player%2+1)
			print(columns_to_avoid)
		
		dummyboard = deepcopy(board) #resets the dummy board so that previous test drops don't affect win condition testing of new drops

	return columns_to_avoid #returns the list of columns to avoid

def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	
	This method has similarities to medium cpu. It first checks if there is an instant win available and then checks if an instant win is possible for the other player. 

	It also checks for a trap (a move that would result in an instant possible win for the other player). It will save a list of columns to avoid and not place the token in these unless it is absolutely necessary.

	Generally, it will favour placing a token in the middle column. Next, it will favour placing a token in the 3rd and 5th columns. 

	If these are all full, it randomly places the token in any available remaining column. 

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: column chosen upon a successful drop (int)
	"""

	# check if instant win is available for current player
	if check_for_win(board, player)!=0:
		column_to_play = check_for_win(board, player)
		drop_piece(board,player,column_to_play)
		return column_to_play
	
	# check if block is required
	elif (check_for_win(board,player%2+1)!=0):
		column_to_play = check_for_win(board,player%2+1)
		drop_piece(board,player,column_to_play)
		return column_to_play
	
	else: 

		trap_columns = check_for_traps(board, player)

		while True:
			if 4 not in trap_columns and drop_piece(board,player,4)== True:
				return 4; # prioritise the middle column

			column_to_play = random.randint(3,5)
			if column_to_play not in trap_columns and drop_piece(board,player,column_to_play)== True:
				return column_to_play
				
			if drop_piece(board,player,3)==False and drop_piece(board,player,4)==False and drop_piece(board,player,5)==False:
				column_to_play = random.randint(2,6)
				if column_to_play not in trap_columns and drop_piece(board,player,column_to_play)== True:
					return column_to_play
				if drop_piece(board,player,2)==False and drop_piece(board,player,6)==False:
					column_to_play = random.randint(1,7)
					if drop_piece(board,player,column_to_play)== True:
						return column_to_play


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""

	board = create_board()
	player = 1
	difficulty_levels = {
		'1': cpu_player_easy,
		'2': cpu_player_medium,
		'3': cpu_player_hard
	}
	
	move_counter = 0
	last_player = 2
	player = 1
	last_dropped_col = 0

	while True:
		select_difficulty = input('Please select a CPU difficulty from: 1 - EASY, 2 - MEDIUM or 3 - HARD: ')
		if select_difficulty in difficulty_levels:
			if select_difficulty == "1": # easy
				while True:
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	

					result = end_of_game(board)

					if result!=0: # check if the player has won
						break 

					# execute player 2 (cpu) turn
					clear_screen()
					print_board(board)
					print(f"Player {last_player} dropped a piece into column {last_dropped_col}")
					last_dropped_col = cpu_player_easy(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1

					result = end_of_game(board)

					if result!=0: # check if the computer has won
						break 
				
				clear_screen()
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None


			else:
				print('Invalid difficulty selected, please try again: ')
			if select_difficulty == "2": # medium
				while True:
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	

					result = end_of_game(board)

					if result!=0: # check if the player has won
						break 

					# execute player 2 (cpu) turn
					clear_screen()
					print_board(board)
					print(f"Player {last_player} dropped a piece into column {last_dropped_col}")
					last_dropped_col = cpu_player_medium(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1

					result = end_of_game(board)

					if result!=0: # check if the computer has won
						break 
				
				clear_screen()
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None


			else:
				print('Invalid difficulty selected, please try again: ')


			if select_difficulty == "3": # hard
				while True:
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	

					result = end_of_game(board)

					if result!=0: # check if the player has won
						break 

					# execute player 2 (cpu) turn
					clear_screen()
					print_board(board)
					print(f"Player {last_player} dropped a piece into column {last_dropped_col}")
					last_dropped_col = cpu_player_hard(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1

					result = end_of_game(board)

					if result!=0: # check if the computer has won
						break 
				
				clear_screen()
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None


			else:
				print('Invalid difficulty selected, please try again: ')


if __name__ == "__main__":
	main()