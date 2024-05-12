import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second_number = stack.pop(-1)
                stack[-1] = int(operators[token](stack[-1], second_number))
                continue
            stack.append(int(token))
        return stack[0]