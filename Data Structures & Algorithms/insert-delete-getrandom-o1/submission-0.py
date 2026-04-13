class RandomizedSet:
    import random
    # randomizedSet.insert(1)
    # {1: 0} [1]
    # randomizedSet.insert(2)
    # randomizedSet.insert(3)
    # {1: 0, 2: 1, 3:2} [1,2,3]
    # {value: index}
    # randomizedSet.remove(2)
    # find index in hashset
    # swap with list in list
    # want to delete from end pop O(1) and del from numSet
    # {1: 0, 2: 1, 3:2} [1,2,3]
    # index = 1
    # [1,3,3] swap whats at index 1 with the last element
    # {1: 0, 2: 1, 3:1}
    # [1,3] pop last element
    # {1: 0, 3:1} delete 2 from hashmap

    def __init__(self):
        # initialize hashmap for O(1) lookup
        # initiaize list for O(1) get random index
        self.numSet = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        # return false if value is present
        if val in self.numSet:
            return False
        # if value is not present, insert into set and list O(1)
        self.numSet[val] = len(self.numList)
        self.numList.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        # check if in hashSet. if yes remove and return True
        if val not in self.numSet:
            return False
        # find index in hashSet O(1)
        index = self.numSet[val]
        # swap with last in list
        self.numList[index] = self.numList[-1]
        # update swapped element in hashset
        self.numSet[self.numList[-1]] = index
        # delete from numSet and list
        self.numList.pop()
        del self.numSet[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()