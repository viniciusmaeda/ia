import cv2
from matplotlib import pyplot as plt

image = cv2.imread('./assets/bolachas.png', 0)

ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

plt.imshow(th1, 'gray')

# define image title
plt.title('THRESH_BINARY', fontsize=8)
# remove x and y label
plt.xticks([]), plt.yticks([])

plt.show()