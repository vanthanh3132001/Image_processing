from PIL import Image
import math
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    #load data
    img = Image.open('img_2.png')
    pixels = img.load()
    img_new_gauss = Image.new(img.mode, img.size)
    pixels_new = img_new_gauss.load()

    gauss =   1.0/57 *np.array(
        [[0, 1, 2, 1, 0],
         [1, 3, 5, 3, 1],
         [2, 5, 9, 5, 2],
         [1, 3, 5, 3, 1],
         [0, 1, 2, 1, 0]])
    #Loc theo gauss
    for i in range(img_new_gauss.size[0] - 2):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_new_gauss.size[1] - 2):
            _r = 0
            _b = 0
            _g = 0
            for k in np.arange(-2, 3):
                for l in np.arange(-2, 3):
                    r, b, g = pixels[i + k, j + l]
                    _r = _r + (r) * gauss[2 + k][2 + l]
                    _b = _b + (b) * gauss[2 + k][2 + l]
                    _g = _g + (g) * gauss[2 + k][2 + l]


            pixels_new[i, j] = (round(_r), round(_b), round(_g), 255)
    #img_new_gauss.show()
    # Loc theo bo loc 2 chieu
    img_new_2c = Image.new(img.mode, img.size)
    pixels_new_2c = img_new_2c.load()

    for i in range(img_new_2c.size[0] - 2):  # img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_new_2c.size[1] - 2):
            _r = 0
            _b = 0
            _g = 0
            r0, b0, g0 = pixels[i, j]
            sumr=0
            sumb=0
            sumg=0

            for k in np.arange(-2, 3):
                for l in np.arange(-2, 3):
                    r, b, g = pixels[i + k, j + l]
                    phu=math.exp(-0.5*(k*k+l*l)/1458)
                    wr=phu*(math.exp(-0.5*(r-r0)*(r-r0)/1458))
                    wb=phu*(math.exp(-0.5*(b-b0)*(b-b0)/1458))
                    wg= phu*(math.exp(-0.5*(g-g0)*(g-g0)/1458))
                    _r = _r + r * wr
                    _b = _b + b * wb
                    _g = _g + g * wg
                    sumr+=wr
                    sumb+=wb
                    sumg+=wg

            _r = round ( _r/sumr )
            _b = round(_b /sumb)
            _g = round(_g /sumg)
            # print("...")
            # print(r0)
            # print(_r)
            # print("...")
            # print(sumr)

            pixels_new_2c[i, j] = (_r, _b, _g, 255)
    #img_new_2c.show()
    # Show
    # images = [img,img_new_2c]
    # widths, heights = zip(*(i.size for i in images))
    #
    # total_width = sum(widths)
    # max_height = max(heights)
    # new_im = Image.new(img.mode, (total_width, max_height))
    # x_offset = 0
    # for im in images:
    #     new_im.paste(im, (x_offset, 0))
    #     x_offset += im.size[0]
    #
    # new_im.show()
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')

    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(img_new_gauss, cmap='gray')

    plt.title('Gaussian'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(img_new_2c, cmap='gray')

    plt.title('Bilateral'), plt.xticks([]), plt.yticks([])

    plt.show()