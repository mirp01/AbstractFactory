from abc import ABC, abstractmethod

class PhoneCase(ABC):
    @abstractmethod
    def create(self):
        pass

class ScreenProtector(ABC):
    @abstractmethod
    def create(self):
        pass