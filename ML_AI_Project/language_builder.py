import string
class Language:
    def __init__(self) -> None:
        pass

    def alphabet(self):
        alpha_dict = list(string.ascii_letters)
        print(alpha_dict)

print(Language.alphabet(''))