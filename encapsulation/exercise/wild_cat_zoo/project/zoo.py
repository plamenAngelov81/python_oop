from my_tests.project import Caretaker
from my_tests.project import Cheetah
from my_tests.project import Keeper
from my_tests.project import Lion
from my_tests.project import Tiger
from my_tests.project import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_workers_salary = 0
        for worker in self.workers:
            all_workers_salary += worker.salary

        if all_workers_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= all_workers_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_care_spending = 0

        for animal in self.animals:
            animal_care_spending += animal.money_for_care

        if animal_care_spending > self.__budget:
            return "You have no budget to tend the wild_farm. They are unhappy."

        self.__budget -= animal_care_spending
        return f"You tended all the wild_farm. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} wild_farm\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs) + '\n'

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'

        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'

        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets) + '\n'

        return result.strip()
