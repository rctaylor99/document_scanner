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


def show_image(image):
    # Show the image to the screen
    # NOTE: Mostly used for testing purposes
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return