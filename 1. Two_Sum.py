class Solution():
    def twoSum(self, nums, target):
        temp = {}
        for index, value in enumerate(nums):
            if value in temp:
                return(temp[value], index)

            else:
                temp[target-value]= index
        return None



s = Solution()
nums = input()
nums = nums.split()
nums = [int(n) for n in nums]
target = int(input())
result = s.twoSum(nums, target)
if result:
    index1, index2 = result
    print(index1, index2)
else:
    print(result)




        