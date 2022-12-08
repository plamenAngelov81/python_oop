from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
        elif aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            new_decoration = Ornament()
            self.decorations_repository.add(new_decoration)
        elif decoration_type == "Plant":
            new_decoration = Plant()
            self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        possible_fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
        if fish_type not in possible_fish_types:
            return f"There isn't a fish of type {fish_type}."
        fish = possible_fish_types[fish_type](fish_name, fish_species, price)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        decoration_price_sum = sum(d.price for d in aquarium.decorations)
        fish_price_sum = sum(f.price for f in aquarium.fish)
        value = decoration_price_sum + fish_price_sum
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"
        return result.strip()
