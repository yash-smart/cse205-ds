from queue import PriorityQueue
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [-1]*n
        lst1 = ["Gold Medal","Silver Medal","Bronze Medal"]
        q = PriorityQueue()
        for i in range(n) :
            q.put((-score[i],i))
        for i in range(n) :
            e = q.get()
            if (i<3) :
                res[e[1]] = lst1[i]
            else :
                res[e[1]] = str(i+1)
        return res