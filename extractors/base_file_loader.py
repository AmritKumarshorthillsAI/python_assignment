from abc import ABC, abstractmethod

class FileLoader(ABC):
    @abstractmethod
    def load_file(self, file_path):
        """Load the specified file."""
        pass

    @abstractmethod
    def validate_file(self, file_path):
        """Validate the file type."""
        pass
