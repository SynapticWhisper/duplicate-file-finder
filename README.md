# Duplicate File Finder

## Description

Duplicate File Finder is a powerful and user-friendly application designed to help you quickly identify and remove duplicate files from your system. Using various search methods such as file name comparison, MD5 hash, and SHA256 hash, this tool ensures a thorough and accurate scanning process. The intuitive interface allows for easy navigation and management of duplicates, enhancing your productivity and freeing up valuable storage space.

This project was carried out as a final qualifying work on professional retraining courses.

## Features

- **Multiple Scan Modes**: Choose from easy (file name), medium (MD5 hash), and hard (SHA256 hash) scanning modes to suit your needs.
- **Fast and Efficient**: Quickly scan directories and subdirectories for duplicate files.
- **Detailed Results**: View detailed information about duplicates including file name, size, creation time, modification time, and path.
- **Batch Operations**: Easily delete all duplicates or only selected files with batch operations.
- **Customizable UI**: Frameless window with custom styling and tooltips for a modern look and feel.
- **Progress Tracking**: Real-time progress bar and statistics to monitor the scanning and deletion processes.

## Technologies Used

- **Python**: The core language used for development.
- **PySide6**: For building the graphical user interface.
- **Hashlib**: For generating MD5 and SHA256 hashes.
- **JSON**: For configuration management.

## Installation

To install and run Duplicate File Finder, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/duplicate-file-finder.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd duplicate-file-finder
    ```
3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Select Directory**: Click the 'Select Folder' button to choose the directory you want to scan.
2. **Choose Scan Mode**: Select the desired scan mode (Easy, Medium, Hard).
3. **Start Scan**: Click the 'Start Scan' button to begin scanning for duplicate files.
4. **View Results**: Examine the results in the table and select duplicates to delete.
5. **Delete Duplicates**: Click 'Delete Selected' or 'Delete All' to remove duplicate files.

## Modules Description

### `FileNameSizeService`

This service finds duplicate files based on their file name and size.

- **Methods**:
  - `get_file_data(file: str) -> Dict`: Returns information about a file including its name, size, creation time, modification time, and path.
  - `find_duplicates(files: List[str])`: Finds duplicate files in a list of file paths based on their file name and size.

```python
def generate_table_data(files: List[str]):
    for duplicate in FileNameSizeService.find_duplicates(files=files):
        yield duplicate

class FileNameSizeService:
    @classmethod
    def get_file_data(cls, file: str) -> Dict:
        file_data = dict()
        file_data["file_name"] = os.path.basename(file)
        file_data["file_size"] = os.path.getsize(file)
        file_data["creation_time"] = datetime.fromtimestamp(os.path.getctime(file)).strftime("%Y-%m-%d %H:%M:%S")
        file_data["modification_time"] = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")
        file_data["file_path"] = file
        return file_data

    @classmethod
    def find_duplicates(cls, files: List[str]):
        cached = set()
        for file in files:
            file_data = cls.get_file_data(file)
            checking_params = (file_data["file_name"], file_data["file_size"])
            if checking_params in cached:
                yield file_data
            else:
                cached.add(checking_params)
                yield None

```

### `HashService`
This service finds duplicate files based on their MD5 or SHA256 hash.

- **Methods**:
  - `get_hash(file_path: str, func: Union[md5, sha256]) -> Dict`: Returns the hash value of a file.
  - `find_duplicates(files: List[str], algorithm: Union[md5, sha256])`: Finds duplicate files in a list of file paths based on their hash value.

```python
def generate_table_data(files: List[str], algorithm: Union[md5, sha256]):
    for duplicate in HashService.find_duplicates(files=files, algorithm=algorithm):
        yield duplicate

class HashService:
    @classmethod
    def get_hash(cls, file_path: str, func: Union[md5, sha256]) -> Dict:
        file_hash = func()
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    @classmethod
    def find_duplicates(cls, files: List[str], algorithm: Union[md5, sha256]):
        hashes = dict()
        for file in files:
            file_data = dict()
            file_data["file_name"] = os.path.basename(file)
            file_data["file_size"] = os.path.getsize(file)
            file_data["creation_time"] = datetime.datetime.fromtimestamp(
                os.path.getctime(file)
            ).strftime("%Y-%m-%d %H:%M:%S")
            file_data["modification_time"] = datetime.datetime.fromtimestamp(
                os.path.getmtime(file)
            ).strftime("%Y-%m-%d %H:%M:%S")
            file_data["file_path"] = file
            file_hash = cls.get_hash(file, algorithm)
            if file_hash in hashes:
                file_data["duplicates"] = hashes[file_hash]["file_name"]
                yield file_data
            else:
                hashes[file_hash] = file_data
                yield None
```

## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please create an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.