from tkinter import *
from functools import partial


### ----------------------- VARIABLES --------------------------- ###
all_buttons = []
whites = []
blacks = []
row = 0
column = 0
color = "grey"
color_len = 0
button_id = 0


### ------------------------ BRAIN ------------------------------ ###
def do_stuff(button_id):
	# button = all_buttons[button_id]
	# button.config(bg='darkgrey')
	# print(button_id+1)
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
		else: color = 'grey'
		if color == 'grey':
			if button_id < 24:
				button = Button(text='',
								highlightthickness=0,
								image=white,
								width=85,
								height=85,
								compound="c",
								bg=color,
								command=partial(do_stuff, button_id),
							)
				whites.append(button)
			if button_id < 40 and button_id > 23:
				button = Button(text='',
							highlightthickness=0,
							image=pixelVirtual,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(do_stuff, button_id),
						)
			if button_id > 39:
				button = Button(text='',
							highlightthickness=0,
							image=black,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(do_stuff, button_id),
						)
				blacks.append(button)
		else:
			button = Button(text='',
							highlightthickness=0,
							image=pixelVirtual,
							width=85,
							height=85,
							compound="c",
							bg=color,
							command=partial(do_stuff, button_id),
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
	
window.mainloop()