from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        length = len(nums)
        
        scores = [[0 for _ in range(length)] for _ in range(length)]


        for i in range(0, length):
            if (nums[i] < length):
                for j in range(nums[i], length):
                    k = length - (j - i) if j > i else i - j
                    #print (f'index: {i}, value: {nums[i]}, scoring index {j}, offset k: {k}')
                    scores[i][k] = 1

        print(scores)

        max_score = 0
        max_k = -1
        for i in range(0, length):
            sum = 0
            for j in range(0, length):
                sum += scores[j][i]

            if sum > max_score:
                max_score = sum
                max_k = i

        return max_k
    
sol = Solution()

nums = [2,3,1,4,0]

print(sol.bestRotation(nums))