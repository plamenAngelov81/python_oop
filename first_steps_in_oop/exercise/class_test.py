class Obj:
    def __init__(self, nums):
        self.nums = nums

    def get_nums(self):
        return len(self.nums)


obj = Obj([1, 2, 3])
print(obj.get_nums())
