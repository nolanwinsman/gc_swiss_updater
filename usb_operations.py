# usb_operations.py

import os
import shutil
import psutil

class USBManager:
    """
    USBManager class provides methods for handling USB-related operations such as detecting
    and managing USB drives.
    """

    @staticmethod
    def get_single_fat32_usb_drive():
        """
        Detects a single FAT32-formatted USB drive connected to the system.
        Returns the partition object representing the USB drive if found, otherwise returns None.
        """
        fat32_usb_drives = []

        partitions = psutil.disk_partitions()

        for partition in partitions:
            try:
                if 'removable' in partition.opts:
                    if partition.fstype.lower() == 'fat32':
                        fat32_usb_drives.append(partition)

            except PermissionError as e:
                print(f"Permission error while accessing {partition.mountpoint}: {e}")

        if len(fat32_usb_drives) == 1:
            return fat32_usb_drives[0]
        else:
            return None

    @staticmethod
    def is_drive_writable(drive_path):
        """
        Checks if a drive is writable by attempting to create and delete a test file.
        Returns True if writable, otherwise returns False.
        """
        try:
            test_file_path = os.path.join(drive_path, 'test.txt')
            with open(test_file_path, 'w') as test_file:
                test_file.write('Test')
            os.remove(test_file_path)
            return True
        except Exception as e:
            print(f"Error writing to {drive_path}: {e}")
            return False

    @staticmethod
    def check_available_space(drive_path, required_space):
        """
        Checks if there is sufficient space available on a drive for the required space.
        Returns True if enough space available, otherwise returns False.
        """
        try:
            disk_usage = psutil.disk_usage(drive_path)
            available_space = disk_usage.free
            if available_space >= required_space:
                return True
            else:
                print(f"Not enough space available on {drive_path}")
                return False
        except Exception as e:
            print(f"Error checking available space on {drive_path}: {e}")
            return False

    @staticmethod
    def check_drive_empty(drive_path):
        """
        Checks if a drive is empty.
        Returns True if empty, otherwise returns False.
        """
        try:
            if os.listdir(drive_path):
                print(f"{drive_path} is not empty")
                return False
            else:
                return True
        except Exception as e:
            print(f"Error checking if {drive_path} is empty: {e}")
            return False

    @staticmethod
    def get_drive_name(drive_device):
        """
        Retrieves the name of the USB drive based on its device path.
        """
        # Implement logic to get drive name based on device path (e.g., using platform-specific APIs)
        # For demonstration purposes, returning a default name
        return "GC"
