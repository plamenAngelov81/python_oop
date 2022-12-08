class Calculator:

    @staticmethod
    def add(*args):
        add_result = sum(args)
        return add_result

    @staticmethod
    def multiply(*args):
        multiply_result = 1
        for i in args:
            multiply_result *= i
        return multiply_result

    @staticmethod
    def divide(*args):
        divide_result = args[0]
        for y in args[1:]:
            divide_result /= y
        return divide_result

    @staticmethod
    def subtract(*args):
        subtract_result = args[0]
        for j in args[1:]:
            subtract_result -= j
        return subtract_result


# print(Calculator.add(5, 5, 5))
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2, 2, 5, 5))
# print(Calculator.subtract(90, 20, -50, 43, 7))
