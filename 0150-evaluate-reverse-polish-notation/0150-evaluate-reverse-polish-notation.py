class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        for ch in tokens:
            if ch in '+-*/':
                b , a = s.pop() , s.pop()
                if ch == '+' : s.append(a+b)
                if ch == '-' : s.append(a-b)
                if ch == '*' : s.append(a*b)
                if ch == '/' : s.append(int(a/b))
            else:
                s.append(int(ch))

        return s[-1]