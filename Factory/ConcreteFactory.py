from AbstractFactory import PhoneAccesoriesFactory
from ConcreteProducts import ApplePhoneCase, AppleScreenProtector, SamsungPhoneCase, SamsungScreenProtector

# Apple Factory
class AppleAccesoriesFactory(PhoneAccesoriesFactory):
    def createPhoneCase(self):
        return ApplePhoneCase()

    def createScreenProtector(self):
        return AppleScreenProtector()

# Samsung Factory
class SamsungAccesoriesFactory(PhoneAccesoriesFactory):
    def createPhoneCase(self):
        return SamsungPhoneCase()

    def createScreenProtector(self):
        return SamsungScreenProtector()
