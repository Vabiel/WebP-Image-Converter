# WebP Image Converter

This repository contains two Python scripts for converting images to WebP format:

1. **Console-based WebP Converter** (`webp_converter_console.py`): A command-line tool for converting images or folders of images to WebP.
2. **PyQt5-based WebP Converter** (`webp_converter_pyqt5.py`): A GUI application with Drag and Drop support and folder selection for converting images to WebP.

Additionally, two scripts are provided to automate setup and execution:

- `setup_and_run.sh`: For Unix-like systems (Linux/macOS).
- `setup_and_run.bat`: For Windows.

## Requirements

- Python 3.6 or higher (download from python.org)
- Pillow: Installed via `pip` in the virtual environment
- PyQt5: Installed via `pip` in the virtual environment

All dependencies are managed within the virtual environment using `pip`, requiring no system-level installations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/webp-converter.git
   cd webp-converter
   ```

2. Install Python 3 from python.org if not already installed.

3. Use the provided setup scripts to create a virtual environment and install dependencies (see below).

## Usage

### Using the Setup Scripts

Two scripts are provided to automate the setup of a Python virtual environment, install dependencies (`Pillow` and `PyQt5`), and run the converters. All dependencies are installed via `pip` within the virtual environment.

#### For Unix-like Systems (Linux/macOS): `setup_and_run.sh`

1. Make the script executable:

   ```bash
   chmod +x setup_and_run.sh
   ```

2. Run the script:

   ```bash
   ./setup_and_run.sh
   ```

3. Follow the prompt to select:

   - `1` for the console-based converter.
   - `2` for the PyQt5-based GUI converter.
   - Press Enter to exit.

4. For the console-based converter, you can:

   - Pass arguments directly:

     ```bash
     ./setup_and_run.sh image.jpg
     ```

     or

     ```bash
     ./setup_and_run.sh --folder path/to/folder
     ```

   - If no arguments are provided, the script will prompt for a file or folder path interactively.

#### For Windows: `setup_and_run.bat`

1. Run the script by double-clicking `setup_and_run.bat` or from the Command Prompt:

   ```cmd
   setup_and_run.bat
   ```

2. Follow the prompt to select:

   - `1` for the console-based converter.
   - `2` for the PyQt5-based GUI converter.
   - Press Enter to exit.

3. For the console-based converter, you can:

   - Pass arguments directly:

     ```cmd
     setup_and_run.bat image.jpg
     ```

     or

     ```cmd
     setup_and_run.bat --folder path/to/folder
     ```

   - If no arguments are provided, the script will prompt for a file or folder path interactively.

#### Notes for Setup Scripts

- Both scripts create a virtual environment in the `venv` directory.
- They install `Pillow` and `PyQt5` automatically via `pip`.
- The virtual environment is deactivated after the script finishes.

### 1. Console-based WebP Converter (`webp_converter_console.py`)

This script allows you to convert images or entire folders to WebP using command-line arguments, Drag and Drop, or interactive prompts.

#### Commands

- Convert individual files:

  ```bash
  python webp_converter_console.py image1.jpg image2.png
  ```

- Convert all supported images in a folder:

  ```bash
  python webp_converter_console.py --folder path/to/folder
  ```

  or

  ```bash
  python webp_converter_console.py path/to/folder
  ```

- Interactive mode (no arguments):

  ```bash
  python webp_converter_console.py
  ```

  The script will prompt for a file or folder path.

#### Drag and Drop

- Drag and drop one or more image files or a folder onto the `webp_converter_console.py` script file. The script will process all supported images.

#### Example Output

```bash
$ python webp_converter_console.py image.jpg
Successfully converted: image.jpg -> image.webp

Total: 1 files and 0 folders converted

$ python webp_converter_console.py --folder images
Successfully converted: images/photo1.png -> images/photo1.webp
Successfully converted: images/photo2.jpg -> images/photo2.webp
Converted 2 images in folder images

Total: 0 files and 1 folders converted

$ python webp_converter_console.py
Enter a file or folder path to convert (or press Enter to exit):
images
Successfully converted: images/photo1.png -> images/photo1.webp
Successfully converted: images/photo2.jpg -> images/photo2.webp
Converted 2 images in folder images

Total: 0 files and 1 folders converted
```

#### Notes

- The script skips unsupported file formats and reports errors for invalid paths or conversion issues.
- Converted images are saved in the same directory with the `.webp` extension.
- Interactive mode is triggered when no command-line arguments are provided, making it easier to use via `setup_and_run.sh`.

### 2. PyQt5-based WebP Converter (`webp_converter_pyqt5.py`)

This script provides a graphical user interface (GUI) for converting images to WebP. It supports Drag and Drop and folder selection.

#### Running the Script

```bash
python webp_converter_pyqt5.py
```

#### Features

- **Drag and Drop**: Drag and drop image files or folders onto the application window to convert them.
- **Folder Selection**: Click the "Select Folder" button to choose a folder, and all supported images inside will be converted.
- **Status Updates**: The GUI displays the status of conversions (e.g., number of images converted or error messages).

#### Requirements

- PyQt5 and Pillow, both installed via `pip` in the virtual environment.

#### Example Usage

1. Run the script:

   ```bash
   python webp_converter_pyqt5.py
   ```

2. A window will appear.

3. Drag and drop images (e.g., `photo.jpg`) or a folder onto the window, or click "Select Folder" to choose a folder.

4. The status label will update with the results, e.g., "Converted: photo.jpg" or "Converted 5 images".

#### Notes

- Converted images are saved in the same directory with the `.webp` extension.

## Supported Formats

- Input: PNG, JPG, JPEG, BMP, GIF
- Output: WebP

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Contact

For questions or suggestions, please open an issue on this repository.