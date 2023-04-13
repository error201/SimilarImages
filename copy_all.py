#!/usr/bin/python
# coding=utf-8


##############################################################################
__author__ = "Jason A. Arter"
__date__ = "2021-04-21"
__copyright__ = ""
__credits__ = ["Jason A. Arter"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jason A. Arter"
__email__ = "jason.arter@gmail.com"
__status__ = "Prototype"
__updated__ = "2021-04-21"
__python_version__ = "3.9"
##############################################################################


from shutil import copy2
from pathlib import Path


photo_extensions = ['.jpg', '.JPG', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.PNG',
                    '.gif', '.webp', '.tiff', '.tif', '.TIF', '.psd', '.raw', '.arw', '.cr2', '.k25',
                    '.bmp', '.BMP', '.dib', '.heif', '.heic', 'ind', 'indd', 'indt', '.svg', '.svgz',
                    '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.ai', '.eps']


def copy_all(source_dir: str, dest_dir: str) -> None:
    """

    :param source_dir:
    :param dest_dir:
    """
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    if not source_path.exists():
        raise FileNotFoundError
    if not source_path.is_dir():
        raise NotADirectoryError
    if not dest_path.exists():
        Path.mkdir(dest_path)
        print("Creating destination directory...")
    filenames = [x for x in source_path.glob('**/*.*') if x.suffix in photo_extensions]
    print("Copying files now...\n")
    existing_files = []
    for source_file_path in filenames:
        source_file_name = source_file_path.name
        dest_file_path = dest_path.joinpath(source_file_name)
        if Path.exists(dest_file_path):
            existing_files.append(dest_file_path)
        else:
            copy2(source_file_path, dest_file_path)
    if len(existing_files) != 0:
        print("Existing files that weren't moved:")
        for name in existing_files:
            print("\t" + str(name))


if __name__ == '__main__':
    copy_all(source_dir=r"f:/Files/Photos/Alessia Ramirez Eng", dest_dir=r"f:/Files/Photo_Copies/")
