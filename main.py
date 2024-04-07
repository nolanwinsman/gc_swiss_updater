# main.py

import os
import shutil
import psutil  # Add import statement for psutil
from usb_operations import USBManager
from github_release_downloader import GitHubReleaseDownloader
from util import Util

# Example usage
repo_owner = "emukidid"
repo_name = "swiss-gc"
target_dir = "swiss-releases"
file_extension = ".7z"  # Specify the desired file extension


swiss_release_file = GitHubReleaseDownloader.download_latest_release(repo_owner, repo_name, target_dir, file_extension)
if swiss_release_file:
    extracted_swiss_folder = Util.extract_7z(swiss_release_file, target_dir)
    print(f"Deleting {swiss_release_file}")
    os.remove(swiss_release_file)
    # Implement file copying using shutil.copytree() here



usb_drive_info = USBManager.get_single_fat32_usb_drive()
if usb_drive_info:
    print("External FAT32 USB Drive Found:")
    print("Drive:", usb_drive_info.device)
    print("Mount point:", usb_drive_info.mountpoint)
    print("File system type:", usb_drive_info.fstype)
    print("Drive name:", USBManager.get_drive_name(usb_drive_info.device))
    print("Usage:", psutil.disk_usage(usb_drive_info.mountpoint))  # Print disk usage information

    # Handles renaming and moving the .DOL file to the root of the Gamecube Swiss Drive
    dol_file = os.path.join(f"{target_dir}/{extracted_swiss_folder}", "DOL", f'{extracted_swiss_folder}.dol')
    ipl_file = os.path.join(usb_drive_info.mountpoint, 'IPL.dol')

    print(f"Renaming {dol_file} to IPL.dol")
    print(f"Moving IPL.dol to {usb_drive_info.mountpoint}")
    
    shutil.move(dol_file, ipl_file, copy_function=shutil.copy2)

    # Moves the rest of the release folder to the Gamecube Swiss Drive
    swiss_release_folder =  os.path.join(f"{target_dir}/{extracted_swiss_folder}")
    print(f"Moving {swiss_release_folder} to {usb_drive_info.mountpoint}")
    Util.copy_files(swiss_release_folder, usb_drive_info.mountpoint)

    print(f"Swiss Version upgraded to {extracted_swiss_folder}")

else:
    print("No single external FAT32 USB drive found.")
