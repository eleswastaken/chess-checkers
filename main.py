from tkinter import *


### ----------------------- VARIABLES --------------------------- ###
squares = []
row = 0
column = 0
color = "black"
color_len = 0

### ------------------------ BRAIN ------------------------------ ###

### -------------------------- GUI ------------------------------ ###

window = Tk()
window.title('Chessmakeskf')
window.minsize(500,500)
window.config(padx=20, pady=20)

# create all buttons and add to SQUARES list
for i in range(8):
	for y in range(8):
		if color_len % 2 ==0:
			color = 'white'
		else: color = 'black'
		image = PhotoImage(file="o.png", width=50, height=50)
		button = Button(text=f'', width=10, height=5, bg=color, image=image)
		button.grid(column=column, row=row)
		squares.append(button)
		column +=1
		color_len +=1
	color_len -=1
	column = 0
	row +=1


window.mainloop()