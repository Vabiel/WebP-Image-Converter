import os
import argparse
from PIL import Image

def convert_image(input_path):
    """Converts a single image to WebP."""
    try:
        output_path = os.path.splitext(input_path)[0] + '.webp'
        with Image.open(input_path) as img:
            img.save(output_path, 'webp')
        print(f'Successfully converted: {input_path} -> {output_path}')
        return True
    except Exception as e:
        print(f'Error during conversion {input_path}: {e}')
        return False

def convert_folder(folder_path):
    """Converts all supported images in a folder."""
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    converted = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(folder_path, filename)
            if convert_image(input_path):
                converted += 1
    return converted

def prompt_for_path():
    """Prompts the user for a file or folder path."""
    print("Enter a file or folder path to convert (or press Enter to exit):")
    path = input().strip()
    if not path:
        return None
    if not os.path.exists(path):
        print(f'Error: {path} does not exist')
        return None
    return path

def main():
    parser = argparse.ArgumentParser(description='Image to WebP Converter')
    parser.add_argument('paths', nargs='*', help='Paths to files or folders to convert')
    parser.add_argument('--folder', '-f', help='Path to the folder to convert all images in it')
    args = parser.parse_args()

    # Initialize paths to process
    paths_to_process = args.paths
    folder_to_process = args.folder

    # If no arguments provided, prompt for a path
    if not paths_to_process and not folder_to_process:
        path = prompt_for_path()
        if not path:
            print('No path provided. Exiting.')
            return
        if os.path.isdir(path):
            folder_to_process = path
        else:
            paths_to_process = [path]

    # Process paths
    converted_files = 0
    converted_folders = 0

    # Handle paths passed as arguments (including Drag and Drop)
    if paths_to_process:
        for path in paths_to_process:
            if not os.path.exists(path):
                print(f'Skip: {path} (does not exist)')
                continue
            if os.path.isdir(path):
                count = convert_folder(path)
                if count > 0:
                    converted_folders += 1
                    print(f'Converted {count} images in folder {path}')
                else:
                    print(f'No supported images found in folder {path}')
            elif os.path.isfile(path) and path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                if convert_image(path):
                    converted_files += 1
            else:
                print(f'Skip: {path} (not supported format)')

    # Handle folder specified via --folder
    if folder_to_process:
        if not os.path.isdir(folder_to_process):
            print(f'Error: {folder_to_process} is not a folder or does not exist')
        else:
            count = convert_folder(folder_to_process)
            if count > 0:
                converted_folders += 1
                print(f'Converted {count} images in folder {folder_to_process}')
            else:
                print(f'No supported images found in folder {folder_to_process}')

    # Final message
    if converted_files > 0 or converted_folders > 0:
        print(f'\nTotal: {converted_files} files and {converted_folders} folders converted')
    else:
        print('\nNothing converted')

if __name__ == '__main__':
    main()