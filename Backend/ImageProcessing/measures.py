import numpy as np
import cv2

def CalculateEntropy(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Normalize the histogram
    hist /= hist.sum()

    # Calculate entropy
    entropy = -np.sum(hist * np.log2(hist + 1e-10))

    return entropy