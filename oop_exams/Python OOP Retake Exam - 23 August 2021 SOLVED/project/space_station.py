
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.complete_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        else:
            if astronaut_type == "Biologist":
                new_astronaut = Biologist(name)
                self.astronaut_repository.add(new_astronaut)
            elif astronaut_type == "Geodesist":
                new_astronaut = Geodesist(name)
                self.astronaut_repository.add(new_astronaut)
            elif astronaut_type == "Meteorologist":
                new_astronaut = Meteorologist(name)
                self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.astronauts.remove(astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        ready_astronauts = [astr for astr in self.astronaut_repository.astronauts if astr.oxygen > 30]
        if len(ready_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        mission_ready_astronauts = sorted(ready_astronauts, key=lambda a: -a.oxygen)
        if len(mission_ready_astronauts) > 5:
            mission_ready_astronauts = mission_ready_astronauts[:5]
        walking_space_astronauts = 0
        for astronaut in mission_ready_astronauts:
            if len(planet.items) == 0:
                break

            while astronaut.oxygen >= astronaut.BREATHE and len(planet.items) > 0:
                item = planet.items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()

            walking_space_astronauts += 1

        if len(planet.items) == 0:
            self.complete_missions += 1
            return f"Planet: {planet_name} was explored. " \
                f"{walking_space_astronauts} astronauts participated in collecting items."
        else:
            self.failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.complete_missions} successful missions!" + "\n"
        result += f"{self.failed_missions} missions were not completed!" + "\n"
        result += "Astronauts' info:" + "\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}" + "\n" + \
                      f"Oxygen: {astronaut.oxygen}" + "\n" + \
                      f"Backpack items: {', '.join(astronaut.backpack) if len(astronaut.backpack) > 0 else 'none'}" + \
                      "\n"
        return result.strip()

