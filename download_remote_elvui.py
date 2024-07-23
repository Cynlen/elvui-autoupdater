import requests
import os
import zipfile
import shutil

def download_elvui(download_url, version_number, installation_path):
    print(installation_path)
    # URL of the file to download (you need to replace this with the actual URL)
    file_url = download_url

    # Path to the Downloads directory
    downloads_dir = os.path.expanduser('~/Downloads')

    # Construct the full file path
    file_path = os.path.join(downloads_dir, f'elvui-{version_number}.zip')
    print(f'Elvui {version_number} has been downloaded to {file_path}')
    # Send a GET request to the URL
    response = requests.get(file_url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a local file in binary write mode
        with open(file_path, 'wb') as file:
            # Write the content of the response to the file
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print('Download completed successfully.')
        print('Unzipping ElvUI...')
        unzip_file(file_path, downloads_dir)
        print(f'ElvUI {version_number} has been extracted successfully!')
        print("Moving ElvUI Folder...")
        copy_files(downloads_dir + '/ElvUI/', f"{installation_path}/Interface/Addons/ElvUI")
        print("Moving ElvUI_Libraries Folder...")
        copy_files(downloads_dir + '/ElvUI_Libraries/', f"{installation_path}/Interface/Addons/ElvUI_Libraries")
        print("Moving ElvUI_Options Folder...")
        copy_files(downloads_dir + '/ElvUI_Options/', f"{installation_path}/Interface/Addons/ElvUI_Options")
    else:
        print('Failed to download file. Status code:', response.status_code)
    

def unzip_file(zip_path, extract_to):
    """
    Unzips a file from `zip_path` to the directory `extract_to`.
    
    :param zip_path: Path to the zip file.
    :param extract_to: Directory where the contents will be extracted.
    """
    # Ensure the extraction directory exists
    os.makedirs(extract_to, exist_ok=True)

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents into the specified directory
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")


def copy_files(source_dir, destination_dir):
    """
    Copies all files from `source_dir` to `destination_dir`.
    
    :param source_dir: Directory from which files will be copied.
    :param destination_dir: Directory to which files will be copied.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        
        # If it's a file, copy it
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
        # If it's a directory, recursively copy it
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)

# Example usage
# zip_path = file_path  # Replace with your zip file path
# extract_to = 'c:/support/'   # Replace with your desired extraction path

# unzip_file(file_path, extract_to)