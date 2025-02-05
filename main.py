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
edge_min = 150
edge_max = 200

# TODO: change this based on the size of the paper that is input
base_point = 0
input_width = 800
input_height = 800


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

    # Finding the edges of the image using Canny method
    edges_img = utils.edge_detect(blurred_img, edge_min, edge_max)

    # # Finding the corners of the paper, using the contours of the edges we just created
    contours, hierarchy = cv2.findContours(edges_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for c in contours:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c,0.02 * p, True)

        if len(approx)==4:
            target = approx
            break
    approx = utils.map_endpoints(target) # approximate corners of the sheet

    # Re-mapping points to specified size
    corner_points = np.float32(
        [[base_point,base_point],
        [input_width,base_point],
        [input_width,input_height],
        [base_point,input_height]]
        )

    remapped_img = cv2.getPerspectiveTransform(approx, corner_points)
    print(remapped_img)
    final_image = cv2.warpPerspective(resized_img, remapped_img, (input_width, input_height))

    # USED IN TESTING -- Displaying resized image that will be used with OpenCV
    utils.show_image(final_image)

    return


if __name__=="__main__": 
    main()