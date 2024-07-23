import os
import psutil

def list_drives():
    partitions = psutil.disk_partitions()
    drives = [partition.device for partition in partitions if partition.fstype != '']
    return drives

def find_wow_installation():
    # List all available drives
    drives = list_drives()

    # Define the starting directories based on the available drives
    starting_directories = []
    for drive in drives:
        starting_directories.append(os.path.join(drive, 'Program Files'))
        starting_directories.append(os.path.join(drive, 'Program Files (x86)'))
        wow_files = ['Wow.exe', 'World of Warcraft.app']


    for starting_directory in starting_directories:
        for root, dirs, files in os.walk(starting_directory):
            for file in wow_files:
                if file in files:
                    return root
                    





# wow_paths = find_wow_installation(starting_directories)
# print(wow_paths)
# if wow_paths:
#     print("World of Warcraft installation(s) found at:")
#     for path in wow_paths:
#         print(path)
# else:
#     print("No World of Warcraft installation found.")