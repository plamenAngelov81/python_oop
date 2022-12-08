from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    FISH_TYPE = "SaltwaterFish"

    def __init__(self, name: str):
        super().__init__(name, 25)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == self.FISH_TYPE:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        return "Water not suitable."
