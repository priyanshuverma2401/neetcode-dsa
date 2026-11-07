class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_l, max_r = height[0], height[-1]
        total_water = 0

        water_p = [0 for _ in range(len(height))]

        while left < right:
            if height[left] > height[right]:
                right-=1
                water = min(max_l, max_r) - height[right]
                if water > 0: total_water += water
                # water_p[right] = water if water > 0 else 0
                max_r = max(max_r, height[right])

            else:
                left+=1
                water = min(max_l, max_r) - height[left]
                if water > 0: total_water += water
                # water_p[left] = water if water > 0 else 0
                max_l = max(max_l, height[left])
        # print(water_p)
        return total_water
                
        