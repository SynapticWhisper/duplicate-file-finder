import os
from datetime import datetime
from typing import Dict, List


def generate_table_data(files: List[str]):
    """
    Generates table data for duplicate files based on their file name and size.

    args:
    - files: A list of file paths.

    yields:
    - A dictionary containing information about duplicate files.

    """
    for duplicate in FileNameSizeService.find_duplicates(files=files):
        yield duplicate


class FileNameSizeService:
    @classmethod
    def get_file_data(cls, file: str) -> Dict:
        """
        Returns information about a file.

        args:
        - file: A string representing the path to the file.

        returns:
        - A dictionary containing information about the file.

        """
        file_data = dict()
        file_data["file_name"] = os.path.basename(file)
        file_data["file_size"] = os.path.getsize(file)
        file_data["creation_time"] = datetime.fromtimestamp(os.path.getctime(file)).strftime("%Y-%m-%d %H:%M:%S")
        file_data["modification_time"] = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")
        file_data["file_path"] = file
        return file_data

    @classmethod
    def find_duplicates(cls, files: List[str]):
        """
        Finds duplicate files in a list of file paths based on their file name and size.

        args:
        - files: A list of file paths.

        yields:
        - A dictionary containing information about duplicate files.

        """
        cached = set()
        for file in files:
            file_data = cls.get_file_data(file)
            checking_params = (file_data["file_name"], file_data["file_size"])
            if checking_params in cached:
                yield file_data
            else:
                cached.add(checking_params)
                yield None
