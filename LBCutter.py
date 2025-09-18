# Files and folders management
from os import mkdir
import os.path
from pathlib import Path
import glob

# Graphical User Interface (GUI)
from tkinter import *
from tkinter import ttk
import tkinter as tk

# Image manipulation
from PIL import ImageTk,Image

# txt file manipulation
import shutil

# Access links
import webbrowser

# PalApply
from PalApply import apply_palette_to_folders

version = "25.09.17"
root = Tk()
root.title('SorR Lifebar Cutter')
root.geometry("310x270")

root.resizable(width=False, height=False)

# ------- FUNCTIONS -------------------------------
class LBC:
	def __init__(self):
		self.LifeButton = Button(root, command=lambda: barCut("Lifebar"), text ="Lifebar", width=10, state=DISABLED)
		self.EmptyButton = Button(root, command=lambda: barCut('emptybar'), text ="Emptybar", width=10, state=DISABLED)
		self.ExtraButton = Button(root, command=lambda: barCut('extrabar'), text ="Extrabar", width=10, state=DISABLED)
		self.PlayerButton = Button(root, command=playerBarMaker, text ="Playerbar", width=10, state=DISABLED)
		self.View1 = Label(root, text=' ', fg='#f00')
		self.View2 = Label(root, text=' ', fg='#f00')
		self.View3 = Label(root, text=' ', fg='#f00')
		self.View4 = Label(root, text=' ', fg='#f00')

		self.photo1 = ""
		self.photo2 = ""
		self.photo3 = ""
		self.photo4 = ""
		self.Texto_final = Label(root, text='\nChoose an option!\n')

	# Get data
	def getFinalText(self):
		return self.Texto_final

	def changeText(self, mytext):
		self.Texto_final = Label(root, text=f'\n{mytext}\n', fg='#00f')
		return self.Texto_final

	def removeLabel(self):
		self.Texto_final.after(9, self.Texto_final.destroy())

	def myBottoms(self):
		if glob.glob("names/*.png"):
		    print(glob.glob("names/*.png"))
		else:
		    print('There are no files')
		# Lifebar -----------------------------------------------------------------------
		if not os.path.isfile('lifebar.png'):
			self.View1['text'] = 'lifebar.png not found!'
		elif Image.open("lifebar.png").size[0] != 104:
			self.View1['text'] = 'Image width is not 104!'
		elif Image.open("lifebar.png").size[1] > 12:
			self.View1['text'] = "Image height is too large!"
		else:
			self.LifeButton['state'] = NORMAL
			self.photo1 = tk.PhotoImage(file='lifebar.png')
			self.View1 = Label(root, image=self.photo1)

		self.LifeButton.grid(row=2, column=0)
		self.View1.grid(row=2, column=1, sticky='w')

		# Emptybar button ----------------------------------------------------------------------
		if not os.path.isfile('emptybar.png'):
			self.View2['text'] = 'emptybar.png not found!'
		elif Image.open("emptybar.png").size[0] < 105:
			self.View1['text'] = 'Image width is less than 105!'
		elif Image.open("emptybar.png").size[1] > 12:
			self.View2['text'] = "Image height is too large!"
		else:
			self.EmptyButton['state'] = NORMAL
			self.photo2 = tk.PhotoImage(file='emptybar.png')
			self.View2 = Label(root, image=self.photo2)

		self.EmptyButton.grid(row=3, column=0)
		self.View2.grid(row=3, column=1, sticky='w')

		# Extrabar button ----------------------------------------------------------------------
		if not os.path.isfile('extrabar.png'):
			self.View3['text'] = 'extrabar.png not found!'
		elif Image.open("extrabar.png").size[0] != 104:
			self.View3['text'] = 'Image width is not 104!'
		elif Image.open("extrabar.png").size[1] > 12:
			self.View3['text'] = "Image height is too large!"
		else:
			self.ExtraButton['state'] = NORMAL
			self.photo3 = tk.PhotoImage(file='extrabar.png')
			self.View3 = Label(root, image=self.photo3)

		self.ExtraButton.grid(row=4, column=0)
		self.View3.grid(row=4, column=1, sticky='w')

		# Playerbar button ----------------------------------------------------------------------
		if not os.path.isfile('playerbar.png'):
			self.View4['text'] = 'playerbar.png not found!'
		elif not os.path.exists('names'):
			self.View4['text'] = '"names" folder not found!'
		# Simple way to check if a file exists.
		elif not glob.glob('names/*.png'):
			self.View4['text'] = 'No png found in "names"!'
		elif Image.open("playerbar.png").size[1] >= 22:
			self.View4['text'] = "Image height is too large!"
		else:
			self.PlayerButton['state'] = NORMAL
			self.photo4 = tk.PhotoImage(file='playerbar.png')
			self.View4 = Label(root, image=self.photo4)

		self.PlayerButton.grid(row=5, column=0)
		self.View4.grid(row=5, column=1, sticky='w')
		
