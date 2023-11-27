#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name,breed):
        self._name = name
        self._breed=breed

    def set_name(self, name):
        if isinstance(name, str) and len(name) <= 25:
            self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def set_breed(self, breed):
        if breed in self.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def get_breed(self):
        return self._breed

    breed = property(get_breed, set_breed)

# Testing
fido = Dog("fido", "Bulldog")
print(fido.breed)  # Output: Bulldog


fido = Dog("fido","Bulldog")
fido.name = "Rex"  # Setting a different name
print(fido.name)  # This will print: "Rex"


