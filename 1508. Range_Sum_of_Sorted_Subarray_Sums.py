
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        
        # Create prefix sums array
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        # Initialize a min-heap to store subarray sums
        min_heap = []
        for i in range(1, n + 1):
            for j in range(i):
                heapq.heappush(min_heap, prefix_sums[i] - prefix_sums[j])
        
        # Calculate the result within the range [left, right]
        total_sum = 0
        for i in range(1, right + 1):
            current_sum = heapq.heappop(min_heap)
            if i >= left:
                total_sum = (total_sum + current_sum) % MOD
        
        return total_sum
