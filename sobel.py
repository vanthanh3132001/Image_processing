from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
if __name__ == "__main__":
    #load data
    img = Image.open('img_2.png')
    pixels = img.load()
    #gray_image
    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         r, b, g = pixels[i, j]
    #         avg = (round((r + b + g) / 3))
    #         pixels[i, j] = (avg, avg, avg, 0)
    #create new image
    img_newX= Image.new(img.mode, img.size)
    pixels_newX = img_newX.load()
    img_newY = Image.new(img.mode, img.size)
    pixels_newY = img_newY.load()
    img_newXY = Image.new(img.mode, img.size)
    pixels_newXY = img_newXY.load()
    sobelX = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])

    sobelY = np.array([[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]])
    for i in range(img_newX.size[0] - 1):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_newX.size[1] - 1):
            _rx = _bx = _gx=0
            _ry = _by = _gy = 0
            _rxy=0

            # r, b, g = pixels[i , j  ]
            # r1, b1, g1 = pixels[i +1, j ]
            # _rx=r-r1
            # _bx=b-b1
            # _gx=g-g1
            for k in np.arange(-1,2):
                for l in np.arange(-1, 2):
                    r, b, g = pixels[i + k, j + l]
                    _rx = _rx + r*sobelX[1-k][1-l]
                    # _bx = _bx + b*sobelX[1+k][1+l]
                    # _gx = _gx + g*sobelX[1+k][1+l]
                    _ry = _ry + r * sobelY[1-k][1-l]
                    # _by = _by + b * sobelY[1 + k][1 + l]
                    # _gy = _gy + g * sobelY[1 + k][1 + l]
            _rx = round(_rx)
            # _bx = round(_bx)
            # _gx = round(_gx)
            _ry = round(_ry)
            # _by = round(_by)
            # _gy = round(_gy)
            _rxy=round(np.sqrt(_rx*_rx+_ry*_ry))

            pixels_newX[i, j] = (_rx, _rx, _rx, 0)
            pixels_newY[i, j] = (_ry, _ry, _ry, 0)
            pixels_newXY[i, j] = (_rxy, _rxy, _rxy, 0)



    #show
    # images = [img, img_newX, img_newY]
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

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')

    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(img_newX, cmap='gray')

    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(img_newY, cmap='gray')

    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(img_newXY, cmap='gray')

    plt.title('Sobel'), plt.xticks([]), plt.yticks([])

    plt.show()
