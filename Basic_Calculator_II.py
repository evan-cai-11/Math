from typing import List
from collections import deque

class Solution():
   
    def split_keep_delimitor(self, s: str, delimitors: set) -> List[str]:
        last = 0
        tokens = []
        for i in range(len(s)):
            if s[i] in delimitors:
                if (i > last):
                    tokens.append(s[last:i])
    
                tokens.append(s[i])
    
                last = i + 1

        if (last < len(s)):
            tokens.append(s[last:])

        return tokens

    def eval(self, stack: List[str], right: int) -> int:
        op = stack.pop()
        left = stack.pop() 

        if (op == '+'):
            return left + right
        else:
            return left - right
   
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        delimitors = set(['+', '-', '(', ')'])
        tokens = self.split_keep_delimitor(s, delimitors)
        print("Tokens: ", tokens)
        stack = []

        for t in tokens:
            if t == ')':
                num = stack.pop()
                left_paran = stack.pop()
                if len(stack) == 0:
                    stack.append(num)
                else:
                    stack.append(self.eval(stack, num))
            elif t in delimitors:
                stack.append(t)
            else:
                num = int(t) if len(t) > 0 else 0
                if len(stack) == 0 or stack[len(stack) - 1] == '(':
                    stack.append(num)
                else:
                    stack.append(self.eval(stack, num))

            print(stack)

        return stack.pop()

sol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
print(sol.calculate(s))