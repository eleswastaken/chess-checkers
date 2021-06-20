from tkinter import *
from functools import partial


### ----------------------- VARIABLES --------------------------- ###
all_buttons = []

whites = [] # numbers
blacks = []

white_sq = [] # objects
black_sq = []

row = 0
column = 0
color = "grey"
color_len = 0
button_id = 0
turn = "black"

window = Tk()
window.title('Checkmates')
window.minsize(500,500)
window.config(padx=20, pady=20)

### ------------------------ BRAIN ------------------------------ ###

def check_win():
	# if one of players runs out of tiles, one has lost
	if len(whites) == 0 or len(blacks) == 0:
		if blacks > whites:
			print("BLACK WINS")
		elif whites > blacks:
			print("WHITE WINS")
		for btn in all_buttons:
			btn["state"] = "disabled"


def check_move():
	# two lines below make sure there are no disabled tiles left
	for button in all_buttons:
		button["state"] = "normal"

	if turn == "white" and  on_hold != True:
		for button in white_sq:
			button["state"] = 'disabled'
		for button in black_sq:
			button["state"] = 'normal'
	elif turn == "black" and on_hold != True:
		for button in black_sq:
			button["state"] = 'disabled'
		for button in white_sq:
			button["state"] = 'normal'

	# --> called every move
	check_win()

def eat_tile(which, lst_bt_id, btn_id):
	global turn
	for step in [-14,-18,14,18]:
		# checks whether between last-bt-id and bt-id is a tile
		if which == "black" and step/2+lst_bt_id in whites:
			white_sq[whites.index(step/2+lst_bt_id)].config(image=pixelVirtual)
			white_sq.remove(white_sq[whites.index(step/2+lst_bt_id)])
			whites.remove(step/2+lst_bt_id)
			move_re(lst_bt_id, btn_id)

		elif which == "white" and step/2+lst_bt_id in blacks:
			black_sq[blacks.index(step/2+lst_bt_id)].config(image=pixelVirtual)
			black_sq.remove(black_sq[blacks.index(step/2+lst_bt_id)])
			blacks.remove(step/2+lst_bt_id)
			move_re(lst_bt_id, btn_id)
		# for n_step in [-14,-18,14,18]:
		# 	if (n_step/2+btn_id in blacks or n_step/2+btn_id in whites) and (btn_id+n_step not in whites) and (btn_id+n_step not in blacks):
		# 		print("hello, this it a;fasddhdhfg")
		# 		# check whether player wants
	if turn == "white":
		turn = "black"
	elif turn == "black":
		turn = "white"		

# this function removes-adds tiles-ids ~ registeres a move
def move_re(lst_bt_id, btn_id):
	button = all_buttons[btn_id]
	lst_bt = all_buttons[lst_bt_id]
	if lst_bt_id in whites:
		button.config(image=white)
		whites.append(btn_id)
		whites.remove(lst_bt_id)
		white_sq.append(button)
		white_sq.remove(last_bt)

	elif lst_bt_id in blacks:
		button.config(image=black)
		blacks.append(btn_id)
		blacks.remove(lst_bt_id)
		black_sq.append(button)
		black_sq.remove(last_bt)
	lst_bt.config(image=pixelVirtual)

def make_move(button_id):
	global turn

	if (last_bt_id - button_id)%7==0 or (last_bt_id - button_id)%9==0:
		# moving only one tile
		for dif in [-7,-9,7,9]:
			# checking wether selected tile is withing 1 tile
			if last_bt_id+dif == button_id:
				# checking for white tile to go only forward
				if last_bt_id in whites and button_id > last_bt_id:
					move_re(last_bt_id, button_id)
					if turn == "white":
						turn = "black"
					elif turn == "black":
						turn = "white"
				# checking for black tile to go only forward
				elif last_bt_id in blacks and button_id < last_bt_id:
					move_re(last_bt_id, button_id)
					if turn == "white":
						turn = "black"
					elif turn == "black":
						turn = "white"
				else:
					print("You cannot go back.")
			# eating opponent's one tile and making a move
			elif last_bt_id+dif in whites and last_bt_id+dif*2 == button_id:
				eat_tile("black", last_bt_id, button_id)
			elif last_bt_id+dif in blacks and last_bt_id+dif*2 == button_id:
				eat_tile("white", last_bt_id, button_id)
	else:
		print("out of line")


last_bt = None
last_bt_id = None
on_hold = False
def pressed(button_id):
	global on_hold, last_bt, last_bt_id

	# checks whether any button is on hold
	if on_hold:
		on_hold = False

		if button_id in whites or button_id in blacks:
			last_bt.config(bg='grey')
			print('Is not empty.')
		else:
			make_move(button_id)
			last_bt.config(bg='grey')

	else:
		on_hold = True

		# if empty tile is selected change the turn back (reselect)
		if button_id not in whites and button_id not in blacks:
			on_hold = False
		
		# "selects button"/ turns tile with button_id in blue color
		elif button_id in whites:			
			button = white_sq[whites.index(button_id)]
			button.config(bg='blue')

		elif button_id in blacks:
			button = black_sq[blacks.index(button_id)]
			button.config(bg='blue')
		
		# in case of epmty tile
		try:
			last_bt = button
			last_bt_id = button_id
		except: print('no peice')

	# is being called every press, checks whose turn is
	check_move()



### -------------------------- GUI ------------------------------ ###



black = PhotoImage(file="images/black.png")
white = PhotoImage(file="images/white.png")
pixelVirtual = PhotoImage(width=1, height=1)

# create all buttons and add to SQUARES list
for i in range(8):
	for y in range(8):
		if color_len % 2 ==0:
			color = 'white'
		else:
			color = 'grey'
			
		if color == 'grey':
			if button_id < 24:
				button = Button(text=button_id,
								highlightthickness=0,
								image=white,
								width=85,
								height=85,
								compound="c",
								bg=color,
								command=partial(pressed, button_id),
							)
				white_sq.append(button)
				whites.append(button_id)

			if button_id < 40 and button_id > 23:
				button = Button(text=button_id,
							highlightthickness=0,
							image=pixelVirtual,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(pressed, button_id),
						)
				
			if button_id > 39:
				button = Button(text=button_id,
							highlightthickness=0,
							image=black,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(pressed, button_id),
						)
				button["state"] = "disabled"
				black_sq.append(button)
				blacks.append(button_id)

		else:
			button = Button(text='',
							highlightthickness=0,
							image=pixelVirtual,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(pressed, button_id),
						)
			button['state'] = 'disabled'

		button.grid(column=column, row=row)

		all_buttons.append(button)

		column +=1
		color_len +=1
		button_id +=1
	color_len -=1
	column = 0
	row +=1

	## code below turns board 90 degrees
	# 	row +=1
	# 	color_len +=1
	# 	button_id +=1
	# color_len -=1
	# row = 0
	# column +=1

window.mainloop()