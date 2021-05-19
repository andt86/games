
import numpy as np
import colorama, time, random
from os import system
from BOARD_grid import big_BOARD

sleep = time.sleep
ss = colorama.Style
r = ss.RESET_ALL
ff = colorama.Fore
bb = colorama.Back

c0 = r+ff.LIGHTBLUE_EX
c1 = r+ff.CYAN
c2 = r+ff.YELLOW
c3 = r+ff.GREEN
c4 = r+ff.MAGENTA

b0 = r+bb.LIGHTBLACK_EX
b1 = r+bb.BLACK
b2 = r+bb.YELLOW
b3 = r+bb.BLACK

P0 = r+ff.LIGHTBLUE_EX
P1 = r+ff.CYAN
P2 = r+ff.YELLOW




class exceeds_input_attempts(Exception):
	pass



def CLEAR():
	_ = system('clear')


def BANNER_label(label_, str_, color_):
	cc = r+color_
	x = str("\n".join(["",
			str(cc+str(label_).center(40," ")+r),
			str(str_),""]))
	
	
	CLEAR()
	print(x)


def BANNER(str_, color_):
	cc = r+color_
	x = str("\n".join(["",str(cc+str(str_).center(40," ")+r),""]))
	
	CLEAR()
	print(x)



def BANNER_list(str_list, color_):
	if color_ == 0:
		color_ = r+ff.LIGHTBLUE_EX
	else:
		color_ = r+color_
	
	str_list = [str(color_+str(ele).center(40," ")+r)
			for ele in str_list]
	
	str_list.insert(0,"")
	str_list.append("")
	
	str_ = str("\n".join(str_list))
	
	CLEAR()
	print(str_)



new_board = ["0","0","0"]
T1 = list("121")
T2 = list("212")
T3 = list("202")


class BOARD_grid:
	board = np.array([				new_board,
													new_board,
													new_board])



def clear_BOARD():
	BANNER("CLEAR BOARD",ff.GREEN)
	continue_str = str("\n".join(
			["","",str(c3+str(str("continue"
					).rjust(12," ")).ljust(15," ")+r+":   ")]))
	
	sleep(1)
	input(continue_str)
	
	BOARD_grid.board = np.array([			new_board,
													new_board,
													new_board])
	


#board = testboard

class BOARD:
	player_LABEL = {
		1 : str(c0+str("PLAYER ").rjust(15," ")+c1+"#1"+r),
		2 : str(c0+str("PLAYER ").rjust(15," ")+c2+"#2"+r)}
	
#	marker_DICT = dict(zip(["0","1","2"],["_","O","X"]))
	color_marker_DICT = dict(
			zip(["0","1","2"],
				[str(P0+"_"+r),str(P1+"O"+r),str(P2+"X"+r)]))
	player_DICT = dict(zip([0,1],["0","1"]))
	
	
	
	def __init__(self):
		self.position_options = np.array([	[1,2,3],
																		[4,5,6],
																		[7,8,9]])
		self.position_DICT = {
			1 : (0,0),
			2 : (0,1),
			3 : (0,2),
			4 : (1, 0),
			5 : (1, 1),
			6 : (1, 2),
			7 : (2, 0),
			8 : (2, 1),
			9 : (2, 2)}
		
	
#	def clear_BOARD(self):
#		new_board = ["0","0","0"]
#		self.board = np.array([	new_board,
#													new_board,
#													new_board])
#		
#		BANNER("BOARD CLEARED",ff.CYAN)
#		input("\n      continue :   ")
		
		
	def check_board(self,player_key):
		check_list = [
				[1,2,3],	[4,5,6],	[7,8,9],
				[1,5,9],	[3,5,7],	[1,4,7],
				[2,5,8],	[3,6,9]]
		
		k = str(player_key)
		check_ = "no win"
		for lists in check_list:
			combo_list = [BOARD_grid.board[
					self.position_DICT[ele]]
				for ele in lists]
			if combo_list == [k,k,k]:
				check_ = "win"
		
		return check_
	
	def print_board(self, clear_):
		grid_options = self.boardOPTION()
		board_grid = big_BOARD(BOARD_grid.board
				).get_block_rowlist()
		
		board_grid = [str("        "+str(ele))
					for ele in board_grid]
		
		if clear_ == 1:
			CLEAR()
		
		print("\n\n")
		for i in range(10):
			x1 = str(board_grid[i])
			x2 = str(grid_options[i])
			X = str("       ".join([x1,x2]))
			print(X)
			
		
		print("\n")
	
	def boardOPTION(self):
		board_grid = []
		for i in range(3):
