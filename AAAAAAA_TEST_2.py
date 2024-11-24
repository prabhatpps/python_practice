import cv2
import numpy as np

# Reading input from STDIN
image_path = raw_input()

# Read the image
data = cv2.imread(image_path)

# 1. Horizontal Flip
data = cv2.flip(data, 1)

# Define the kernel
kernel = np.ones((4, 4), np.uint8)

# 2. Dilation - 3 iterations
data = cv2.dilate(data, kernel, iterations=3)

# 3. Erosion - 3 iterations
data = cv2.erode(data, kernel, iterations=3)

# 4. Closing
data = cv2.morphologyEx(data, cv2.MORPH_CLOSE, kernel)

# 5. Opening
data = cv2.morphologyEx(data, cv2.MORPH_OPEN, kernel)

# Convert the resultant image to grayscale
gray_image = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)

# Save the array to a text file
file_name = 'submission.txt'
np.savetxt(file_name, gray_image, fmt='%d', delimiter=',')
