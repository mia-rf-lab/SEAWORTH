from PIL import Image
import os

for img_name in ['pho_3.png', 'pho_4.png']:
    path = f"/Users/mia/Desktop/SEAWORTH/web/assets/{img_name}"
    if os.path.exists(path):
        with Image.open(path) as img:
            print(f"{img_name}: {img.size}, mode: {img.mode}")
