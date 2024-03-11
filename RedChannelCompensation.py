# Importing numpy and opencv
import numpy as np
import cv2

# Defining a function to perform red channel compensation
def red_channel_compensation(image, alpha, window_size):
    # Converting the image to float32
    image = image.astype(np.float32)
    # Spliting the image into RGB channels
    B, G, R = cv2.split(image)
    # Initializing the compensated red channel
    R_comp = np.zeros_like(R)
    # Getting the image's height and width
    height, width = image.shape[:2]
    # Getting the half window size
    half = window_size // 2
    # Padding the image borders with zeros
    image = cv2.copyMakeBorder(image, half, half, half, half, cv2.BORDER_CONSTANT, value=0)
    # Looping over the image pixels
    for i in range(height):
        for j in range(width):
            # Getting the local window of the image
            window = image[i:i+window_size, j:j+window_size]
            # Getting the mean value of the green and blue channels in the window
            mean_G = np.mean(window[:, :, 1])
            mean_B = np.mean(window[:, :, 2])
            # Computing the compensated red value according to equation in the paper
            R_comp[i, j] = R[i, j] + (alpha * mean_G + (1 - alpha) * mean_B - R[i, j]) * (alpha * G[i, j] + (1 - alpha) * B[i, j]) / (R[i, j] + G[i, j] + B[i, j])
    # Clipping the compensated red channel to the range [0, 255]
    R_comp = np.clip(R_comp, 0, 255)
    # Merging the RGB channels
    image = cv2.merge((B, G, R_comp))
    # Converting the image back to uint8
    image = image.astype(np.uint8)
    # Returning the compensated image
    
    print ("Successfully completed Red Channel Compensation")

    return image