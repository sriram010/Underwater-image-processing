import numpy as np
import cv2

# Define a function for adaptive histogram transform[^1^][1]
def adaptive_histogram_transform(image):
    # Convert the image from RGB to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    # Split the HSV channels
    h, s, v = cv2.split(hsv)
    # Get the mean value of the V channel
    mean_v = np.mean(v)
    # Define the epsilon value
    epsilon = 10
    # Define the piecewise linear function for histogram transform[^2^][2]
    def transform(x):
        if x < mean_v - epsilon:
            return 100 * x / (mean_v - epsilon)
        elif abs(x - mean_v) <= epsilon:
            return x - mean_v + 120
        else:
            return 115 + 140 * (x - mean_v - epsilon) / (255 - mean_v - epsilon)
    # Apply the transform function to the V channel
    v = np.vectorize(transform)(v)
    # Clip the values to the range [0, 255]
    v = np.clip(v, 0, 255).astype(np.uint8)
    # Merge the HSV channels
    hsv = cv2.merge([h, s, v])
    # Convert the image back to RGB color space
    image = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    # Return the transformed image

    print ("Successfully completed Adaptive Histogram Transform")

    return image