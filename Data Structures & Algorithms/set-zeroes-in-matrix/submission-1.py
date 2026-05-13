class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        b = [[matrix[r][c] for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    for k in range(cols):
                        b[r][k]=0
                    for a in range(rows):
                        b[a][c]=0

        for r in range(rows):
            for c in range(cols):
                matrix[r][c]=b[r][c]                   
                    
                    

        
        