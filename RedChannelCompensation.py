# Import numpy and opencv
import numpy as np
import cv2

# Define a function to perform red channel compensation
def red_channel_compensation(image, alpha, window_size):
    # Convert the image to float32
    image = image.astype(np.float32)
    # Split the image into RGB channels
    B, G, R = cv2.split(image)
    # Initialize the compensated red channel
    R_comp = np.zeros_like(R)
    # Get the image height and width
    height, width = image.shape[:2]
    # Get the half window size
    half = window_size // 2
    # Pad the image borders with zeros
    image = cv2.copyMakeBorder(image, half, half, half, half, cv2.BORDER_CONSTANT, value=0)
    # Loop over the image pixels
    for i in range(height):
        for j in range(width):
            # Get the local window of the image
            window = image[i:i+window_size, j:j+window_size]
            # Get the mean value of the green and blue channels in the window
            mean_G = np.mean(window[:, :, 1])
            mean_B = np.mean(window[:, :, 2])
            # Compute the compensated red value according to equation (8) in the paper
            R_comp[i, j] = R[i, j] + (alpha * mean_G + (1 - alpha) * mean_B - R[i, j]) * (alpha * G[i, j] + (1 - alpha) * B[i, j]) / (R[i, j] + G[i, j] + B[i, j])
    # Clip the compensated red channel to the range [0, 255]
    R_comp = np.clip(R_comp, 0, 255)
    # Merge the RGB channels
    image = cv2.merge((B, G, R_comp))
    # Convert the image back to uint8
    image = image.astype(np.uint8)
    # Return the compensated image
    
    print ("Successfully completed Red Channel Compensation")

    return image