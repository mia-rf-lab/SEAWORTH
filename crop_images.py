from PIL import Image
import os

images = ['2.jpg', '3.jpg', '4.jpg']
base_dir = '/Users/mia/Desktop/SEAWORTH/web/assets/'

for img_name in images:
    img_path = os.path.join(base_dir, img_name)
    if os.path.exists(img_path):
        with Image.open(img_path) as img:
            width, height = img.size
            # Crop 450 pixels from left, 300 pixels from top
            crop_box = (450, 300, width, height)
            cropped_img = img.crop(crop_box)
            
            new_name = img_name.replace('.jpg', '_nologo.jpg')
            new_path = os.path.join(base_dir, new_name)
            cropped_img.save(new_path, quality=90)
            print(f"Saved {new_name}")
