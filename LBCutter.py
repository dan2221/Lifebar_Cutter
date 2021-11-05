from os import mkdir
import os.path
from pathlib import Path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image

root = Tk()
root.title('SorR Lifebar Cutter')
root.geometry("282x280")

root.resizable(width=False, height=False)

# ------- FUNCTIONS -------------------------------
class LBC:
	def __init__(self):
		self.LifeButton = Button(root, command=lambda: barCut("Lifebar"), text ="Lifebar", width=10, state=DISABLED)
		self.EmptyButton = Button(root, command=lambda: barCut('emptybar'), text ="Emptybar", width=10, state=DISABLED)
		self.ExtraButton = Button(root, command=lambda: barCut('extrabar'), text ="Extrabar", width=10, state=DISABLED)
		self.View1 = Label(root, text=' ', fg='#f00')
		self.View2 = Label(root, text=' ', fg='#f00')
		self.View3 = Label(root, text=' ', fg='#f00')

		self.photo1 = ""
		self.photo2 = ""
		self.photo3 = ""
		self.Texto_final = Label(root, text='\nPlease, choose an option!\n')

	# Get data
	def getFinalText(self):
		return self.Texto_final

	def changeText(self, mytext):
		self.Texto_final = Label(root, text=f'\n{mytext}\n', fg='#00f')
		return self.Texto_final

	def removeLabel(self):
		self.Texto_final.after(9, self.Texto_final.destroy())

	def myBottoms(self):
		# Lifebar -----------------------------------------------------------------------
		if not os.path.isfile('lifebar.png'):
			self.View1['text'] = 'lifebar.png not found!'
		elif int(Image.open("lifebar.png").size[0]) != 104:
			self.View1['text'] = 'Image width is not 104!'
		elif int(Image.open("lifebar.png").size[1]) > 12:
			self.View1['text'] = "Image height is too large!"
		else:
			self.LifeButton['state'] = NORMAL
			self.photo1 = tk.PhotoImage(file='lifebar.png')
			self.View1 = Label(root, image=self.photo1)

		self.LifeButton.grid(row=2, column=0)
		self.View1.grid(row=2, column=1, sticky='w')

		# Emptybar ----------------------------------------------------------------------
		if not os.path.isfile('emptybar.png'):
			self.View2['text'] = 'emptybar.png not found!'
		elif int(Image.open("emptybar.png").size[0]) != 106:
			self.View2['text'] = 'Image width is not 106!'
		elif int(Image.open("emptybar.png").size[1]) > 12:
			self.View2['text'] = "Image height is too large!"
		else:
			self.EmptyButton['state'] = NORMAL
			self.photo2 = tk.PhotoImage(file='emptybar.png')
			self.View2 = Label(root, image=self.photo2)

		self.EmptyButton.grid(row=3, column=0)
		self.View2.grid(row=3, column=1, sticky='w')

		# Extrabar ----------------------------------------------------------------------
		if not os.path.isfile('extrabar.png'):
			self.View3['text'] = 'extrabar.png not found!'
		elif int(Image.open("extrabar.png").size[0]) != 104:
			self.View3['text'] = 'Image width is not 104!'
		elif int(Image.open("extrabar.png").size[1]) > 12:
			self.View3['text'] = "Image height is too large!"
		else:
			self.ExtraButton['state'] = NORMAL
			self.photo3 = tk.PhotoImage(file='extrabar.png')
			self.View3 = Label(root, image=self.photo3)

		self.ExtraButton.grid(row=4, column=0)
		self.View3.grid(row=4, column=1, sticky='w')
		
# The function below uses Pillow library to cut the images.
def barCut(barfile):
	p1.removeLabel()
	if not os.path.exists(barfile):
		os.mkdir(barfile)
	original = Image.open(f"{barfile}.png")
	width, height = original.size # Get dimensions
	if barfile == 'emptybar':
		# EmptyBar ------------------------------------------
		xpos = 0
		for S in range(24, 128):
			cropped = original.crop((xpos, 0, width, height))
			# Add number 0 to filenames with two digits:
			if S >= 100:
				cropped.save(f'emptybar/{S}.png')
				print(f'{S} created')
			else:
				cropped.save(f'emptybar/0{S}.png')
				print(f'0{S} created')
			xpos+=1

		# Others --------------------------------------------
	else:
		for G in range(24, 128):
			cropped = original.crop((0, 0, width, height))
			# Add number 0 to filenames with two digits:
			if G >= 100:
				cropped.save(f'{barfile}/{G}.png')
				print(G,'created')
			else:
				cropped.save(f'{barfile}/0{G}.png')
				print(f'0{G} created')
			width-=1
	p1.changeText('DONE!').grid(row=7, columnspan=2)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def get_concat_v():
	# This script creates an image with indexed palette of three images.
	# Credits to nkmk for part of the code:
	# https://note.nkmk.me/en/python-pillow-concat-images/

	myPalette=[]
	another = ''
	p1.removeLabel()
	im1 = Image.open('lifebar.png')
	im2 = Image.open('emptybar.png')
	im3 = Image.open('extrabar.png')
	dst = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height))

	# Paste all images in one
	dst.paste(im1, (0, 0))
	dst.paste(im2, (0, im1.height))
	dst.paste(im3, (0, int(im1.height+im2.height)))
	converted = dst.convert('P', palette=Image.ADAPTIVE, colors=255)
	
	# Get all color data from image and remove unnecessary characters.
 	# The result is only numbers and spaces, that will be concatenate in the var "another".
	for G in converted.convert('RGB').getcolors():
		another += str(G)[:-1][1:].replace("(","").replace(")"," ").replace(",","")

	# Append only RGB color values from string "another" to array "myPalette".
	# The "[:-1]" removes the blank space in the end of string "another".
	count = 1
	for G in another[:-1].split(" "):
		if count != 1:
			myPalette.append(int(G))
		count+=1
		if count == 5:
			count = 1

	# Add transparent collor (RGB:0,0,0) to first index of palette:
	for G in range(3):
		myPalette.insert(G, 0)

	# Print all palette values:
	count = 3
	print('Palette colors (RGB):')
	for G in range(int(len(myPalette))//3):
		print(f'Color {G}: {myPalette[count-3]},{myPalette[count-2]},{myPalette[count-1]}')
		count+=3

	# Create a new image to receive the palette and be saved:
	p_img = Image.new('P', (16, 16))
	p_img.putpalette(myPalette)
	p_img.save('PALETTE.png')

	p1.changeText('Image created!').grid(row=7, columnspan=2)

#================= HOME ==========================
p1 = LBC()

Label(root, text='SORR LIFEBAR CUTTER v1.4 by Chavyn\n').grid(row=0, columnspan=2, ipadx=25)
Label(root, text='What do you want to crop?\n').grid(row=1, columnspan=2)

# -----------------------------------------------------------------------

p1.myBottoms()

Label(root, text=' ').grid(row=5, columnspan=2)

# Palette
paleteButton=Button(root, command=get_concat_v, text="Create image with indexed palette", state=NORMAL)

# Check if files exist
for G in ('life','empty','extra'):
	if not os.path.isfile(f'{G}bar.png'):
		paleteButton['state']=DISABLED

paleteButton.grid(row=6, columnspan=2)

# Final text
p1.getFinalText().grid(row=7, columnspan=2)

root.mainloop()