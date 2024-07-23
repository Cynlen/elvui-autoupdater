from locate_wow_installation import *
from locate_local_elvui_version import *
from locate_remote_elvui_version import *
from download_remote_elvui import *

''' Steps Required:
A: Find the current path of world of warcraft (scan multiple drives if needed)
B: Find the currently installed version of elvui
C: Go out to the internet and find the currently available version of elvui
D: If outdated, patch it, if not then quit
E: Run daily at like 3AM'''

# A:
print("Searching for the install location of WoW...")
installation_path = find_wow_installation()
print(f"Retail WoW is installed at the following location: {installation_path}")

# B:
print("Determining what the most recent version of ElvUI is along with the download URL...")
remote_elvui_version_results = find_remote_elvui_version()
remote_elvui_version = remote_elvui_version_results[0]
download_url = remote_elvui_version_results[1]
# print(remote_elvui_version)
# print(download_url)

# # C:
print("Searching for the currently installed version of ElvUI...")
local_elvui_version = invoke_elvui_checker(installation_path)
#Removing unnecessary portions from the response
print(local_elvui_version)

# # D:
# #if outdated, download updated elvui
if local_elvui_version < remote_elvui_version:
    download_elvui(download_url, remote_elvui_version, installation_path)
else:
    print("***ElvUI Appears to be up to date, no action taken.***")
