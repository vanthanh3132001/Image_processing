from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
def scale_to_0_255(img):
    min_val = np.min(img)
    max_val = np.max(img)
    new_img = (img - min_val) / (max_val - min_val) # 0-1
    new_img *= 255
    return new_img




if __name__ == "__main__":
    # load data
    img = Image.open('img_4.png')
    pixels = img.load()

    img_newX = Image.new(img.mode, img.size)
    pixels_newX = img_newX.load()
    img_newY = Image.new(img.mode, img.size)
    pixels_newY = img_newY.load()
    img_newXY = Image.new(img.mode, img.size)
    pixels_newXY = img_newXY.load()
    img_newC = Image.new(img.mode, img.size)
    pixels_newC = img_newC.load()
    gauss = 1.0 / 57 * np.array(
        [[0, 1, 2, 1, 0],
         [1, 3, 5, 3, 1],
         [2, 5, 9, 5, 2],
         [1, 3, 5, 3, 1],
         [0, 1, 2, 1, 0]])
    sobelX = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])

    sobelY = np.array([[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]])
    # Loc theo gauss
    for i in range(img.size[0] - 2):  # img_new.size[0] = width, img_new.size[1]=height
        for j in range(img.size[1] - 2):
            _r = 0
            _b = 0
            _g = 0
            for k in np.arange(-2, 3):
                for l in np.arange(-2, 3):
                    r, b, g = pixels[i + k, j + l]
                    _r = _r + (r) * gauss[2 + k][2 + l]
                    _b = _b + (b) * gauss[2 + k][2 + l]
                    _g = _g + (g) * gauss[2 + k][2 + l]

            pixels[i, j] = (round(_r), round(_b), round(_g), 255)
    for i in range(img_newX.size[0] - 1):  # img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_newX.size[1] - 1):
            _rx = _bx = _gx = 0
            _ry = _by = _gy = 0
            _rxy = 0

            for k in np.arange(-1, 2):
                for l in np.arange(-1, 2):
                    r, b, g = pixels[i + k, j + l]
                    _rx = _rx + r * sobelX[1 - k][1 - l]
                    _ry = _ry + r * sobelY[1 - k][1 - l]

            _rx = round(_rx)
            _ry = round(_ry)
            _rxy = round(np.sqrt(_rx * _rx + _ry * _ry))

            pixels_newX[i, j] = (_rx, _rx, _rx, 0)
            pixels_newY[i, j] = (_ry, _ry, _ry, 0)
            pixels_newXY[i, j] = (_rxy, _rxy, _rxy, 0)
    scale_to_0_255(img_newX)
    scale_to_0_255(img_newY)
    Grad = np.degrees(np.arctan2(img_newX, img_newY))
    Grad = np.abs(Grad)
    Grad[Grad <= 22.5] = 0
    Grad[Grad >= 157.5] = 0
    Grad[(Grad > 22.5) * (Grad < 67.5)] = 45
    Grad[(Grad >= 67.5) * (Grad <= 112.5)] = 90
    Grad[(Grad > 112.5) * (Grad <= 157.5)] = 135

    for i in range(img_newX.size[0] - 1):  # img_new.size[0] = width, img_new.size[1]=height
        for j in range(img_newX.size[1] - 1):
            if ((Grad[i, j][0] >= -22.5 and Grad[i, j][0] <= 22.5) or (Grad[i, j][0] <= -157.5 and Grad[i, j][0] >= 157.5)):
                if ((pixels_newXY[i, j][0] > pixels_newXY[i, j + 1][0]) and (pixels_newXY[i, j][0]  > pixels_newXY[i, j - 1][0] )):
                    NMS = pixels_newXY[i, j][0]
                else:
                    NMS = 0
            if ((Grad[i, j][0] >= 22.5 and Grad[i, j][0] <= 67.5) or (Grad[i, j][0] <= -112.5 and Grad[i, j][0] >= -157.5)):
                if ((pixels_newXY[i, j][0]  > pixels_newXY[i + 1, j + 1][0] ) and (pixels_newXY[i, j][0]  > pixels_newXY[i - 1, j - 1][0] )):
                    NMS = pixels_newXY[i, j][0]
                else:
                    NMS = 0
            if ((Grad[i, j][0] >= 67.5 and Grad[i, j][0] <= 112.5) or (Grad[i, j][0] <= -67.5 and Grad[i, j][0] >= -112.5)):
                if ((pixels_newXY[i, j][0]  > pixels_newXY[i + 1, j][0] ) and (pixels_newXY[i, j][0]  > pixels_newXY[i - 1, j][0] )):
                    NMS = pixels_newXY[i, j][0]
                else:
                    NMS = 0
            if ((Grad[i, j][0] >= 112.5 and Grad[i, j][0] <= 157.5) or (Grad[i, j][0] <= -22.5 and Grad[i, j][0] >= -67.5)):
                if ((pixels_newXY[i, j][0]  > pixels_newXY[i + 1, j - 1][0] ) and (pixels_newXY[i, j][0]  > pixels_newXY[i - 1, j + 1][0] )):
                    NMS = pixels_newXY[i, j][0]
                else:
                    NMS = 0
            pixels_newC[i, j] = (NMS, NMS, NMS, 0)

    # show
    # Grad = np.degrees(np.arctan2(_ry, _rx))

    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')

    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(img_newC, cmap='gray')

    plt.title(' Candy edge'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(img_newXY, cmap='gray')

    plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

    plt.show()
