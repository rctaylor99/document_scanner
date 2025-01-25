# Importing packages
import numpy as np
import cv2
import image_utilities as utils

# Defining constants
resize_width = 1200
resize_height = 800

# kernel size must be positive and odd for gaussian blur
blur_kernel_size = 5
blur_sigma = 0

# TODO: Edit these values to ensure best image quality
edge_min = 95
edge_max = 125


def main():
    # Printing welcome message
    print('===================================')
    print('----Welcome to Document Scanner----')
    print('===================================')

    # Read in new image and resize to work with OpenCV
    original_img = utils.scan_image()
    resized_img = utils.resize_image(original_img, resize_width, resize_height)

    # Convert resized image to greyscale
    greyscale_img = utils.convert_to_greyscale(resized_img)
    
    # Using Gaussian blur to eliminate the Gaussian noise from the image
    blurred_img = utils.blur(greyscale_img, blur_kernel_size, blur_sigma)

    edges_img = utils.edge_detect(blurred_img, edge_min, edge_max)

    # USED IN TESTING -- Displaying resized image that will be used with OpenCV
    utils.show_image(edges_img)

    return


if __name__=="__main__": 
    main()