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
        Copies files from source to destination, creating destination directory if needed.
        """
        os.makedirs(dst, exist_ok=True)  # Create destination directory if it doesn't exist
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            if os.path.isdir(src_path):
                # Recursively copy subdirectories
                Util.copy_files(src_path, dst_path)  # Use Util.copy_files() recursively
            else:
                # Copy files, overwrite existing files
                shutil.copy2(src_path, dst_path)
