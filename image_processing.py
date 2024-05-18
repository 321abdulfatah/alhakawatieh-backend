import cv2
import numpy as np

def count_circles(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=10, maxRadius=100)

    # Count the number of detected circles
    num_circles = 0

    if circles is not None:
        # Convert the (x, y, radius) output to integers
        circles = np.uint16(np.around(circles))
        for _ in circles[0, :]:
            num_circles += 1

    return num_circles
