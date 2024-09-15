from typing import List

class Solution:

    def trap_ascend(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = 1
        cum = 0
        while right < len(height):
            if height[right] >= height[left]:
                total += cum
                left = right
                cum = 0
            else:
                cum += height[left] - height[right]
            
            right += 1

        return total

    def trap(self, height: List[int]) -> int:
        
        tallest = 0

        for i in range(0, len(height)):
            if height[i] > height[tallest]:
                tallest = i

        left_seg = height[0:tallest + 1]
        right_seg = height[tallest:len(height)][::-1]

        return self.trap_ascend(left_seg) + self.trap_ascend(right_seg)
    

sol = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
