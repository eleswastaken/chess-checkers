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
move = "black"


### ------------------------ BRAIN ------------------------------ ###

def check_win():
	

def check_move():
	for button in all_buttons:
		button["state"] = "normal"
	if move == "white" and  to_move != True:
		for button in white_sq:
			button["state"] = 'disabled'
		for button in black_sq:
			button["state"] = 'normal'
	elif move == "black" and to_move != True:
		for button in black_sq:
			button["state"] = 'disabled'
		for button in white_sq:
			button["state"] = 'normal'

def eat(word, button_id):
	global move
	print("ate", word)
	for dif in [-14,-18,14,18]:
		if dif+last_bt_id==button_id:
			if dif/2+last_bt_id in whites:
				eat_id = dif/2+last_bt_id
				eat_bt = white_sq[whites.index(eat_id)]
				cl_bt = "white"
			elif dif/2+last_bt_id in blacks:
				eat_id = dif/2+last_bt_id
				eat_bt = black_sq[blacks.index(eat_id)]
				cl_bt = "black"
	if word == "white" and cl_bt == "white":
		whites.remove(eat_id)
		white_sq.remove(eat_bt)	
	elif word =="black" and cl_bt == "black":
		blacks.remove(eat_id)
		black_sq.remove(eat_bt)
	eat_bt.config(image=pixelVirtual)
	if move == "white":
		move = "black"
	elif move == "black":
		move = "white"

def make_move(button_id):
	global move
	print(button_id, 'made a move')

	def move_re():
		if last_bt_id in whites:
			button.config(image=white)
			whites.append(button_id)
			whites.remove(last_bt_id)
			white_sq.append(button)
			white_sq.remove(last_bt)

		elif last_bt_id in blacks:
			button.config(image=black)
			blacks.append(button_id)
			blacks.remove(last_bt_id)
			black_sq.append(button)
			black_sq.remove(last_bt)
		last_bt.config(image=pixelVirtual)
		
	button = all_buttons[button_id]
	if (last_bt_id - button_id)%7==0 or (last_bt_id - button_id)%9==0:
		for dif in [-7,-9,7,9]:
			if last_bt_id+dif == button_id:
				move_re()
				print('hi hi')
				# implement here no-go-back too
				if move == "white":
					move = "black"
				elif move == "black":
					move = "white"
		else:
			for dif in [-14,-18,14,18]:
				if last_bt_id+dif == button_id:
					if dif/2+last_bt_id in whites:
						eat("white", button_id)
						move_re()
					elif dif/2+last_bt_id in blacks:
						eat("black", button_id)
						move_re()
					print('hi twice')
			else:
				print('too far')
		
	else:
		print("out of line")
		# for dif in [-14,-18,14,18]:
		# 	if last_bt_id+dif == button_id:
		# 		if dif/2+last_bt_id in blacks or dif/2+last_bt_id in whites:
					
		# 			if last_bt in black_sq and (last_bt_id-9 in whites or last_bt_id-7 in whites or last_bt_id+9 in whites or last_bt_id+7 in whites):
		# 				eat("white", button_id)
		# 			elif last_bt in white_sq and (last_bt_id-9 in blacks or last_bt_id-7 in blacks or last_bt_id+9 in blacks or last_bt_id+7 in blacks):
		# 				eat("black", button_id)
				
		# 			if last_bt_id in whites:
		# 				button.config(image=white)
		# 				whites.append(button_id)
		# 				whites.remove(last_bt_id)
		# 				white_sq.append(button)
		# 				white_sq.remove(last_bt)

		# 			elif last_bt_id in blacks:
		# 				button.config(image=black)
		# 				blacks.append(button_id)
		# 				blacks.remove(last_bt_id)
		# 				black_sq.append(button)
		# 				black_sq.remove(last_bt)
		# 			last_bt.config(image=pixelVirtual)
		# 			if move == "white":
		# 				move = "black"
		# 			elif move == "black":
		# 				move = "white"
		# 		else:
					# print('too far')
		# else:
		# 	if button_id 
		# 	if last_bt_id in whites:
		# 		button.config(image=white)
		# 		whites.append(button_id)
		# 		whites.remove(last_bt_id)
		# 		white_sq.append(button)
		# 		white_sq.remove(last_bt)

		# 	elif last_bt_id in blacks:
		# 		button.config(image=black)
		# 		blacks.append(button_id)
		# 		blacks.remove(last_bt_id)
		# 		black_sq.append(button)
		# 		black_sq.remove(last_bt)
		# 	last_bt.config(image=pixelVirtual)
		# 	if move == "white":
		# 		move = "black"
		# 	elif move == "black":
		# 		move = "white"
	
	
	

last_bt = None
last_bt_id = None
to_move = False
def pressed(button_id):
	global to_move, last_bt, last_bt_id
	print(button_id, "got pressed")

	if to_move:
		to_move = False

		if button_id in whites or button_id in blacks:
			print('is not empty')
		else:
			make_move(button_id)
		last_bt.config(bg='grey')

	else:
		to_move = True

		if button_id not in whites and button_id not in blacks:
			to_move = False

		elif button_id in whites:			
			button = white_sq[whites.index(button_id)]
			button.config(bg='blue')

		elif button_id in blacks:
			button = black_sq[blacks.index(button_id)]
			button.config(bg='blue')
		
		try:
			last_bt = button
			last_bt_id = button_id
		except: print('no peice')
	check_move()



### -------------------------- GUI ------------------------------ ###

window = Tk()
window.title('Checkmates')
window.minsize(500,500)
window.config(padx=20, pady=20)

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

# move = Label(text="white to move")	
# move.grid(column=0, row=row+1, columnspan=8)

window.mainloop()