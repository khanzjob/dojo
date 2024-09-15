import os

def list_files(startpath, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # Get the level of the current directory based on the number of slashes
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

if __name__ == "__main__":
    # Use the current working directory as the parent directory
    parent_directory = os.getcwd()
    output_file = "directory_structure.txt"
    list_files(parent_directory, output_file)
    print(f"Directory structure has been written to {output_file}.")
