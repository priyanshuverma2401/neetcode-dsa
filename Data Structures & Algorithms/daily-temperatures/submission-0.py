class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_arr = [0 for _ in range(len(temperatures))]
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, i = stack.pop()
                output_arr[i] = index - i
            stack.append((temp, index))
        return output_arr
        