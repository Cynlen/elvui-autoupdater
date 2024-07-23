import requests

def find_remote_elvui_version():
    # API endpoint for ElvUI addon version
    api_url = 'https://api.tukui.org/v1/addon/elvui'

    # Send a GET request to the API
    response = requests.get(api_url)
    data = response.json()
    download_url = data.get('url')
    # Extract the version number
    version = data.get('version')
    last_update = data.get('last_update')

    # Print the results
    print(version)
    return [version, download_url]
#find_remote_elvui_version()