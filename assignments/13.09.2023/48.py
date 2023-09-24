class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range (length) :
            temp = []
            for j in range(length-1,-1,-1) :
                temp.append(matrix[j][i])
            matrix.append(temp.copy())
        for i in range(length) :
            matrix.pop(0)