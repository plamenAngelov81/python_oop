from project.plantation import Plantation

plantation = Plantation(5)
plantation.hire_worker("John")
plantation.hire_worker("Lily")
plantation.planting("John", "corn")
plantation.planting("John", "garlic")
plantation.planting("John", "onion")
plantation.planting("Lily", "tomato")
plantation.planting("Lily", "roses")
print(plantation.__str__())
