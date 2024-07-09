class Solution(object):

    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        i = 1
        temp = customers[0][0] + customers[0][1]
        sum_wait = customers[0][1]
        
        while i < len(customers):
            if temp > customers[i][0]:
                wait_time = temp - customers[i][0] + customers[i][1]
                sum_wait += wait_time
                temp += customers[i][1]
            else:
                sum_wait += customers[i][1]
                temp = customers[i][0] + customers[i][1]
            i += 1
        
        result = sum_wait / len(customers)
        return result
    
s = Solution()
print(s.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))
