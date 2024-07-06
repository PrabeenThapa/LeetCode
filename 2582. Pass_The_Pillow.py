class Solution:
    def passThePillow(self, n, time):
        t = time // (n - 1)
        pos = time % (n - 1)

        if t % 2 == 1:
            return n - pos
        else:
            return 1 + pos
        

s = Solution()
n = s.passThePillow(3,5)
print(n)