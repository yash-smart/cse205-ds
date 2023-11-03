from queue import PriorityQueue
class Solution:
    def largestInteger(self, num: int) -> int:
        q = PriorityQueue()
        q2 = PriorityQueue()
        n = len(str(num))
        nums = [int(i) for i in str(num)]
        for i in range(n) :
            q.put((nums[i]%2,-nums[i]))
            q2.put((nums[i]%2,i))
        for i in range(n) :
            nums[q2.get()[1]] = -q.get()[1]
        str1 = ''
        for i in nums :
            str1 += str(i)
        return int(str1)