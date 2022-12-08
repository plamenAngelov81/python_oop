class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index == len(self.text):
                raise StopIteration
            value_to_get = self.text[self.index]
            if value_to_get in "AaEeOoIiYyUu":
                self.index += 1
                return value_to_get
            self.index += 1


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
#