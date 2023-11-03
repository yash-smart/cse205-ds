from queue import PriorityQueue
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        q = PriorityQueue()
        for i in nums :
            q.put(-i)
        if (not q.empty()) :
            e1 = q.get()
        if (not q.empty()) :
            e2 = q.get()
        return (-e1-1)*(-e2-1)