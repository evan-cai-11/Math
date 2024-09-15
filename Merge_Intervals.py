from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_list = sorted(intervals, key = lambda x: x[0])
        output = [sorted_list[0]]
        output_index = 0

        for i in range(1, len(sorted_list)):
            if sorted_list[i][0] <= output[output_index][1]:
                output[output_index][1] = sorted_list[i][1]
            else:
                output.append(sorted_list[i])
                output_index += 1

        return output

            
