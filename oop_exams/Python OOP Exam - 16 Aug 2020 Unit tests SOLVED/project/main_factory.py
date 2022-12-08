from project.factory.paint_factory import PaintFactory

factory = PaintFactory("Mecha", 10)
factory.add_ingredient("red", 3)
factory.add_ingredient("blue", 5)
print(repr(factory))
