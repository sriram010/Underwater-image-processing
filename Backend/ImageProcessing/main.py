# Importing all modules
import cv2 
import sys
from red_channel_compensation import RedChannelCompensation
from white_balance import WhiteBalance
from retinex_with_dense_pixels import RetinexWithDensePixels
from adaptive_histogram_transform import AdaptiveHistogramTransform
from measures import CalculateEntropy

# Adding the imput image path
image_path =input()
image = cv2.imread(image_path)
alpha = 1 
window_size = 5

# Calling all the image processing functions
compensated_image = RedChannelCompensation(image, alpha, window_size)
white_balanced_image = WhiteBalance(compensated_image)
retinex_image = RetinexWithDensePixels(white_balanced_image)
final_image = AdaptiveHistogramTransform(retinex_image)

# Saving the output image path
output_path = "E:/mini_project/Underwater-image-processing/Frontend/public/processed_image.png"
cv2.imwrite(output_path, compensated_image)
print(f"Final output image saved to {image_path}. Processed image saved as {output_path}.")

entropy_value = CalculateEntropy(image_path)
print(f"Entropy of {image_path}: {entropy_value:.4f}")