# The function below uses Pillow library to cut the images.
def barCut(barfile):
	p1.removeLabel()
	if not os.path.exists(barfile):
		os.mkdir(barfile)
	original = Image.open(f"{barfile}.png").convert('RGB')
	width, height = original.size # Get dimensions
	if barfile == 'emptybar':
		# EmptyBar ------------------------------------------
		xpos = 0
		for S in range(24, 129):
			cropped = original.crop((xpos, 0, width, height))
			# Add number 0 to filenames with two digits:
			if S >= 100:
				cropped.save(f'emptybar/{S}.bmp')
				print(f'{S}.bmp created')
			else:
				cropped.save(f'emptybar/0{S}.bmp')
				print(f'0{S}.bmp created')
			xpos+=1

		# Others --------------------------------------------
	else:
		for G in range(24, 128):
			cropped = original.crop((0, 0, width, height))
			# Add number 0 to filenames with two digits:
			if G >= 100:
				cropped.save(f'{barfile}/{G}.bmp')
				print(f'{G}.bmp created')
			else:
				cropped.save(f'{barfile}/0{G}.bmp')
				print(f'0{G}.bmp created')
			width-=1
	p1.changeText('DONE!').grid(row=8, columnspan=2)

# This function makes players' emptybars
def playerBarMaker():
	p1.removeLabel()
	if not os.path.exists('playerbar'):
		os.mkdir('playerbar')
	original = Image.open("playerbar.png").convert('RGBA')

	# Get all files in "names" folder.
	for G in glob.glob("names/*.png"):
		# Remove unnecessary characters.
		var_pname = str(G).replace('names\\','')
		# Create a black image to paste others.
		newpbar = Image.new('RGBA', (original.width, original.height))
		# Current player name image.
		pname = Image.open(f"names/{var_pname}").convert('RGBA')

		# Apply transparency to player name image.
		# Thanks to Clay for the code:
		# https://clay-atlas.com/us/blog/2020/11/28/python-en-package-pillow-convert-background-transparent/
		newImage = []
		for item in pname.getdata():
		    if item[:3] == (0, 0, 0):
		        newImage.append((255, 255, 255, 0))
		    else:
		        newImage.append(item)

		pname.putdata(newImage)

		# Paste player name on the bar, save it and print results.
		newpbar.paste(original, (0, 0))
		newpbar.paste(pname, (18, 2), pname)
		newpbar.save(f"playerbar/{var_pname}")
		print(f"Playerbar created: {var_pname}")

	p1.changeText('Player bars done!').grid(row=8, columnspan=2)

