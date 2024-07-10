class Solution:
    def minOperations(self, logs: list[str]) -> int:
        c = 0
        for val in logs:
            if val == "../":
                if c>0:
                    c-=1
            elif val != "./":
                c+=1

        return c

logs = ["d1/","../","../","../"]
s1 = Solution()
step=s1.minOperations(logs)
print(step)