class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst = ["Gold Medal","Silver Medal","Bronze Medal"]
        n = len(score)
        res = [-1]*n
        lst2 = []
        for i in range(n) :
            lst2.append([score[i],i])
        lst2.sort(key=lambda x: x[0],reverse=True)
        for i in range(n) :
            if i in [0,1,2] :
                res[lst2[i][1]] = lst[i]
            else :
                res[lst2[i][1]] = str(i+1)
        return res
