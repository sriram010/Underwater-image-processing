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
print("Starting to process the input image")
compensated_image = RedChannelCompensation(image, alpha, window_size)
output_path = "E:/mini_project/Underwater-image-processing/Backend/ImageProcessing/OutputImages/red_channel_compensated_image.png"
cv2.imwrite(output_path, compensated_image)
print(f"Red Channel Compensated image saved as {output_path}.")

white_balanced_image = WhiteBalance(compensated_image)
output_path = "E:/mini_project/Underwater-image-processing/Backend/ImageProcessing/OutputImages/white_balanced_image.png"
cv2.imwrite(output_path, white_balanced_image)
print(f"White Balanced image saved as {output_path}.")

retinex_image = RetinexWithDensePixels(white_balanced_image)
output_path = "E:/mini_project/Underwater-image-processing/Backend/ImageProcessing/OutputImages/retinex_image.png"
cv2.imwrite(output_path, retinex_image)
print(f"Retinex image saved as {output_path}.")

final_image = AdaptiveHistogramTransform(retinex_image)
output_path = "E:/mini_project/Underwater-image-processing/Backend/ImageProcessing/OutputImages/adaptive_histogram_image.png"
cv2.imwrite(output_path, compensated_image)
print(f"Adaptive Histogram image saved as {output_path}.")

# Saving the output image path
output_path = "E:/mini_project/Underwater-image-processing/Frontend/public/processed_image.png"
cv2.imwrite(output_path, compensated_image)
print(f"Final output image saved to {image_path}. Processed image saved as {output_path}.")

entropy_value = CalculateEntropy(image_path)
print(f"Entropy of {image_path}: {entropy_value:.4f}")