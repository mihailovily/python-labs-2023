from PIL import Image
from PIL import ImageFilter
import sys

filename = "image.jpg"


def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def save_img(img_file):
    img_file.save("new_image.jpg")


def resize_2x(img_file):
    left = img_file.width / 3
    top = img_file.height / 3
    right = 2 * img_file.width / 3
    bottom = 2 * img_file.height / 3
    cropped_img = img_file.crop((left, top, right, bottom))
    return cropped_img


def blur(img_file):
    blur_img = img_file.filter(ImageFilter.BLUR)
    return blur_img


def hires(img_file):
    sharp_img = img_file.filter(ImageFilter.SHARPEN)
    return sharp_img


while True:
    print(
        "Что сделать с изображением?\n1 - вырезать середину\n2 - блюр\n3 - резкость\n0 - выход"
    )
    manipulation = input()
    if is_number(manipulation):
        manipulation = int(manipulation)
        with Image.open(filename) as img:
            img.load()
            if manipulation == 1:
                new_img = resize_2x(img)
            elif manipulation == 2:
                new_img = blur(img)
            elif manipulation == 3:
                new_img = hires(img)
            elif manipulation == 0:
                sys.exit()
            else:
                continue
            save_img(new_img)
            print('Изображение сохранено в new_image.jpg')
    else:
        print("error")
