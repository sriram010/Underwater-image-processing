import cv2
import numpy as np

def red_channel_compensation(input_image, alpha, window_size):
    # Read the input image
    img = cv2.imread(input_image)
    cv2.imshow("image", img)

    # # Split the image into red, green, and blue channels
    # b, g, r = cv2.split(img)

    # # Calculate the mean of green and blue channels using a window
    # green_mean = cv2.blur(g, (window_size, window_size))
    # blue_mean = cv2.blur(b, (window_size, window_size))

    # # Perform the compensation for the red channel
    # compensated_red = r + alpha * (green_mean - blue_mean)

    # # Merge the compensated channels back into an image
    # compensated_img = cv2.merge((b, green_mean, compensated_red))

    # return compensated_img

# Example usage
input_image_path = "8_img.jpg"
alpha_value = 0.5
window_size_value = 5
# output_image = 
red_channel_compensation(input_image_path, alpha_value, window_size_value)

# Save the compensated image
# output_image_path = "compensated_image.jpg"
# cv2.imwrite(output_image_path, output_image)
# print(f"Compensated image saved as {output_image_path}")
