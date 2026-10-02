class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        area = 0

        while left < right: # O(N)
            # print(f"left: {left}, right: {right}")
            min_height = min(heights[left], heights[right])
            area = max(area, (min_height * (right - left)))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area

# Time Complexity: O(N)
# Space Complexity: O(1)
            
        