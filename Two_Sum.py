from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Use sorted() with enumerate() to keep track of original indices
        sorted_with_indices = sorted(enumerate(nums), key=lambda x: x[1])

        # Separate the sorted numbers and the original indices
        sorted_numbers = [x[1] for x in sorted_with_indices]
        original_indices = [x[0] for x in sorted_with_indices]

        start = 0
        end = len(nums) - 1
        while(start < end):
            if sorted_numbers[start] + sorted_numbers[end] > target:
                end -= 1
            elif sorted_numbers[start] + sorted_numbers[end] < target:
                start += 1
            else:
                return [original_indices[start], original_indices[end]]

        return []           