import datetime
from hashlib import md5, sha256
from typing import List, Union, Dict
import os


def generate_table_data(files: List[str], algorithm: Union[md5, sha256]):
    """
    Generates table data for duplicate files.

    args:
    - files: A list of file paths.
    - algorithm: An instance of md5 or sha256 algorithm.

    yields:
    - A dictionary containing information about duplicate files.

    """
    for duplicate in HashService.find_duplicates(files=files, algorithm=algorithm):
        yield duplicate


class HashService:
    @classmethod
    def get_hash(cls, file_path: str, func: Union[md5, sha256]) -> Dict:
        """
        Returns the hash value of a file.

        args:
        - file_path: A string representing the path to the file.
        - func: An instance of md5 or sha256 algorithm.

        returns:
        - A dictionary containing the hash value of the file.

        """
        file_hash = func()
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    @classmethod
    def find_duplicates(cls, files: List[str], algorithm: Union[md5, sha256]):
        """
        Finds duplicate files in a list of file paths.

        args:
        - files: A list of file paths.
        - algorithm: An instance of md5 or sha256 algorithm.

        yields:
        - A dictionary containing information about duplicate files.

        """
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
