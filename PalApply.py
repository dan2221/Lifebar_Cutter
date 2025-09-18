from PIL import Image
import os
import glob

def apply_palette_to_folders(
    palette_file="palette.pal",
    folders=None,
    image_extensions=(".png", ".bmp")
):
    if folders is None:
        folders = ["lifebar", "emptybar", "extrabar"]

    palette = []
    with open(palette_file) as pal_file:
        lines = pal_file.readlines()
        for line in lines[3:]:
            parts = line.strip().split()
            if len(parts) == 3:
                palette.extend(map(int, parts))
    palette = palette[:768] + [0]*(768 - len(palette))
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette(palette)

    for folder in folders:
        if not os.path.isdir(folder):
            print(f"Folder not found: {folder}")
            continue
        for ext in image_extensions:
            for img_path in glob.glob(os.path.join(folder, f"*{ext}")):
                try:
                    img = Image.open(img_path).convert("RGB")
                    quantized = img.quantize(palette=pal_img, dither=Image.NONE)
                    quantized.save(img_path)
                    print(f"Palette applied: {img_path}")
                except Exception as e:
                    print(f"Failed for {img_path}: {e}")
    print("All done!")