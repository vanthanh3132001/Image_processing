from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
def median(lst):
    n = len(lst)
    s = sorted(lst)
    if n % 2 == 0:
        return  s[(int)(n/2)]
    else:
        return  s[(int)(n/2+1)]

if __name__ == "__main__":

    # Loc theo trung binh
    img = Image.open('salt_noise.png')
    pixels = img.load()
    img_new = Image.new(img.mode, img.size)
    pixels_new = img_new.load()

    for i in range(img_new.size[0] - 2):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_new.size[1] - 2):
            _r = 0
            _b = 0
            _g = 0
            for k in np.arange(-2, 3):
                for l in np.arange(-2, 3):
                    r, b, g = pixels[i + k, j + l]
                    _r = _r + r
                    _b = _b + b
                    _g = _g + g
            _r = round(_r / 25)
            _b = round(_b / 25)
            _g = round(_g / 25)
            pixels_new[i, j] = (_r, _b, _g, 255)

    # Loc theo trung vi
    img_new_tv = Image.new(img.mode, img.size)
    pixels_new_tv = img_new_tv.load()
    for i in range(img_new_tv.size[0] - 1):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_new_tv.size[1] - 1):
            _r = 0
            _b = 0
            _g = 0
            a=[]
            b1=[]
            c=[]
            for k in np.arange(-1, 2):
                for l in np.arange(-1, 2):
                    r, b, g = pixels[i + k, j + l]
                    a.append(r)
                    b1.append(b)
                    c.append(g)
            _r = median(a)
            _b = median(b1)
            _g = median(c)
            pixels_new_tv[i, j] = (_r, _b, _g, 255)
            a.clear()
            b1.clear()
            c.clear()

    #Show
    # images = [img, img_new_tv,img_new]
    # widths, heights = zip(*(i.size for i in images))
    #
    # total_width = sum(widths)
    # max_height = max(heights)
    #
    # new_im = Image.new(img.mode, (total_width, max_height))
    #
    # x_offset = 0
    # for im in images:
    #     new_im.paste(im, (x_offset, 0))
    #     x_offset += im.size[0]

    # new_im.show()
    # plt.subplot(221), plt.imshow(img), plt.title('Original image')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222), plt.imshow(img_new_tv), plt.title('Median')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223), plt.imshow(img_new), plt.title('Normalized Box Filter')
    # plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')

    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(img_new_tv, cmap='gray')

    plt.title('Median'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(img_new, cmap='gray')

    plt.title('Normalized Box Filter'), plt.xticks([]), plt.yticks([])

    plt.show()


