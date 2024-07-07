class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        solution_list = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            try:
                difference = temperatures[index + 1] - temp
            except IndexError:
                solution_list[index] = 0
                continue
            if difference > 0:
                solution_list[index] = 1
                while stack:
                    if temperatures[stack[-1]] >= temperatures[index + 1]:
                        break
                    solution_list[stack[-1]] = (index + 1) - stack[-1]
                    stack.pop(-1)
            else:
                stack.append(index)
        return solution_list
