class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, param):
        current_fill = self.content + param
        if current_fill <= Glass.capacity:
            self.content += param
            return f"Glass filled with {param} ml"
        else:
            return f"Cannot add {param} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        diff = Glass.capacity - self.content
        return f"{diff} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
