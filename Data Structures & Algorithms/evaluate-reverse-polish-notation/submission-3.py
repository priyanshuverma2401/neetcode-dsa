class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+" or c == "-" or c == "*" or c == "/":
                rightOperand = stack.pop()
                leftOperand = stack.pop()

                match c:
                    case "+":
                        stack.append(leftOperand + rightOperand)
                    case "-":
                        stack.append(leftOperand - rightOperand)
                    case "*":
                        stack.append(leftOperand * rightOperand)
                    case "/":
                        stack.append(int(leftOperand / rightOperand))

            else:
                stack.append(int(c))
        return stack[-1]



        