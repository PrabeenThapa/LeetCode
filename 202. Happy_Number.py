class Solution():
    def isHappy(self,n):
        alist = []
        sum = 0
        while sum not in alist:
            alist.append(sum)
            sum = 0
            while n:
                a = n%10
                n = n//10
                sum = sum + a**2
            n=sum
            print(sum)
            print(alist)
            if sum == 1:
                return True
h1 = Solution()
if h1.isHappy(2):
    print("Happy Number.")
else:
    print("Not a Happy Number.")