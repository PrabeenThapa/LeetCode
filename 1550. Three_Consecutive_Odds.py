class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in arr:
            if i%2!=0:
                count +=1
                if count>=3:
                    return True
                continue
            count = 0       
s = Solution()
result = s.threeConsecutiveOdds([1,1,3,4,6])

print("Three consecutive Odd: ", result)