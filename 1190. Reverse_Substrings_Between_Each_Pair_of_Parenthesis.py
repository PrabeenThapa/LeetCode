class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '(': 
                stack.append("(")
            elif char == ')': 
                r = []
                while stack and stack[-1] != "(":
                    r.append(stack.pop()[::-1])
                stack.pop()
                stack.append("".join(r))
            else:
                stack.append(char)
        
        return "".join(stack)
    
s1 = Solution()
print(s1.reverseParentheses("(u(love)i)"))