# Thank you window
def open_love_window():
    love_win = Toplevel(root)
    love_win.title("Thanks 💖")
    love_win.geometry("340x210")
    love_win.resizable(False, False)
    Label(love_win, text=f"Developed with love by Dan Chavyn.\nVersion: {version}\n\nCheck out also:", font=("Arial", 12)).pack(pady=5)
    
    # Link 1
    link1 = Label(love_win, text="Project GitHub", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link1.pack()
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/dan2221/Lifebar_Cutter"))
    
    # Link 2
    link2 = Label(love_win, text="My YouTube channel", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link2.pack()
    link2.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.youtube.com/playlist?list=PLa-mXLTenBmKFWyTz2OeIF-b6gNuYOWzw"))

    # Link 3
    link3 = Label(love_win, text="Ko-Fi", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link3.pack()
    link3.bind("<Button-1>", lambda e: webbrowser.open_new("https://ko-fi.com/danchavyn"))

    # Link 4
    link4 = Label(love_win, text="PayPal", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link4.pack()
    link4.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.paypal.com/donate/?hosted_button_id=RK8T3UG4T2LCU"))
    
    Label(love_win, text="\n\n\nThank you for using!\n\n", font=("Arial", 10)).pack()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def get_concat_v():
	# This script creates an image with indexed palette of three images.
	# Credits to nkmk for code to paste images:
	# https://note.nkmk.me/en/python-pillow-concat-images/

	myPalette=[]
	another = ''
	p1.removeLabel()
	im1 = Image.open('lifebar.png')
	im2 = Image.open('emptybar.png')
	im3 = Image.open('extrabar.png')
	dst = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height))

	# Paste all images in one.
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

	# Add transparent collor (RGB:0,0,0) to first index of palette.
	for G in range(3):
		myPalette.insert(G, 0)

	# >>> SORT COLORS EXCEPT THE FIRST <<<
	# myPalette is currently: [0, 0, 0, R1, G1, B1, R2, G2, B2, ...]
	# Keep the first color (transparent) fixed
	transparent = myPalette[:3]
	colors = myPalette[3:]

	# Group the rest into (R, G, B) tuples
	color_tuples = [tuple(colors[i:i+3]) for i in range(0, len(colors), 3)]

	# Sort the tuples (by default: R, then G, then B)
	color_tuples_sorted = sorted(color_tuples)

	# Flatten back to a list and rejoin with the transparent color at the front
	myPalette = list(transparent) + [value for rgb in color_tuples_sorted for value in rgb]

	##################################################


	# Create .pal file.
	Path('palette.pal').touch()
	arquivo_pal = open('palette.pal', 'w')
	arquivo_pal.write("JASC-PAL\n0100\n256\n")

	# Print all palette values and add to palette file.
	count = 3
	print('Palette colors (RGB):')
	for G in range(len(myPalette)//3):
		print(f'Color {G}: {myPalette[count-3]},{myPalette[count-2]},{myPalette[count-1]}')
		arquivo_pal.write(f'{myPalette[count-3]} {myPalette[count-2]} {myPalette[count-1]}\n')
		count += 3

	# Add black color (RGB:0,0,0) to remain space in the palette.
	if len(myPalette)//3 < 256:
		for G in range(256-len(myPalette)//3):
			arquivo_pal.write('0 0 0\n')

	p1.changeText('Palette created!').grid(row=8, columnspan=2)

	# Close the file so it can be used in the next method.
	arquivo_pal.close()

	apply_palette_to_folders()

# :::::::::::::::::::::::::::: HOME ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
p1 = LBC()

Label(root, text='Click the buttons to cut your bars into pieces.').grid(row=0, columnspan=2, ipadx=32)
Label(root, text=' ').grid(row=1, columnspan=2)

# -----------------------------------------------------------------------

p1.myBottoms()

Label(root, text=' ').grid(row=6, columnspan=2)

# Palette button.
paleteButton=Button(root, command=get_concat_v, text="Create and Apply Palette", state=NORMAL)

# Check if files exist
for G in ('life','empty','extra'):
	if not os.path.isfile(f'{G}bar.png'):
		paleteButton['state']=DISABLED

paleteButton.grid(row=7, columnspan=2)

# Final text
p1.getFinalText().grid(row=8, columnspan=2)
try:
    heart_img = PhotoImage(file="heart16x16.png")
    heart_btn = Button(root, image=heart_img, command=open_love_window, bd=0)
    heart_btn.image = heart_img  # evita garbage collection
    heart_btn.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)
    
except Exception as e:
    print("Erro ao carregar ícone:", e)

root.mainloop()