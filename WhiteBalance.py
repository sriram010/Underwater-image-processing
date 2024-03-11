# Importing numpy
import numpy as np
# Assuming the input image is in RGB format and stored in a variable named img

# Defining a function for white balance based on the maximal response assumption
def white_balance(img):
    # Getting the maximum values of each channel
    r_max = np.max(img[:,:,0])
    g_max = np.max(img[:,:,1])
    b_max = np.max(img[:,:,2])

    # Computing the scaling factors for each channel
    r_scale = r_max / 255
    g_scale = g_max / 255
    b_scale = b_max / 255

    # Applying the scaling factors to the image
    img[:,:,0] = img[:,:,0] / r_scale
    img[:,:,1] = img[:,:,1] / g_scale
    img[:,:,2] = img[:,:,2] / b_scale

    # Clipping the values to the range [0, 255]
    img = np.clip(img, 0, 255)

    # Converting the image to uint8 type
    img = img.astype(np.uint8)

    print ("Successfully completed White Balancing")

    # Returning the white balanced image
    return img