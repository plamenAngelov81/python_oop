from project.bakery import Bakery

bakery = Bakery("Mindy's plate")
print(bakery.add_food("Bread", "Food_1", 1.50))
print(bakery.add_food("Bread", "Food_2", 2.50))
print(bakery.add_food("Cake", "Cream Caramel", 2.00))
print(bakery.add_drink("Tea", "Green", 1.50, "Best Tea"))
print(bakery.add_drink("Water", "Best Water", 1.30, "East Well"))
print(bakery.add_drink("Water", "Some Water Name", 1.40, "Golden Well"))
print(bakery.add_drink("Tea", "Black", 1.80, "Like Tea"))
print(bakery.add_table("OutsideTable", 60, 5))
print(bakery.add_table("InsideTable", 10, 10))
print(bakery.add_table("OutsideTable", 70, 6))
print(bakery.add_table("InsideTable", 32, 15))
print(bakery.add_table("OutsideTable", 75, 15))
print(bakery.add_table("OutsideTable", 55, 4))
print(bakery.add_table("InsideTable", 20, 5))
print(bakery.reserve_table(5))
print(bakery.reserve_table(10))
print(bakery.reserve_table(9))

print(bakery.order_food(55, "Cream Caramel", "Food_1", "Food_2", "Grilled Chicken"))
print(bakery.order_drink(20, "Best Water", "Black", "Green", "Beer"))

print(bakery.leave_table(20))
print(bakery.leave_table(55))

print(bakery.get_total_income())
print(bakery.get_free_tables_info())
