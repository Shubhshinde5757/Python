from PIL import Image
import numpy as np 

img = Image.open("digit_28x28.png")
img = img.convert("L")
img = img.resize((28,28))

pixels = np.array(img)

print("Image size : ", pixels.shape)

print("pixel Value :")
print(pixels)

# 0     Pure Black
# 255   Pure White
# 50    Dark Gray
# 120   Mediam gray
# 200   Light gray
