from os import mkdir
import os.path
from pathlib import Path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()
root.title('SorR Lifebar Cutter')
root.geometry("290x230")

if os.path.isfile('icon/cutter16x16.ico'):
	root.iconbitmap('icon/cutter16x16.ico')

root.resizable(width=False, height=False)

# ------- FUNCTIONS -------------------------------
#echo = lambda value: Label(root, text=value).pack()
class LBC:
	def __init__(self):
		self.LifeButton = Button(root, command=LifebarCut, text ="Lifebar", width=10, state=DISABLED)
		self.EmptyButton = Button(root, command=EmptybarCut, text ="Emptybar", width=10, state=DISABLED)
		self.ExtraButton = Button(root, command=ExtrabarCut, text ="Extrabar", width=10, state=DISABLED)
		self.View = Label(root, text=' ', fg='#f00')

		self.photo1 = ""
		self.photo2 = ""
		self.photo3 = ""
		self.Texto_final = Label(root, text='\nPlease, choose an option!')

	# Get data
	def getFinalText(self):
		return self.Texto_final

	def changeText(self):
		self.Texto_final = Label(root, text='\nDONE!', fg='#00f')
		return self.Texto_final

	def removeLabel(self):
		self.Texto_final.after(9, self.Texto_final.destroy())

	def botoes(self):
		# Lifebar -----------------------------------------------------------------------
		if not os.path.isfile('lifebar.png'):
			self.View['text'] = 'lifebar.png not found!'
		elif int(Image.open("lifebar.png").size[0]) != 104:
			self.View['text'] = 'Image width is not 104!'
		elif int(Image.open("lifebar.png").size[1]) > 12:
			self.View['text'] = "Image height is too large!"
		else:
			self.LifeButton['state'] = NORMAL
			self.photo1 = tk.PhotoImage(file='lifebar.png')
			self.View = Label(root, image=self.photo1)

		self.LifeButton.grid(row=2, column=0)
		self.View.grid(row=2, column=1, sticky='w')

		# Emptybar ----------------------------------------------------------------------
		if not os.path.isfile('emptybar.png'):
			self.View['text'] = 'emptybar.png not found!'
		elif int(Image.open("emptybar.png").size[0]) != 106:
			self.View['text'] = 'Image width is not 106!'
		elif int(Image.open("emptybar.png").size[1]) > 12:
			self.View['text'] = "Image height is too large!"
		else:
			self.EmptyButton['state'] = NORMAL
			self.photo2 = tk.PhotoImage(file='emptybar.png')
			self.View = Label(root, image=self.photo2)

		self.EmptyButton.grid(row=3, column=0)
		self.View.grid(row=3, column=1, sticky='w')

		# Extrabar ----------------------------------------------------------------------
		if not os.path.isfile('extrabar.png'):
			self.View['text'] = 'extrabar.png not found!'
		elif int(Image.open("extrabar.png").size[0]) != 104:
			self.View['text'] = 'Image width is not 104!'
		elif int(Image.open("extrabar.png").size[1]) > 12:
			self.View['text'] = "Image height is too large!"
		else:
			self.ExtraButton['state'] = NORMAL
			self.photo3 = tk.PhotoImage(file='extrabar.png')
			self.View = Label(root, image=self.photo3)

		self.ExtraButton.grid(row=4, column=0)
		self.View.grid(row=4, column=1, sticky='w')
		
def LifebarCut():
	p1.removeLabel()
	if not os.path.exists('lifebar'):
		os.mkdir('lifebar')
	original = Image.open("lifebar.png")
	width, height = original.size # Get dimensions
	for G in range(24, 128):
		cropped = original.crop((0, 0, width, height))
		cropped.save(f'lifebar/{G}.png')
		print(G,'created')
		width-=1
	p1.changeText().grid(row=5, columnspan=2)
	
def ExtrabarCut():
	p1.removeLabel()
	if not os.path.exists('extrabar'):
		os.mkdir('extrabar')
	original = Image.open("extrabar.png")
	width, height = original.size # Get dimensions
	for M in range(24, 128):
		cropped = original.crop((0, 0, width, height))
		cropped.save(f'extrabar/{M}.png')
		print(M,'created')
		width-=1
	p1.changeText().grid(row=5, columnspan=2)

def EmptybarCut():
	p1.removeLabel()
	if not os.path.exists('emptybar'):
		os.mkdir('emptybar')
	original = Image.open("emptybar.png")
	width, height = original.size # Get dimensions
	xpos = 0
	for S in range(24, 128):
		cropped = original.crop((xpos, 0, width, height))
		cropped.save(f'emptybar/{S}.png')
		print(f'{S} created')
		xpos+=1
	p1.changeText().grid(row=5, columnspan=2)

#================= HOME ==========================
p1 = LBC()

Label(root, text='SORR LIFEBAR CUTTER v1.3 by Chavyn\n').grid(row=0, columnspan=2, ipadx=25)
Label(root, text='What do you want to crop?\n').grid(row=1, columnspan=2)

# -----------------------------------------------------------------------

p1.botoes()

p1.getFinalText().grid(row=5, columnspan=2)
root.mainloop()