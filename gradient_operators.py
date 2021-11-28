from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    #load data
    img = Image.open('img_5.png')
    pixels = img.load()

    img_newX= Image.new(img.mode, img.size)
    pixels_newX = img_newX.load()
    img_newY = Image.new(img.mode, img.size)
    pixels_newY = img_newY.load()
    img_newXY = Image.new(img.mode, img.size)
    pixels_newXY = img_newXY.load()
    sobelX = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]])

    sobelY = np.array([[-1, -1, -1],
                       [0, 0, 0],
                       [1, 1, 1]])
    for i in range(img_newX.size[0] - 1):       #img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_newX.size[1] - 1):
            _rx = _bx = _gx=0
            _ry = _by = _gy = 0
            _rxy=0

            for k in np.arange(-1,2):
                for l in np.arange(-1, 2):
                    r, b, g = pixels[i + k, j + l]
                    _rx = _rx + r*sobelX[1-k][1-l]

                    _ry = _ry + r * sobelY[1-k][1-l]

            _rx = round(_rx)

            _ry = round(_ry)

            _rxy=round(np.sqrt(_rx*_rx+_ry*_ry))

            pixels_newX[i, j] = (_rx, _rx, _rx, 0)
            pixels_newY[i, j] = (_ry, _ry, _ry, 0)
            pixels_newXY[i, j] = (_rxy, _rxy, _rxy, 0)



    #show


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')

    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(img_newX, cmap='gray')

    plt.title(' X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(img_newY, cmap='gray')

    plt.title(' Y'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(img_newXY, cmap='gray')

    plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

    plt.show()
