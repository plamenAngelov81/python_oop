from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    FISH_TYPE = "FreshwaterFish"

    def __init__(self, name: str):
        super().__init__(name, 50)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == self.FISH_TYPE:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        return "Water not suitable."
