from PIL import Image, ImageFilter
import os

input_folder = 'pictures'
output_folder = 'picturefilter'
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(('.jpg', '.png')):
        path = os.path.join(input_folder, file)
        img = Image.open(path)
        filtered_img = img.filter(ImageFilter.SHARPEN)

        result_path = os.path.join(output_folder, f'filtered {file}')
        filtered_img.save(result_path)

print("Изображения сохранены")