#			print(self.position_options[i])
			x = str(" | ".join([str(ele)
					for ele in self.position_options[i]]))
			board_grid.append(x)
		
		board_grid = [str("     | "+ele+" |")
				for ele in board_grid]
		
		grid_options = board_grid
		
		
		
		blank1 = str(" ")
		for _ in range(4):
			grid_options.insert(0,blank1)
			grid_options.append(blank1)
		
		
		return grid_options
		
		
		
	
	def take_turn(self, player_key, turn_cnt):
		turn_str = str(c1+str("turn "+str(turn_cnt)
				).rjust(8," ")+r)
		
		str_ = self.player_LABEL[player_key]
		DICT = self.position_DICT
		print_board = self.print_board
		while True:
			BANNER_label("ENTER SPACE", str_, ff.CYAN)
			print(turn_str)
			print_board(0)
			position_ = int(input_("SPACE"))
			if position_ in [1,2,3,4,5,6,7,8,9]:
				pass
			else:
				BANNER("INVALID SPACE", ff.RED)
			
			position = BOARD_grid.board[DICT[position_]]
			if position != "0":
				BANNER("SPACE TAKEN", ff.RED)
				sleep(0.5)
			else:
				BOARD_grid.board[DICT[position_]] = str(player_key)
				break
		BANNER_label("End of turn", str_, ff.CYAN)
		sleep(0.25)
	
	def check_forFULLboard(self):
		board_full = "full"
		for i in range(3):
			if "0" in BOARD_grid.board[i]:
				board_full = "good"
		return board_full
	
	def check_forwinners(self):
		check_ = self.check_board
		player_key_list = [1, 2]
		check_list = [check_(ele) for ele in player_key_list]
		
		if check_list == ['no win', 'no win']:
			code_ = "no win"
		else:
			code_ = "win"
			key_ = check_list.index("win")
			winner_key = int(player_key_list[key_])
			
			BANNER_label("WINNER",
					str(self.player_LABEL[winner_key]),
					ff.CYAN)
			self.print_board(0)
		
		board_full = self.check_forFULLboard()
		if code_ == "no win" and board_full == "full":
			code_ = "game over draw"
			
			BANNER_label("GAME OVER",
					str("game over draw"),
					ff.CYAN)
			
#			input()
			
		return code_
	
	def game_(self):
#		self.clear_BOARD()
		take_turn = self.take_turn
		check_ = self.check_forwinners
		
		turn_cnt = 1
		while True:
			
#			print_board(1)
#			input("    take turn  :  ")
			take_turn(1, turn_cnt)
			
			code_ = check_()
			if code_ == "win":
				break
			elif code_ == "game over draw":
				break
			
			take_turn(2, turn_cnt)
			code_ = check_()
			if code_ == "win":
				break
			elif code_ == "game over draw":
				break
			
			turn_cnt += 1



#def positionOPTION():
#	x = str("\n".join([str("   "+str(ele1)) 
#			for ele1 in [str(" | ".join(ele))
#			for ele in ["123","456","789"]]]))
#	
#	print(x)
	
	
def input_(label_):
	good_ = [1,2,3,4,5,6,7,8,9]
	while True:
		try:
			q = int(input(str(label_).rjust(12," ")+":  "))
			if q in good_:
				break
			else:
				raise ValueError()
			
		except (IndexError, ValueError, TypeError):
			BANNER("error", ff.CYAN)
	return q


def RESTART_():
	input_typeDICT = {
			"S" : "RESTART",
			"Q" : "QUIT",}
	
	q1, q2 = str(c4+"   ["+r), str(c4+"]   "+r)
	ques_ = str("\n     :  ")
	k_ = [str(q1+c2+str(ele)+q2)
			for ele in list(input_typeDICT.keys())]
	v_ = [str(c1+str(ele)+r)
			for ele in list(input_typeDICT.values())]
	list_ = str("\n".join([str("".join(tuple_))
			for tuple_ in list(zip(k_, v_))]))
	
	
	input_attempt = 0
	max_input_attempt = 3
	
	continue_str = str("\n".join(
			["","",str(c3+str(str("continue"
					).rjust(12," ")).ljust(15," ")+r+":   ")]))
	
	sleep(2)
	input(continue_str)
	
	while True:
		
		
		
		try:
			if input_attempt >= max_input_attempt:
				raise exceeds_input_attempts()
				#for _ in range(3):
#					BANNER_list(
#							["ERROR", 
#							"EXCEEDS INPUT ATTEMPTS",
#							"EXITING PGM"], ff.RED)
#					sleep(0.25)
#					CLEAR()
#					sleep(0.125)
#					
#				Ans_ = "QUIT"
#				break
			BANNER("CHOOSE OPTION", ff.GREEN)
			
			print("")
			print(list_)
			q = str(input(ques_))
			if q == "":
				raise TypeError()
			else:
				if q in ["Q", "q"]:
					Ans_ = "QUIT"
					break
				elif q in ["S", "s"]:
					Ans_ = "RESTART"
					break
				else:
					raise TypeError()
		
		except (TypeError, ValueError, IndexError):
			input_attempt += 1
			for _ in range(3):
					BANNER_list(
						["ERROR", "INVALID INPUT"], ff.RED)
					sleep(0.25)
					CLEAR()
					sleep(0.125)
					continue
		except exceeds_input_attempts:
			exceeds_str = str("\n".join(
				[str(c3+str(ele).center(40," ")+r)
					for ele in 
						["EXCEEDS INPUT ATTEMPTS",
						"EXITING PGM"]]))
			
			for _ in range(3):
				BANNER("ERROR", ff.RED)
				print(exceeds_str)
				sleep(0.25)
				CLEAR()
				sleep(0.125)
			Ans_ = "QUIT"
			break
			
	
	if Ans_ == "QUIT":
		sleep(0.25)
		BANNER("QUITING PGM", ff.RED)
		sleep(0.5)
		quit()
	elif Ans_ == "RESTART":
		sleep(0.25)
		BANNER("RESTARTING PGM",
				ff.GREEN+ss.BRIGHT)
		sleep(0.5)
		START()
		


def START():
	clear_BOARD()
	BOARD().game_()
	RESTART_()

START()
