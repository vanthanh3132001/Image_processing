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
    H1 = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])

    H2 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    H3 = np.array([[1, -2, 1],
                   [-2, 4, -2],
                   [1, -2, 1]])
    # gauss = 1.0 / 57 * np.array(
    #     [[0, 1, 2, 1, 0],
    #      [1, 3, 5, 3, 1],
    #      [2, 5, 9, 5, 2],
    #      [1, 3, 5, 3, 1],
    #      [0, 1, 2, 1, 0]])
    gauss = 1.0 / 16 * np.array(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]
         ])
    # Loc theo gauss
    # for i in range(img.size[0] - 2):  # img_new.size[0] = width, img_new.size[1]=height
    #     for j in range(img.size[1] - 2):
    #         _r = 0
    #         _b = 0
    #         _g = 0
    #         for k in np.arange(-1, 2):
    #             for l in np.arange(-1, 2):
    #                 r, b, g = pixels[i + k, j + l]
    #                 _r = _r + (r) * gauss[1 + k][1 + l]
    #                 _b = _b + (b) * gauss[1 + k][1 + l]
    #                 _g = _g + (g) * gauss[1 + k][1 + l]
    #
    #         pixels[i, j] = (round(_r), round(_b), round(_g), 255)
    for i in range(img_newX.size[0] - 1):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_newX.size[1] - 1):
            _rx = _bx = _gx=0
            _ry = _by = _gy = 0
            _rxy=0


            for k in np.arange(-1,2):
                for l in np.arange(-1, 2):
                    r, b, g = pixels[i + k, j + l]
                    _rx = _rx + r*H1[1-k][1-l]
                    _ry = _ry + r * H2[1-k][1-l]
                    _rxy = _rxy+r*H3[1-k][1-l]
            _rx = round(_rx)
            _ry = round(_ry)
            _rxy = round(_rxy)



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

    plt.title(' H1 filtering'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(img_newY, cmap='gray')

    plt.title(' H2 filtering'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(img_newXY, cmap='gray')

    plt.title('H3 filtering'), plt.xticks([]), plt.yticks([])

    plt.show()