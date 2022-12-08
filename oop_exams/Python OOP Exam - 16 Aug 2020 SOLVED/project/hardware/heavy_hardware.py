from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        result = value * 2
        self.__capacity = result

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        result = int(value * 0.75)
        self.__memory = result
