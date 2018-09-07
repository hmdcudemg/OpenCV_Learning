import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()

    dst = cv2.GaussianBlur(frame, (5, 5), 0)

    cv2.imshow('Original', frame)
    cv2.imshow('Gaussian', dst)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
