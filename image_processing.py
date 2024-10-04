from PIL import Image, ImageEnhance
import numpy as np
import time

## This method changes the hue with numpy, but will remove the transprarency
# 255 gives the normal picture
def adjust_hue(image, shift):
    hsv_image = image.convert('HSV')
    numpy_image = np.array(hsv_image)

    # adjust hue with shift and modulo with 256 for color space (0-255)
    numpy_image[..., 0] = (numpy_image[..., 0].astype(int) + shift) % 256
    adjusted_image = Image.fromarray(numpy_image, mode='HSV').convert('RGB')
    return adjusted_image

image = Image.open('mr_saturn.png')

logo = image.resize((int(image.width / 2), int(image.height / 2)))
image = image.resize((400, 400))

for x in range(0, 4):
    copyable = logo.copy()
    copyable = adjust_hue(copyable, x * 32)

    for y in range(0, 4):
        pos = (int(x * 50 + (x * 50 if x > 0 else 0)), int (y * 50 + (y * 50 if y > 0 else 0)))
        print(f"Pos:{x * 50 + (x * 50 if x > 0 else 0)}, {y * 50 + (y * 50 if y > 0 else 0)}")
        image.paste(copyable, pos)

image.show()

time.sleep(5)