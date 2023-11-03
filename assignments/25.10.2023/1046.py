from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = PriorityQueue()
        for i in stones :
            q.put(-i)
        while (q.qsize() > 1) :
            e1 = -q.get()
            e2 = -q.get()
            if (e1 != e2) :
                q.put(e2-e1)
        if (q.qsize() == 1) :
            return -q.get()
        else :
            return 0