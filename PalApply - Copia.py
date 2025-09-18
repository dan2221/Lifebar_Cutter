from PIL import Image
import os
import glob

# --- CONFIGURATION ---
PALETTE_FILE = "i_view_palette.pal"  # Path to your palette file
FOLDERS = ["lifebar", "emptybar", "extrabar"]  # Folders to process
IMAGE_EXTENSIONS = (".png", ".bmp")  # Supported image formats

# --- LOAD PALETTE ---
palette = []
with open(PALETTE_FILE) as pal_file:
    lines = pal_file.readlines()
    for line in lines[3:]:  # Skip JASC-PAL header
        parts = line.strip().split()
        if len(parts) == 3:
            palette.extend(map(int, parts))

# Ensure palette is 768 values (256 colors * 3 channels)
palette = palette[:768] + [0]*(768 - len(palette))

# --- CREATE PALETTE IMAGE ---
pal_img = Image.new("P", (1, 1))
pal_img.putpalette(palette)

# --- PROCESS EACH FOLDER ---
for folder in FOLDERS:
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        continue
    # Find all matching image files
    for ext in IMAGE_EXTENSIONS:
        for img_path in glob.glob(os.path.join(folder, f"*{ext}")):
            try:
                img = Image.open(img_path).convert("RGB")
                quantized = img.quantize(palette=pal_img, dither=Image.NONE)
                quantized.save(img_path)
                print(f"Palette applied: {img_path}")
            except Exception as e:
                print(f"Failed for {img_path}: {e}")

print("All done!")