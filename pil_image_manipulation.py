"""
Author: Thomas Cascais Nisterenko
Date: 2021-10-09
Purpose: This python script iterates through image files in a folder,
         resizes them, rotates them, and finally, converts them to a
         different format. Uses os, re, and pillow (PIL) modules.
"""

import os
from PIL import Image
import re


def get_imgs(dir_path):
    """
    Given a path to a directory, this file takes all the correct
    image files (found in README) and saves them to a list.
    :param dir_path: string with the directory path
    :return img_lst: list with image file names
    """

    # initializes empty img_lst
    img_lst = []
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
    :param image: image path
    :return: None
    """
    image_obj = Image(image)
    new_image = image_obj.rotate(270).resize((128, 128))
    new_image.save(update_filename(image))


def update_filename(old_name):
    """
    Updates image filename with the correct information
    so that it may be saved to the proper directory.
    :param old_name: string with old filename/path
    :param new_name: string with new filename/path
    """

    # pattern to capture only the unique file_name
    pattern = r"/images/(\w+).tiff$"

    file_name = re.match(pattern, old_name).group(1)

    # new_name is constructed with the correct info
    new_name = "~/opt/icons/" + file_name + ".jpg"

    return new_name

def main():
    """
    main function executes the logic in the script and calls other functions
    """

    images = get_imgs("~/images")
    for img in images:
        man_img(img)


if __name__ == "__main__":
    main()

