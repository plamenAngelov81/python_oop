def genrange(start_num, end_num):
    for i in range(start_num, end_num + 1):
        yield i


# print(list(genrange(1, 10)))