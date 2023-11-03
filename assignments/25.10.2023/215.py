from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for i in nums :
            q.put(-i)
        for i in range(k-1) :
            q.get()
        return -q.get()