from AbstractProducts import PhoneCase, ScreenProtector

# Apple
class ApplePhoneCase(PhoneCase):
    def create(self):
        return "Creating Apple phone case"

class AppleScreenProtector(ScreenProtector):
    def create(self):
        return "Creating Apple screen protector"

# Samsung
class SamsungPhoneCase(PhoneCase):
    def create(self):
        return "Creating Samsung phone case"

class SamsungScreenProtector(ScreenProtector):
    def create(self):
        return "Creating Samsung screen protector"