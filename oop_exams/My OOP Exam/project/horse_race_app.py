from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def find_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey
        return None

    def horse_is_taken(self, horse_type):
        for index in range(len(self.horses) - 1, - 1, -1):
            if self.horses[index].__class__.__name__ == horse_type:
                if not self.horses[index].is_taken:
                    return self.horses[index]
        return None

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_dict = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
        if horse_type not in horse_dict:
            return
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        horse = horse_dict[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.horse_is_taken(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey.name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_race_by_type(race_type)
        jockey = self.find_jockey_by_name(jockey_name)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        sorted_jockey_list = sorted(race.jockeys, key=lambda x: x.horse.speed)

        winner = sorted_jockey_list[-1]
        result = f"The winner of the {race.race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
                 f"Winner's horse: {winner.horse.name}."
        return result




