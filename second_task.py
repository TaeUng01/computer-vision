import cv2
import numpy as np

img = cv2.imread('./cat.jpg', cv2.IMREAD_COLOR)      # BGR
img_gray = np.zeros_like(img)

for i in range(3):
    # 0.299 R + 0.587 G + 0.114 B
    img_gray[:, :, i] = 0.299 * img[:, :, 2] + 0.584 * img[:, :, 1] + 0.1148 * img[:, :, 0]



cv2.imshow('Gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()