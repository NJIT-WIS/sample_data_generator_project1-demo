"""File operations """
import os


class FileOperations:
    @staticmethod
    def get_project_root_directory():
        """Get root project directory"""
        return os.getcwd()

    @staticmethod
    def get_calculate_file_path(data_directory, data_file_name):
        """Calculate File path"""
        return os.path.join(FileOperations.get_project_root_directory(), data_directory, data_file_name)
