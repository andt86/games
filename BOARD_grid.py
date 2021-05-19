
import numpy as np
import colorama, time, random
from os import system

sleep = time.sleep
ss = colorama.Style
r = ss.RESET_ALL
ff = colorama.Fore
bb = colorama.Back

b0 = r+bb.LIGHTBLACK_EX
b1 = r+bb.LIGHTWHITE_EX
b2 = r+bb.CYAN
b3 = r+bb.YELLOW



space0 = str(b0+" "+r)
block0 = str(b1+"   "+r)
block1 = str(b2+"   "+r)
block2 = str(b3+"   "+r)

class big_BOARD:
	board_ = {
		"000" : [str(space0.join([block0,block0,block0])),
						str(space0.join([block0,block0,block0]))],
					
		"100" : [str(space0.join([block1,block0,block0])),
						str(space0.join([block1,block0,block0]))],
					
		"010" : [str(space0.join([block0,block1,block0])),
						str(space0.join([block0,block1,block0]))],
					
		"001" : [str(space0.join([block0,block0,block1])),
						str(space0.join([block0,block0,block1]))],
					
		"110" : [str(space0.join([block0,block0,block1])),
						str(space0.join([block0,block0,block1]))],}
	board_DICT = {
			"0" : block0,
			"1" : block1,
			"2" : block2,}
	
	def __init__(self, board_array):
		row1 = str("".join(board_array[0]))
		row2 = str("".join(board_array[1]))
		row3 = str("".join(board_array[2]))
		self.row_list = [row1, row2, row3]
	
	def make_rows(self, row_str):
		
		block_row = str(space0+str(space0.join(
				[self.board_DICT[ele]for ele in row_str]
				))+space0)
		
		block_rowlist = [block_row, block_row]
		return block_rowlist
	
	def get_block_rowlist(self):
#		row1, row2, row3 = self.row_list
		row_list = self.row_list
		
		seperator_ = str("".join([str(space0)
					for i in range(13)]))
		grid_ = []
		for i in range(3):
			block_rowlist = self.make_rows(row_list[i])
			
			if i == 2:
				grid_.extend(block_rowlist)
			else:
				grid_.extend(block_rowlist)
				grid_.append(seperator_)
		grid_.insert(0,seperator_)
		grid_.append(seperator_)
		
		return grid_
	
	def show_BOARD(self):
		grid_list = str("\n".join([str("   "+str(ele))
				for ele in self.get_block_rowlist()]))
		
		print(grid_list)
		
#test = np.array([	['0', '1', '0'],
#								['0', '1', '0'],
#								['0', '2', '0']])

#AA = big_BOARD(test).get_block_rowlist()
#print(len(AA))
