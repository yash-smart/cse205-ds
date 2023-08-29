class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        lst1 = []
        for i in nums :
            if (i != 1) :
                lst1.append(count)
                count = 0 
            else :
                count += 1
        lst1.append(count)
        return max(lst1)