from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max = 0
        while (left < right):
            area = 0
            if (height[left] <= height[right]):
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1

            max = area if area > max else max

        return max
