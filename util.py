# file_extractor.py

import os
import shutil
from py7zr import SevenZipFile

class Util:
    """
    FileExtractor class provides methods for extracting files from 7z archives.
    """

    @staticmethod
    def extract_7z(file_path, target_dir):
        """
        Extracts files from a 7z archive to the specified target directory.
        Returns the name of the extracted file.
        """
        os.makedirs(target_dir, exist_ok=True)
        with SevenZipFile(file_path, 'r') as archive:
            file_list = archive.getnames()
            archive.extractall(target_dir)
            # Assuming only one file is extracted, return its name
            return file_list[0] if file_list else None

    @staticmethod
    def copy_files(src, dst):
        """
        Copies files from source to destination, replacing existing files in the destination.
        """
        # Create the destination directory if it doesn't exist
        os.makedirs(dst, exist_ok=True)

        # Iterate over files in the source directory
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)

            # Copy the file from source to destination, replacing if already exists
            try:
                shutil.copy(src_path, dst_path)
                print(f"Copied '{src_path}' to '{dst_path}'")
            except shutil.SameFileError:
                # If the source and destination files are the same, skip
                continue
            except IsADirectoryError:
                # If the item is a directory, recursively copy it
                Util.copy_files(src_path, dst_path)