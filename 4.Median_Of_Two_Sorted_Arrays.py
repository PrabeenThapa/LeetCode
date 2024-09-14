class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        
        c=0
        for num in nums1:
            c=c+1
        
        if c%2==0:
            return (nums1[c//2]+nums1[c//2-1])/2
        else:
            return nums1[c//2]



s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))
