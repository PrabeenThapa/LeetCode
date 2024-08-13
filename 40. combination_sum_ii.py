from typing import List

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def search_combinations(start_index: int, remaining_sum: int, path: List[int]):
            if remaining_sum == 0:
                combinations.append(path.copy())
                return
            
            for index in range(start_index, len(nums)):
                if index > start_index and nums[index] == nums[index - 1]:
                    continue
                if nums[index] > remaining_sum:
                    break
                
                path.append(nums[index])
                search_combinations(index + 1, remaining_sum - nums[index], path)
                path.pop()

        combinations = []
        nums.sort()
        search_combinations(0, target, [])
        return combinations
