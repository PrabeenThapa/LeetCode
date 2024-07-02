class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = ""
        tmp=""
        dct = {}
        count = 0
        for char in s:
            if char in lst:
                dct[count]=[lst]
                for c in lst:
                    if c == char:
                        tmp = ""
                        count=0
                        continue
                    count+=1
                    tmp+=c
                lst = tmp
            lst+=char
            count+=1
        dct[count]= [lst]
        print(dct)
        return max(dct.keys())


test = Solution()
length= test.lengthOfLongestSubstring("abac")
print("Length of longest substring : ", length)