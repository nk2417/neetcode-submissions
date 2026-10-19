class Solution:
    def calPoints(self, operations: List[str]) -> int:
        baseball_stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                one = baseball_stack[-1]
                two = baseball_stack[-2]
                total = int(one) + int(two)
                baseball_stack.append(total)
            elif operations[i] == "D":
                one = baseball_stack[-1]
                total = int(one) * 2
                baseball_stack.append(total)
            elif operations[i] == "C":
                baseball_stack.pop()
            else:
                baseball_stack.append(int(operations[i]))

        return sum(baseball_stack)



        