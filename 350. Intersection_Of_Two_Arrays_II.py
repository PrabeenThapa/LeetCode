class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        for i in  nums1:
            if i in nums2:
                nums3.append(i)
                nums2.remove(i)
        return nums3
    
s = Solution()
print(s.intersect([1,2,3],[2,3,4]))


