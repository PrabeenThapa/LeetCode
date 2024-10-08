class Solution:
    def numWaterBottles(self,numBottles,numExchange):
        numEmpty, result = 0, 0

        while numBottles:
            result += numBottles
            numEmpty += numBottles
            numBottles  = numEmpty // numExchange
            numEmpty = numEmpty % numExchange

        return result
    

a,b = input().split()
s1=Solution()
result = s1.numWaterBottles(int(a),int(b))
print(result)
