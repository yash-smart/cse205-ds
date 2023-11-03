from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = []
        count = []
        q = PriorityQueue()
        for i in nums :
            if (i in elements) :
                for j in range(len(elements)) :
                    if (elements[j] == i) :
                        count[j][0] += 1
                        break
            else :
                elements.append(i)
                count.append([1,i])
        for i in count :
            q.put((-i[0],i[1]))
        ans = []
        for i in range(k) :
            ans.append(q.get()[1])
        return ans