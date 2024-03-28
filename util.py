# file_extractor.py

import os
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