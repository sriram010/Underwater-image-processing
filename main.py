# Importing all modules
import cv2
from RedChannelCompensation import red_channel_compensation
from WhiteBalance import white_balance
from RetinexWithDensePixels import retinex_with_dense_pixels
from AdaptiveHistogramTransform import adaptive_histogram_transform

# Adding the imput image path
image_path = "TestImages/102_img_.png"  
image = cv2.imread(image_path)
alpha = 1 
window_size = 5

# Calling all the image processing functions
compensated_image = red_channel_compensation(image, alpha, window_size)
white_balanced_image = white_balance(compensated_image)
retinex_image = retinex_with_dense_pixels(white_balanced_image)
final_image = adaptive_histogram_transform(retinex_image)

# Saving the output image path
output_path = "OutputImages/processed_image.png"
cv2.imwrite(output_path, compensated_image)

print(f"Final output image saved to {image_path}. Processed image saved as {output_path}.")