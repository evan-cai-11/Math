from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        layer = 0

        while layer < n // 2:
            print("Layer: ", layer)
            for i in range(layer, n - layer - 1):
                print(f'Starting pos: ({layer}, {i})')
                print(f'Second pos: ({i}, {n - layer - 1})')
                print(f'Third pos: ({n - layer - 1}, {n - i - 1})')
                print(f'Fourth pos: ({n - i - 1}, {layer})')

                v2 = matrix[i][n - layer - 1]
                matrix[i][n - layer - 1] = matrix[layer][i]
                t3 = matrix[n - layer - 1][n - i - 1]
                matrix[n - layer - 1][n - i - 1] = v2
                t4 = matrix[n - i - 1][layer]
                matrix[n - i - 1][layer] = t3
                matrix[layer][i] = t4

            layer += 1

        
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
sol.rotate(matrix)
print("Matrix after rotation", matrix)
