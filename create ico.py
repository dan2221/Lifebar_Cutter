from PIL import Image

img = Image.open("icon.png")
sizes = [(256,256), (128,128), (64,64), (48,48), (32,32), (24,24), (16,16)]
img.save("myicon.ico", sizes=sizes)