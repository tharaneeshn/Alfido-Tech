import os
import shutil
import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        filename='file_automation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def rename_files(directory, prefix):
    try:
        for count, filename in enumerate(os.listdir(directory)):
            old_path = os.path.join(directory, filename)
            if os.path.isfile(old_path):
                ext = os.path.splitext(filename)[1]
                new_name = f"{prefix}_{count+1}{ext}"
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                logging.info(f"Renamed: {filename} -> {new_name}")
        print("Files renamed successfully!")
    except Exception as e:
        logging.error(f"Error renaming files: {e}")
        print(f"Error: {e}")

def sort_files_by_extension(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1][1:]
                if not ext:
                    ext = 'no_extension'
                folder = os.path.join(directory, ext)
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, filename))
                logging.info(f"Moved {filename} to {folder}")
        print("Files sorted by extension successfully!")
    except Exception as e:
        logging.error(f"Error sorting files: {e}")
        print(f"Error: {e}")

def clean_empty_dirs(directory):
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            for d in dirs:
                path = os.path.join(root, d)
                if not os.listdir(path):
                    os.rmdir(path)
                    logging.info(f"Removed empty directory: {path}")
        print("Empty directories cleaned successfully!")
    except Exception as e:
        logging.error(f"Error cleaning directories: {e}")
        print(f"Error: {e}")

def main():
    setup_logger()
    print("\nFile Automation Script")
    print("1. Rename Files")
    print("2. Sort Files by Extension")
    print("3. Clean Empty Directories")

    choice = input("Enter your choice (1-3): ")
    directory = input("Enter directory path: ").strip()

    if not os.path.exists(directory):
        print("Invalid directory path!")
        return

    if choice == '1':
        prefix = input("Enter prefix for renaming files: ")
        rename_files(directory, prefix)
    elif choice == '2':
        sort_files_by_extension(directory)
    elif choice == '3':
        clean_empty