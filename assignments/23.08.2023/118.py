class Solution:
    def __init__(self) :
        self.rows = []
    def helper(self,n) :
        curr = [1]
        if (self.rows) :
            for i in range(len(self.rows[-1])-1) :
                curr.append(self.rows[-1][i] + self.rows[-1][i+1])
        if(n == 1) :
            self.rows.append(curr)
        else :
            curr.append(1)
            self.rows.append(curr)
    def generate(self, numRows: int) -> List[List[int]]:
        for i in range(1,numRows+1) :
            self.helper(i)
        return self.rows