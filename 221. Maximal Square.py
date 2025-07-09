class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [list(map(int,i)) for i in matrix]


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1


        return max(map(max,matrix))**2

                

        
