import os

def rename_images(folder_path, new_extension):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if len(image_files) == 0:
        print("No files found in the folder.")
        return
    
    new_name_template = "clouds_{}.{}".format
    
    for idx, old_name in enumerate(image_files):
        new_name = new_name_template(idx, new_extension)
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{old_name}' to '{new_name}'")

if __name__ == "__main__":
    folder_path = "C:\\Users\\naina\\OneDrive\\utsa\\EGR"
    new_extension = "jpg"  # Replace with your desired extension
    rename_images(folder_path, new_extension)
