#!/usr/bin/python
# coding=utf-8


##############################################################################
__author__ = "Jason A. Arter"
__date__ = "2021-04-01"
__copyright__ = ""
__credits__ = ["Jason A. Arter"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jason A. Arter"
__email__ = "jason.arter@gmail.com"
__status__ = "Prototype"
__updated__ = "2021-04-01"
__python_version__ = "3.11"
##############################################################################


import imagehash
import argparse
import os
import numpy as np
from pathlib import Path
from PIL import Image


def find_duplicates(self):
    source_path = Path(self.dirname)
    if not source_path.exists():
        raise FileNotFoundError
    if not source_path.is_dir():
        raise NotADirectoryError
    filenames = [x for x in source_path.glob('**/*.*') if x.suffix in ['.jpg', '.JPG', '.jpeg']]
    hashes = {}
    duplicates = []
    print("Finding duplicates now...\n")
    for image_file in filenames:
        with Image.open(image_file) as img:
            temp_hash = imagehash.average_hash(img, self.hash_size)
            if temp_hash in hashes:
                print(f"Duplicate {image_file} \nfound for Image {hashes[temp_hash]}!\n")
                duplicates.append(image_file)
            else:
                hashes[temp_hash] = image_file
    if len(duplicates) != 0:
        # a = input(f"Do you want to delete these {len(duplicates)} Images? Press Y or N:  ")
        # space_saved = 0
        # if a.strip().lower() == "y":
        #     for duplicate in duplicates:
        #         space_saved += os.path.getsize(os.path.join(self.dirname, duplicate))
        #         os.remove(os.path.join(self.dirname, duplicate))
        #         print(f"{duplicate} Deleted Successfully!")
        #     print("\n\nYou saved {} mb of Space!".format(round(space_saved / 1000000), 2))
        # else:
        number_of_dupes = len(duplicates)
        print(f"Number of duplicates: {number_of_dupes}")
        print("Thank you for Using Duplicate Remover")
    else:
        print("No Duplicates Found :(")


def test_hash(location: str, hash_size: int = 8, similarity: int = 80) -> None:
    with Image.open(location) as img:
        hash1 = imagehash.average_hash(img, hash_size).hash
        print(hash1)


def find_similar(self, location: str, similarity: int = 80) -> None:
    filenames = os.listdir(self.dirname)
    threshold = 1 - similarity / 100
    diff_limit = int(threshold * (self.hash_size ** 2))
    with Image.open(location) as img:
        hash1 = imagehash.average_hash(img, self.hash_size).hash
    print(f"Finding Similar Images to {location} Now!\n")
    for image in filenames:
        with Image.open(os.path.join(self.dirname, image)) as img:
            hash2 = imagehash.average_hash(img, self.hash_size).hash
            if np.count_nonzero(hash1 != hash2) <= diff_limit:
                print(f"{image} image found {similarity}% similar to {location}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", required=True, help="Source path containing photos to compare.", type=str)
    parser.add_argument("-a", "--autodelete", required=False, help="Auto-delete duplicates?", type=bool)
    my_args = parser.parse_args()

    dr = DuplicateRemover(dirname=r"F:/Files/Photos/Ariel Arter")
    dr.find_duplicates()
