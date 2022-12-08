from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int):
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str,
                                capacity_consumption: int,
                                memory_consumption: int):
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware_by_name(hardware_name)
        software = System.find_software_by_name(software_name)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f"Hardware Components: {len(System._hardware)}" + "\n"
        result += f"Software Components: {len(System._software)}" + '\n'
        result += f"Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / " \
                  f"{sum(h.memory for h in System._hardware)}" + '\n'
        result += f"Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / " \
                  f"{sum(h.capacity for h in System._hardware)}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f'Express Software Components: {hardware.take_software_by_type()[0]}\n'
            result += f'Light Software Components: {hardware.take_software_by_type()[1]}\n'
            result += f'Memory Usage: {hardware.calculate_total_software_memory_usage()} / ' \
                      f'{hardware.memory}\n'
            result += f"Capacity Usage: {hardware.calculate_total_software_capacity_usage()} / " \
                      f"{hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            result += f"Software Components: {hardware.get_software_components()}\n"
        return result.strip()

    @staticmethod
    def find_hardware_by_name(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware
        return None

    @staticmethod
    def find_software_by_name(software_name):
        for software in System._software:
            if software.name == software_name:
                return software
        return None
