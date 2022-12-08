def reverse_text(some_string):
    for i in range(len(some_string) - 1, - 1, -1):
        yield some_string[i]


# for char in reverse_text("step"):
#     print(char, end='')
#