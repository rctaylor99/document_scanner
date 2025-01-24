# Importing packages
# from pyimagesearch.transform import four_point_transform
# from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils 

# Defining constants
resize_width = 1200
resize_height = 800

def scan_image():
    # TODO: Update the function to scan, rather than return the test image in the folder 
    return cv2.imread("test_img.jpg")


def resize_image(image):
    # TODO: Update the image_width and image_height variables to more reasonable values
    return cv2.resize(image, (resize_width,resize_height))


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

def main():
    # Printing welcome message
    print('===================================')
    print('----Welcome to Document Scanner----')
    print('===================================')

    # Read in new image and resize to work with OpenCV
    original_img = scan_image()
    resized_img = resize_image(original_img)

    # Convert resized image to greyscale
    greyscale_img = convert_to_greyscale(resized_img)
    


    # USED IN TESTING -- Displaying resized image that will be used with OpenCV
    show_image(greyscale_img)

    return


if __name__=="__main__": 
    main()