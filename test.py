import sys
from PIL import Image

img = Image.open('img_1.png')
pixels = img.load()
# Trong rgb màu xám (đen trắng) là màu có r=g=b trong 1 pixel
new_img = Image.new(img.mode, img.size)
pixels_new = new_img.load()
for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
        r, b, g = pixels[i,j]
        avg = int(round((r + b + g) / 3))
        pixels_new[i,j] = (avg, avg, avg, 0)
# img.show()
# new_img.show()

images = [img,new_img]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new(img.mode, (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.show()

