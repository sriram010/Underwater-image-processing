# Importing numpy and opencv
import numpy as np
import cv2

# Defining a function to implement illuminance improvement by retinex with dense pixels
def RetinexWithDensePixels(image):
    # Converting the image from BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Extracting the value component
    v = hsv[:, :, 2]
    # Getting the height and width of the image
    h, w = v.shape
    # Initializing the illumination component
    l = np.zeros_like(v, dtype=np.float32)
    # Defining the eight directions for the path selection
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # Defining the step size for each iteration
    step = 1
    # Defining the number of iterations
    n_iter = int(np.log2(min(h, w)))
    # Looping over the eight directions
    for d in directions:
        # Looping over the iterations
        for i in range(n_iter):
            # Calculating the offset for the current iteration
            offset = step * (2 ** i)
            # Looping over the rows of the image
            for x in range(h):
                # Looping over the columns of the image
                for y in range(w):
                    # Calculating the coordinates of the next pixel along the direction
                    x_next = x + d[0] * offset
                    y_next = y + d[1] * offset
                    # Checking if the coordinates are valid
                    if 0 <= x_next < h and 0 <= y_next < w:
                        # Updating the illumination component by comparing the pixel values
                        l[x, y] = max(l[x, y], v[x, y] - v[x_next, y_next])
    # Averaging the illumination component over the eight directions
    l = l / 8
    # Normalizing the illumination component to [0, 255]
    l = cv2.normalize(l, None, 0, 255, cv2.NORM_MINMAX)
    # Calculating the reflection component by subtracting the illumination component from the value component
    r = v - l
    # Replacing the value component with the reflection component
    hsv[:, :, 2] = r
    # Converting the image back to BGR color space
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    print ("Successfully completed Retinex With Dense Pixels")

    # Returning the result
    return result