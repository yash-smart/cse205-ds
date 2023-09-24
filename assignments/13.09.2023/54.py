class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversal = []
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        print(num_rows, num_columns)
        top = 0
        right = num_columns-1
        bottom = num_rows-1
        left = 0

        while True:

            for t in range(left, right+1):
                print(top, t)
                traversal.append(matrix[top][t])
            top += 1
            if top > bottom:
                return traversal

            for r in range(top, bottom+1):
                print(r, right)
                traversal.append(matrix[r][right])
            right -= 1
            if right < left:
                return traversal

            for b in range(right, left-1, -1):
                print(bottom, b)
                traversal.append(matrix[bottom][b])
            bottom -= 1
            if bottom < top:
                return traversal

            for l in range(bottom, top-1, -1):
                print(l, left)
                traversal.append(matrix[l][left])
            left += 1
            if left > right:
                return traversal