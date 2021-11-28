import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('img_3.png')

blur = cv.bilateralFilter(img,9,75,75)

# Convert color from bgr (OpenCV default) to rgb
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

# Display
plt.subplot(121),plt.imshow(img_rgb),plt.title('Gauss Noise')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur_rgb),plt.title('Gauss Noise - Blurred')
plt.xticks([]), plt.yticks([])

plt.show()