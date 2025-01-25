# Utilities that are useful for vision project, but don't need to be housed in the main file

import cv2

def scan_image():
    # TODO: Update the function to scan, rather than return the test image in the folder 
    return cv2.imread("test_img.jpg")


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

def show_image(image):
    # Show the image to the screen
    # NOTE: Mostly used for testing purposes
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return