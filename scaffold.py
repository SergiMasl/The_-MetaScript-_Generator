#!/usr/bin/env python3

import os
import sys

def main():

    template = """#!/usr/bin/env python3
import sys

def main():
    sys.stdout.write("This is stdout message.\\n")
    sys.stderr.write(\"This is stderr message.")

if __name__ == \"__main__\":
    main()
"""

    #ask user for project name
    new_project_name = input("Enter the project name: ").strip()
    if not new_project_name:
        print("Project name cannot be empty.")

    #create project directory
    try:
        os.makedirs(new_project_name)

        #ask for file name
        file_name = input("Enter the main file name (with extension, e.g., main.py): ").strip()
        if not file_name:
            print("File name cannot be empty.")
            sys.exit(1) 
        else:
            file_path = os.path.join(new_project_name, file_name)
            with open(file_path, 'w') as f:
                f.write(template)
            print(f"Project '{new_project_name}' created with file '{file_name}'.") 

    #i used execpt to catch if directory or file already exists
    except FileExistsError:
        print(f"Directory '{new_project_name}' already exists.")
        sys.exit(1)     
    except Exception as e:
        print(f"Error creating directory '{new_project_name}': {e}")
        sys.exit(1)       

if __name__ == "__main__":
    main()