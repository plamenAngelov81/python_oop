def up_part(n):
    counter = n - 1
    for i in range(1, n + 1):
        print(" " * counter + "* " * i)
        counter -= 1


def low_part(n):
    for j in range(1, n):
        print(" " * j + "* " * (n - j))


some_num = int(input())
up_part(some_num)
low_part(some_num)
