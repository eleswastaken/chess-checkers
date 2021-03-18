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


### ------------------------ BRAIN ------------------------------ ###

def make_move(button_id):
	global old_button, old_id, is_waiting
	print('called make_move')
	button = all_buttons[button_id]

	if old_button.cget('image') == 'pyimage2':
		button.config(image=white)
		white_sq.remove(old_button)
		white_sq.append(button)
		whites.remove(old_id)
		whites.append(button_id)

	elif old_button.cget('image') == 'pyimage1':
		button.config(image=black)
		black_sq.remove(old_button)
		black_sq.append(button)
		blacks.remove(old_id)
		blacks.append(button_id)

	old_button.config(image=pixelVirtual, bg='grey')


old_button = None
old_id = None
is_waiting = False
just = True
def pressed(button_id):
	global old_button, is_waiting, old_id, just
	just = True
	print('called pressed')
	print(button_id)

	if is_waiting:
		make_move(button_id)
		is_waiting = False
		just = False
		pass

	# white is pressed
	if just:
		if button_id in whites:
			button = white_sq[whites.index(button_id)]
			button.config(bg='blue')
			old_button = button
			old_id = button_id
			is_waiting = True
			pass

		# black is pressed
		elif button_id in blacks:
			button = black_sq[blacks.index(button_id)]
			button.config(bg='blue')
			old_button = button
			old_id = button_id
			is_waiting = True
			pass
### -------------------------- GUI ------------------------------ ###

window = Tk()
window.title('Chessmakeskf')
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
				button = Button(text='',
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
				button = Button(text='',
							highlightthickness=0,
							image=pixelVirtual,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(pressed, button_id),
						)
				
			if button_id > 39:
				button = Button(text='',
							highlightthickness=0,
							image=black,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(pressed, button_id),
						)
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
# print(whites)
# print(blacks)
# print(white_sq)
# print(black_sq)
	
window.mainloop()