class Solution:
    def __init__(self) :
        self.lst1 = []
        self.lst2 = []
        self.j = None
        self.prev = []
    def subsets(self,i=0) :
        if (i == 0) :
            self.prev = [[],[self.lst1[i]]]
            self.subsets(i+1)
        elif(i == self.j) :
            self.lst2 = self.prev

        else :
            temp = []
            for k in self.prev :
                temp.append(k + [self.lst1[i]])
            for h in temp :
                self.prev.append(h)
            self.subsets(i+1)
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.lst1 = [i for i in range(1,n+1)]
        self.j = n
        self.subsets()

        return [i for i in self.lst2 if len(i) == k]
        