"""
Author: Thomas Cascais Nisterenko
Date: 2021-10-09
Purpose: This python script iterates through image files in a folder,
         resizes them, rotates them, and finally, converts them to a
         different format. Uses os, and pillow modules.
"""

import os
import PIL  # pillow module for compatibility with python3

def get_imgs(dir_path):
    """
    Given a path to a directory, this file takes all the correct
    image files (found in README) and saves them to a list.
    :param dir_path: string with the directory path
    :return img_lst: list with image file names
    """

    img_lst = []  # initializes empty img_lst

    # loops through all files in given dir_path
    for filename in os.listdir(dir_path):
        # image files of TIFF format are appended to the list
        if filename.endswith(".tiff"):
            img_lst.append(filename)
    
    return img_lst

def man_img(image):
    """
    Given an image object, this file manipulates it according
    to the specifications (found in README). Resizes, rotates,
    and changes format.
    :param image: image object
    :return: None
    """

def main():
    """
    main function executes the logic in the script and calls other functions
    """

    images = get_imgs("~/images")
    for img in images:
        man_img(img)

if __name__ == "__main__":
    main()
