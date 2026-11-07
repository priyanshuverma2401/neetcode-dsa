class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                start = i
                max_area = max(max_area, (index - i) * h)
            stack.append((start, height))
        
        while stack:
            start, height = stack.pop()
            max_area = max(max_area, (n - start)*height)
        
        return max_area

        