from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_last_free_car_by_type(self, car_type):
        for i in range(len(self.cars) - 1, - 1, - 1):
            car = self.cars[i]
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        return None

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car_type_list = ["MuscleCar", "SportsCar"]
        if car_type not in car_type_list:
            return
        for current_car in self.cars:
            if current_car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_last_free_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None and not car.is_taken:
            old_car = driver.car
            old_car.is_taken = False
            car.is_taken = True
            driver.car = car
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        if driver.car is None and not car.is_taken:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):

        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        # if race is None:
            #raise Exception(f"Race {race_name} could not be found!")

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for driver in race.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)

        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        winners = sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]

        result = ''
        for driver in winners:
            driver.number_of_wins += 1
            result += f'Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n'
        return result.strip()
