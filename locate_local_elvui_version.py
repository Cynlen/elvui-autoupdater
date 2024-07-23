import os




def get_elvui_version(addons_path):
    elvui_path = os.path.join(addons_path, 'ElvUI')
    
    # Check if the ElvUI directory exists
    if os.path.isdir(elvui_path):
        toc_file = None
        for file in os.listdir(elvui_path):
            if file.endswith('.toc'):
                toc_file = file
                break
        
        if toc_file:
            toc_file_path = os.path.join(elvui_path, toc_file)
            
            # Read the .toc file to get the version
            with open(toc_file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.startswith('## Version:'):
                        version = line.split(':', 1)[1].strip()
                        return version
    
    return "ElvUI not found"

def invoke_elvui_checker(installation_path):
    install_path = installation_path
    # Path to the World of Warcraft AddOns directory
    wow_addons_path = os.path.expanduser(f'{install_path}/Interface/AddOns')

    # Get ElvUI version
    elvui_version = get_elvui_version(wow_addons_path).replace("v", "")

    # Print ElvUI version
    print(f"ElvUI Version: {elvui_version}")
    return elvui_version

#invoke_elvui_checker('D:\Program Files (x86)\World of Warcraft\_retail_')
