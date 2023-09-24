class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix[0])
        transpose = [[] for i in range(length)] 
        for i in matrix :
            for j in range(length) :
                transpose[j].append(i[j])
        return transpose