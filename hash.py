#!/usr/bin/python
# coding=utf-8


##############################################################################
__author__ = "JArter"
__date__ = "2023-04-13"
__copyright__ = "Copyright April 2023"
__credits__ = ["Jason A. Arter"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jason A. Arter"
__email__ = "jason.arter@gmail.com"
__status__ = "Prototype"
__updated__ = "2023-04-14"
__python_version__ = "3.11"
##############################################################################


import os
import datetime
import re
from PIL import Image
from pathlib import Path, PureWindowsPath
from win32api import MoveFile
from secrets import choice


file_pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}\.\d{2}\.\d{2}\.\d{3}.\w*", re.IGNORECASE)
dtg_tags = [0x0132, 0x9003, 0x9004, 0xC71B]
photo_extensions = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif',
                    '.webp', '.tiff', '.tif', '.psd', '.raw', '.arw', '.cr2', '.k25',
                    '.bmp', '.dib', '.heif', '.heic', 'ind', 'indd', 'indt', '.svg',
                    '.svgz', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.ai',
                    '.eps', '.png']


def rename_all(source_dir: str, dry_run=True) -> None:
    """
    :param source_dir:
    :param dry_run:
    """
    source_path = Path(source_dir)
    if not source_path.exists():
        raise FileNotFoundError
    if not source_path.is_dir():
        raise NotADirectoryError
    filenames = [x for x in source_path.glob('**/*.*') if x.suffix.lower() in photo_extensions]
    for source_file_path in filenames:
        times = []
        my_filename = PureWindowsPath(source_file_path).name
        if file_pattern.match(my_filename):
            print("File has correct naming format:", source_file_path)
            continue
        try:
            with Image.open(source_file_path) as img:
                stat_info = os.stat(source_file_path)
                modified_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
                times.append(modified_time)
                exif_tags = img.getexif()
                for item, value in exif_tags.items():
                    if item in dtg_tags:
                        try:
                            formatted_time = datetime.datetime.strptime(str(value), "%Y:%m:%d %H:%M:%S")
                        except ValueError:
                            print(f"Bad time value for file {source_file_path}.")
                            continue
                        times.append(formatted_time)
                chosen_time = min(times)
                file_time = chosen_time.strftime("%Y-%m-%dT%H.%M.%S")
                file_time_milliseconds = file_time + "." + ("{:0>3d}".format(choice(range(1, 1000))))
                new_file_name = file_time_milliseconds + source_file_path.suffix
                new_file_path = source_file_path.parent.joinpath(Path(new_file_name))
                if new_file_name is not None:
                    if not new_file_path.exists():
                        if not dry_run:
                            img.close()
                            MoveFile(str(source_file_path), str(new_file_path))
                            print(f"Renamed {source_file_path} to {new_file_path}")
                        else:
                            print(f"old: {source_file_path}\t\t\tnew: {new_file_path}")
                    else:
                        print(f"{new_file_path} already exists.")
        except:
            print("I've hit the exception on filename:", source_file_path)
        # except PIL.UnidentifiedImageError:
        #     print("PIL couldn't identify image:", source_file_path)
        #     continue


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-s", "--source", required=True, help="Directory to copy photos from.", type=str)
    # parser.add_argument("-d", "--destination", required=True, help="Directory to copy photos to.", type=str)
    # my_args = parser.parse_args()

    rename_all(source_dir=r"D:\Files\Photos", dry_run=False)
