import os
import shutil
import re

def remove_prefixes_from_images_in_current_folder():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    for file_name in files:
        if file_name.startswith("IMG_") or file_name.startswith("VID_"):
            # Get the new file name by removing the prefix
            new_file_name = file_name[4:]
            os.rename(file_name, new_file_name)

def group_files_by_date_in_its_name():
    current_dir = os.getcwd()
    for file_name in os.listdir(current_dir):
        if re.match(r"^\d{8}_", file_name):
            source_path = os.path.join(current_dir, file_name)
            destination_path = os.path.join(current_dir, file_name[:8])
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)
            shutil.move(source_path, destination_path)
            print(f"Moved file: {file_name}")

if __name__ == "__main__":
    remove_prefixes_from_images_in_current_folder()
    group_files_by_date_in_its_name()