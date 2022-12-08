from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Sandy"))
print(space_station.add_astronaut("Meteorologist", "Mandy"))
print(space_station.add_astronaut("Geodesist", "Mindy"))
print(space_station.add_astronaut("Biologist", "Tiffany"))
print(space_station.add_astronaut("Meteorologist", "Sindy"))
print(space_station.add_astronaut("Geodesist", "John"))
print(space_station.add_astronaut("Biologist", "Eve"))

print(space_station.add_planet("Arcadia", "stone, animal sceleton, plants, laser rifle, ancient artifact, treasure, "
                                          "blp pistol, titanium armor, plasma long range rifle, fuel, robot parts, "
                                          "little radar"))
print(space_station.add_planet("Calypso", "repair tools, beginner rifle, vehicle part, iron ore, animal skin, axe, "
                                          "knife, pipe, old tire, laser ammo, plush toy, ore extracting tool"))
print(space_station.send_on_mission("Arcadia"))
space_station.recharge_oxygen()
print(space_station.send_on_mission("Calypso"))
space_station.recharge_oxygen()
print(space_station.report())
