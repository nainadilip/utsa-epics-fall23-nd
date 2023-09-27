import os
import shutil

def organize_images(source_folder, target_folder_prefix, images_per_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    image_files.sort()  # Sort files to maintain order
    
    if len(image_files) == 0:
        print("No image files found in the source folder.")
        return
    
    total_images = len(image_files)
    total_folders = total_images // images_per_folder
    
    if total_images % images_per_folder != 0:
        total_folders += 1
    
    for folder_idx in range(total_folders):
        folder_name = f"{target_folder_prefix}_{folder_idx + 1}"
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        start_idx = folder_idx * images_per_folder
        end_idx = min((folder_idx + 1) * images_per_folder, total_images)
        
        for idx in range(start_idx, end_idx):
            image_name = image_files[idx]
            source_path = os.path.join(source_folder, image_name)
            target_path = os.path.join(folder_path, image_name)
            shutil.move(source_path, target_path)
            print(f"Moved '{image_name}' to '{folder_name}'")

if __name__ == "__main__":
    source_folder = "C:\\Users\\naina\\OneDrive\\utsa\\EGR"
    target_folder_prefix = "group"
    images_per_folder = 10
    organize_images(source_folder, target_folder_prefix, images_per_folder)
