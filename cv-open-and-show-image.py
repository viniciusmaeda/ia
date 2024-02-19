# This sample will open and show a simple image.

# importing opencv library
import cv2

# imageGrayScale = cv2.imread('./assets/bolachas.png', -1) # original image
imageGrayScale = cv2.imread('./assets/bolachas.png', 0) # gray scale image
# imageGrayScale = cv2.imread('./assets/bolachas.png', 1) # color image (original)

# show image
cv2.imshow('Gray Scale Image', imageGrayScale)

# wait for a key press to close window
cv2.waitKey(0)

# destroy window
cv2.destroyAllWindows()

# create a image
cv2.imwrite('./temp/imageGrayScale.png', imageGrayScale)