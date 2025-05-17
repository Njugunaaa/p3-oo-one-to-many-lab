class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        my_pets = []
        for pet in Pet.all:
            if pet.owner == self:
                my_pets.append(pet)
        return my_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a pet!")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("That's not a valid pet type.")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
