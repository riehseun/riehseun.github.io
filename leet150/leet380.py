class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val not in self.positions:
            self.nums.append(val)
            self.positions[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.positions:
            list_index = self.nums[-1]
            dict_index = self.positions[val]
            self.nums[dict_index], self.positions[list_index] = list_index, dict_index
            self.nums.pop()
            self.positions.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()