class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        total_water = 0

        # calculating left max for each element
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        
        # calculating the right max for each element
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])

        # print(f"left_max arr: {left_max}")
        # print(f"right_max arr: {right_max}")
        
        
        # calculating the amount of water for each position.
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            # print(water)
            if water > 0: total_water += water

        return total_water
        