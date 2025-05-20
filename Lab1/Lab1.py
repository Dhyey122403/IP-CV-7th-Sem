import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# URL of the image
url = 'https://images.unsplash.com/photo-1721616216040-88b305eea70d?q=80&w=2003&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

# Download the image
response = requests.get(url)
image_bytes = BytesIO(response.content)

# Read the image using OpenCV
image = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Save the original and greyscale images
cv2.imwrite('original_image.png', image)
cv2.imwrite('greyscale_image.png', image_gray)