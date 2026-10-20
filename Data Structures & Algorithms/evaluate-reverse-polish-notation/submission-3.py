class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one - two)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(float(one)/two))
            else:
                stack.append(int(n))
                
        return stack[0]


        