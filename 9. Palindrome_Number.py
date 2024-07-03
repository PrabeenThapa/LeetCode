class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t2=""
        t=str(x)

        t2 = t[::-1]

        if t==t2:
            return True
        else:
            return False
        
s = Solution()
print(s.isPalindrome(-121))