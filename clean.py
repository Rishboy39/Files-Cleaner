import os
import shutil

def organize_files(directory):
    extension_folders = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".docx": "Documents",
        ".ppt": "Powerpoints",
        ".xlsx": "Excel Files",
    }

    for folder_name in extension_folders.values():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            if extension.lower() in extension_folders:
                destination_folder = os.path.join(directory, extension_folders[extension.lower()])
                shutil.move(file_path, os.path.join(destination_folder, filename))
            else:
                other_folder = os.path.join(directory, "Other")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))

if __name__ == "__main__":
    directory_to_organize = input("Enter the directory path to organize: ")
    organize_files(directory_to_organize)
    print("Files organized successfully!")
