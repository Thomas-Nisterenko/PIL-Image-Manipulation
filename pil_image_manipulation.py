#!/usr/bin/env python3
"""
Author: Thomas Cascais Nisterenko
Date: 2021-10-09
Purpose: This python script iterates through image files in a folder,
         resizes them, rotates them, and finally, converts them to a
         different format. Uses os and pillow (PIL) modules.
"""

import os
from PIL import Image


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
        # codnitional dodges a hidden file
        if ".DS" not in filename:
            img_lst.append(filename)
    
    return img_lst


def man_img(image_name):
    """
    Given an image name, this file manipulates it according
    to the specifications (found in README). Resizes, rotates,
    and changes format.
    :param image: image path
    :return: None
    """
    # image_obj is opened in RGB mode
    image_obj = Image.open(image_name).convert("RGB")
    # manipulations to the image are made (rotated and resized)
    new_image = image_obj.rotate(270).resize((128, 128))
    return new_image


def update_all(images):
    """
    Iterates through a list of images and updates all of them.
    :param images: list with image file names
    :return updated: dictionary with updated image objects
    """

    # updated is initialized as an empty dictionary
    updated = {}

    # every image is manipulated and then saved into the dictionary
    # with its name as the key
    for image in images:
        updated[image] = man_img(image)
    
    return updated

def save_all(updated_images, dir_path):
    """
    Saves all images in new format.
    :param updated_images: dictionary containing image objects
    :param dir_path: path to the directory where images are to be saved
    """

    # changes directory to make saving images easier
    os.chdir(dir_path)

    # each image object is saved with its correct name as a JPEG file
    for name, img_obj in updated_images.items():
        img_obj.save(name, "JPEG")

def main():
    """
    main function executes the logic in the script and calls other functions
    """

    # gets the path to the images directory from home
    images_dir = os.getcwd() + "/images"

    # enters the images directory to make file manipulation more streamlined
    os.chdir(images_dir)

    # core functionality of the script: gets the old images, produces the new ones,
    # and finally saves them all in the specified directory
    old_images = get_imgs(images_dir)
    new_images = update_all(old_images)
    save_all(new_images, "/opt/icons")


if __name__ == "__main__":
    main()
