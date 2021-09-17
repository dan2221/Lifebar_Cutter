import os
import os.path
import shutil
import glob
from pathlib import Path
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('SorR Lifebar Cutter')
root.geometry("290x200")
root.iconbitmap('icon/cutter.ico')

# ------- FUNCTIONS -------------------------------

echo = lambda value: Label(root, text=value).pack()

def LifebarCut():
	if not os.path.exists('lifebar'):
		os.mkdir('lifebar')
	original = Image.open("lifebar.png")
	width, height = original.size # Get dimensions
	for G in range(24, 128):
		cropped = original.crop((0, 0, width, height))
		cropped.save(f'lifebar/{G}.png')
		print(G,'created')
		width-=1
	width, height = original.size # Get dimensions

def ExtrabarCut():
	if not os.path.exists('extrabar'):
		os.mkdir('extrabar')
	original = Image.open("extrabar.png")
	width, height = original.size # Get dimensions
	for G in range(24, 128):
		cropped = original.crop((0, 0, width, height))
		cropped.save(f'extrabar/{G}.png')
		print(G,'created')
		width-=1

def EmptybarCut():
	if not os.path.exists('emptybar'):
		os.mkdir('emptybar')
	original = Image.open("emptybar.png")
	width, height = original.size # Get dimensions
	xpos = 0
	for G in range(24, 128):
		cropped = original.crop((xpos, 0, width, height))
		cropped.save(f'emptybar/{G}.png')
		print(f'{G} created: {xpos},{width}')
		xpos+=1

#================= HOME ==========================
echo('SORR LIFEBAR CUTTER v1.1 by Chavyn\n')
echo('What do you want to crop?\n')

LifeButton = Button(root, text ="Lifebar", command = LifebarCut)
LifeButton.pack()

EmptyButton = Button(root, text ="Emptybar", command = EmptybarCut)
EmptyButton.pack()

ExtraButton = Button(root, text ="Extrabar", command = ExtrabarCut)
ExtraButton.pack()

root.mainloop()