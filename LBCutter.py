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
		self.LifeButton = 'qualquer coisa'
		self.EmptyButton = 'qualquer coisa'
		self.ExtraButton = 'qualquer coisa'
		self.LifeView = 'qualquer coisa'
		self.EmptyView = 'qualquer coisa'
		self.ExtraView = 'qualquer coisa'
		self.photo1 = 'qualquer coisa'
		self.photo2 = 'qualquer coisa'
		self.photo3 = 'qualquer coisa'
		self.Texto_final = Label(root, text='\nPlease, choose an option!')

	# Get data
	def getLifeButton(self):
		return self.LifeButton

	def getLifeView(self):
		return self.LifeView

	def getEmptyButton(self):
		return self.EmptyButton

	def getEmptyView(self):
		return self.EmptyView

	def getExtraButton(self):
		return self.ExtraButton

	def getExtraView(self):
		return self.ExtraView

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
			self.LifeButton = Button(root, text ="Lifebar", state=DISABLED, width=10)
			self.LifeView = Label(root, text='lifebar.png not found!', fg='#f00')
		elif int(Image.open("lifebar.png").size[0]) != 104:
			self.LifeButton = Button(root, text ="Lifebar", state=DISABLED, width=10)
			self.LifeView = Label(root, text='Image width is not 104!', fg='#f00')
		elif int(Image.open("lifebar.png").size[1]) > 12:
			self.LifeButton = Button(root, text ="Lifebar", state=DISABLED, width=10)
			self.LifeView = Label(root, text="Image height is too large!", fg='#f00')
		else:
			self.LifeButton = Button(root, text ="Lifebar", command=LifebarCut, width=10)
			self.photo1 = tk.PhotoImage(file='lifebar.png')
			self.LifeView = ttk.Label(root, image=self.photo1)

		# Emptybar ----------------------------------------------------------------------
		if not os.path.isfile('emptybar.png'):
			self.EmptyButton = Button(root, text ="Emptybar", state=DISABLED, width=10)
			self.EmptyView = Label(root, text='emptybar.png not found!', fg='#f00')
		elif int(Image.open("emptybar.png").size[0]) != 106:
			self.EmptyButton = Button(root, text ="Emptybar", state=DISABLED, width=10)
			self.EmptyView = Label(root, text='Image width is not 106!', fg='#f00')
		elif int(Image.open("emptybar.png").size[1]) > 12:
			self.EmptyButton = Button(root, text ="Emptybar", state=DISABLED, width=10)
			self.EmptyView = Label(root, text="Image height is too large!", fg='#f00')
		else:
			self.EmptyButton = Button(root, text ="Emptybar", command = EmptybarCut, width=10)
			self.photo2 = tk.PhotoImage(file='emptybar.png')
			self.EmptyView = ttk.Label(root, image=self.photo2)

		# Extrabar ----------------------------------------------------------------------
		if not os.path.isfile('extrabar.png'):
			self.ExtraButton = Button(root, text ="Extrabar", state=DISABLED, width=10)
			self.ExtraView = Label(root, text='extrabar.png not found!', fg='#f00')
		elif int(Image.open("extrabar.png").size[0]) != 104:
			self.EmptyButton = Button(root, text ="Extrabar", state=DISABLED, width=10)
			self.EmptyView = Label(root, text='Image width is not 104!', fg='#f00')
		elif int(Image.open("extrabar.png").size[1]) > 12:
			self.EmptyButton = Button(root, text ="Extrabar", state=DISABLED, width=10)
			self.EmptyView = Label(root, text="Image height is too large!", fg='#f00')
		else:
			self.ExtraButton = Button(root, text ="Extrabar", command = ExtrabarCut, width=10)
			self.photo3 = tk.PhotoImage(file='extrabar.png')
			self.ExtraView = ttk.Label(root, image=self.photo3)
		
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

Label(root, text='SORR LIFEBAR CUTTER v1.2 by Chavyn\n').grid(row=0, columnspan=2, ipadx=25)
Label(root, text='What do you want to crop?\n').grid(row=1, columnspan=2)

# Lifebar -----------------------------------------------------------------------

p1.botoes()

p1.getLifeButton().grid(row=2, column=0)
p1.getLifeView().grid(row=2, column=1, sticky='w')

p1.getEmptyButton().grid(row=3, column=0)
p1.getEmptyView().grid(row=3, column=1, sticky='w')

p1.getExtraButton().grid(row=4, column=0)
p1.getExtraView().grid(row=4, column=1, sticky='w')


p1.getFinalText().grid(row=5, columnspan=2)
root.mainloop()