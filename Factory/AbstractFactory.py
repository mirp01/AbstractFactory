from abc import ABC, abstractmethod

class PhoneAccesoriesFactory(ABC):
    @abstractmethod
    def createPhoneCase(self):
        pass

    @abstractmethod
    def createScreenProtector(self):
        pass
