from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.memory_consumption <= self.available_memory and \
                software.capacity_consumption <= self.available_capacity:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    @property
    def available_memory(self):
        return self.memory - sum(s.memory_consumption for s in self.software_components)

    @property
    def available_capacity(self):
        return self.capacity - sum(c.capacity_consumption for c in self.software_components)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    def take_software_by_type(self):
        light = 0
        express = 0
        for software in self.software_components:
            if software.software_type == "Light":
                light += 1
            elif software.software_type == "Express":
                express += 1
        return [express, light]

    def calculate_total_software_memory_usage(self):
        memory_usage = sum(s.memory_consumption for s in self.software_components)
        return memory_usage

    def calculate_total_software_capacity_usage(self):
        capacity_usage = sum(c.capacity_consumption for c in self.software_components)
        return capacity_usage

    def get_software_components(self):
        result = ''
        if len(self.software_components) > 0:
            result += f"{', '.join(s.name for s in self.software_components)}"
        else:
            result += 'None'
        return result
