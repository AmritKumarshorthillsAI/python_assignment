from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def store(self, data):
        """Store the extracted data."""
        pass
