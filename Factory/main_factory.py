from ConcreteFactory import AppleAccesoriesFactory, SamsungAccesoriesFactory

# Client
def createProduct(factory):
    phoneCase = factory.createPhoneCase()
    screenProtector = factory.createScreenProtector()
    
    print(phoneCase.create())
    print(screenProtector.create())

# main
if __name__ == "__main__":
    print("Apple Accesories Factory:")
    createProduct(AppleAccesoriesFactory())
    
    print("\nSamsung Accesories Factory:")
    createProduct(SamsungAccesoriesFactory())