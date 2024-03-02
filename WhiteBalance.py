# Assuming the input image is in RGB format and stored in a variable named img
import numpy as np
import cv2

# Define a function for white balance based on the maximal response assumption
def white_balance(img_path):
    # Get the maximum values of each channel
    img = cv2.imread(img_path)
    r_max = np.max(img[:,:,0])
    g_max = np.max(img[:,:,1])
    b_max = np.max(img[:,:,2])

    # Compute the scaling factors for each channel
    r_scale = r_max / 255
    g_scale = g_max / 255
    b_scale = b_max / 255

    # Apply the scaling factors to the image
    img[:,:,0] = img[:,:,0] / r_scale
    img[:,:,1] = img[:,:,1] / g_scale
    img[:,:,2] = img[:,:,2] / b_scale

    # Clip the values to the range [0, 255]
    img = np.clip(img, 0, 255)

    # Convert the image to uint8 type
    img = img.astype(np.uint8)

    # Return the white balanced image
    return img


# Example of using the function
# output_image = white_balance(r"D:\mini project\practise\compensated_image.jpg")
# output_image_path = "D:\mini project\practise\white_balanced_image.jpg"
# cv2.imwrite(output_image_path, output_image)
# print(f"Compensated image saved as {output_image_path}")