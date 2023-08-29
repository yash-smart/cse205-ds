class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        result = []
        while True :
            if(len(result) == k) :
                return result[-1]
                break
            if (curr not in arr) :
                result.append(curr)
            curr += 1
            