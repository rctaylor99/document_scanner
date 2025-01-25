# Importing packages
# from pyimagesearch.transform import four_point_transform
# from skimage.filters import threshold_local
import numpy as np
# import argparse
import cv2
# import imutils 
import image_utilities as utils

# Defining constants
resize_width = 1200
resize_height = 800


def main():
    # Printing welcome message
    print('===================================')
    print('----Welcome to Document Scanner----')
    print('===================================')

    # Read in new image and resize to work with OpenCV
    original_img = utils.scan_image()
    resized_img = utils.resize_image(original_img)

    # Convert resized image to greyscale
    greyscale_img = utils.convert_to_greyscale(resized_img)
    


    # USED IN TESTING -- Displaying resized image that will be used with OpenCV
    utils.show_image(greyscale_img)

    return


if __name__=="__main__": 
    main()