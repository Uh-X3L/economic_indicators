#!/usr/bin/env python3
"""
create_structure.py

This script creates the folder structure for the crypto project:
my_crypto_project/
├── src/
│   ├── __init__.py
│   ├── key_vault.py
│   ├── crypto_manager.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_key_vault.py
│   └── test_crypto_manager.py
├── requirements.txt
├── setup.py
└── README.md
"""

import os

def create_project_structure(project_name=""):
    # Get the directory where this script resides (e.g., "start")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # The root folder is the parent directory of the script's directory
    root_dir = os.path.abspath(os.path.join(script_dir, ".."))

    # Define the folder structure with their respective files
    structure = {
        "src": ["__init__.py", "key_vault.py", "crypto_manager.py", "config.py", "main.py"],
        "tests": ["__init__.py", "test_key_vault.py", "test_crypto_manager.py"],
        "": ["requirements.txt", "setup.py", "README.md"]
    }


    # Loop through the defined structure to create directories and files
    for folder, files in structure.items():
        folder_path = os.path.join(root_dir, folder) if folder else root_dir

        # Create the subdirectory if it's not the base folder
        if folder:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created directory: {folder_path}")

        # Create the files in the specified folder
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    # Optionally, add a header comment into each file
                    f.write(f"# {filename} for {project_name} project\n")
                print(f"Created file: {file_path}")
            else:
                print(f"File already exists: {file_path}")

if __name__ == "__main__":
    create_project_structure()