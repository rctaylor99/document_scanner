# Utilities that are useful for vision project, but don't need to be housed in the main file

import cv2
import numpy as np
import time

def scan_image():
    # DONE: Update the function to scan, rather than return the test image in the folder 
    capture = cv2.VideoCapture(3)

    if not capture.isOpened():
        print("Error: Could not open Webcam")
        exit()

    time.sleep(2)

    # Capture a single frame from the video
    ret, frame = capture.read()

    # If the frame is captured correctly, save it!
    if ret: 
        cv2.imwrite("scanned_image.jpg", frame)
        print("Image saved as jpg")
    else:
        print("Failed to capture image")

    capture.release()

    return cv2.imread("scanned_image.jpg")


def resize_image(image, width, height):
    # TODO: Update the image_width and image_height variables to more reasonable values
    return cv2.resize(image, (width,height))


def convert_to_greyscale(image):
    # Using CV2 to convert the input image to greyscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def blur(image, kernel_size, sigma):
    # Gaussian blur within the CV2 Library
    return cv2.GaussianBlur(image,(kernel_size, kernel_size), sigma)


def edge_detect(image, min, max):
    # Using Canny method of determining edges on an image
    return cv2.Canny(image, min, max)


def map_endpoints(image):
    image = image.reshape((4,2))
    new_image = np.zeros((4,2), dtype = np.float32)

    add = image.sum(1)
    new_image[0] = image[np.argmin(add)]
    new_image[2] = image[np.argmax(add)]

    difference = np.diff(image, axis = 1)
    new_image[1] = image[np.argmin(difference)]
    new_image[3] = image[np.argmax(difference)]

    return new_image

def show_image(image0):
    # Show the image to the screen
    # NOTE: Mostly used for testing purposes
    cv2.imshow("Image", image0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return