class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if self.isOperator(token):
                b = stack.pop()
                a = stack.pop()
                result = self.applyOperator(token, a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()

    def isOperator(self, token: str) -> bool:
        return token in ("+", "-", "*", "/")

    def applyOperator(self, operator: str, a: int, b: int) -> int:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(a / b)
        else:
            raise ValueError("Invalid operator")
