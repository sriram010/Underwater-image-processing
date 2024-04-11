# Importing numpy and opencv
import numpy as np
import cv2

# Defineing a function for adaptive histogram transform
def AdaptiveHistogramTransform(image):
    # Converting the image from RGB to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    # Splitting the HSV channels
    h, s, v = cv2.split(hsv)
    # Getting the mean value of the V channel
    mean_v = np.mean(v)
    # Defining the epsilon value
    epsilon = 10
    # Defining the piecewise linear function for histogram transform
    def transform(x):
        if x < mean_v - epsilon:
            return 100 * x / (mean_v - epsilon)
        elif abs(x - mean_v) <= epsilon:
            return x - mean_v + 120
        else:
            return 115 + 140 * (x - mean_v - epsilon) / (255 - mean_v - epsilon)
    # Applying the transform function to the V channel
    v = np.vectorize(transform)(v)
    # Clipping the values to the range [0, 255]
    v = np.clip(v, 0, 255).astype(np.uint8)
    # Merging the HSV channels
    hsv = cv2.merge([h, s, v])
    # Converting the image back to RGB color space
    image = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    print ("Successfully completed Adaptive Histogram Transform")

    # Returning the transformed image
    return image