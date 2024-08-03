class Solution:
    def canBeEqual(self, list1: List[int], list2: List[int]) -> bool:
        frequency1 = {}
        frequency2 = {}

        for num in list1:
            if num in frequency1:
                frequency1[num] += 1
            else:
                frequency1[num] = 1

        for num in list2:
            if num in frequency2:
                frequency2[num] += 1
            else:
                frequency2[num] = 1

        return frequency1 == frequency2