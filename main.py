# Importing all modules
import cv2
from red_channel_compensation import RedChannelCompensation
from white_balance import WhiteBalance
from retinex_with_dense_pixels import RetinexWithDensePixels
from adaptive_histogram_transform import AdaptiveHistogramTransform

# Adding the imput image path
image_path = "TestImages/102_img_.png"  
image = cv2.imread(image_path)
alpha = 1 
window_size = 5

# Calling all the image processing functions
compensated_image = RedChannelCompensation(image, alpha, window_size)
white_balanced_image = WhiteBalance(compensated_image)
retinex_image = RetinexWithDensePixels(white_balanced_image)
final_image = AdaptiveHistogramTransform(retinex_image)

# Saving the output image path
output_path = "OutputImages/processed_image.png"
cv2.imwrite(output_path, compensated_image)

print(f"Final output image saved to {image_path}. Processed image saved as {output_path}.")