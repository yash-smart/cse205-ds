class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        curr = nums
        while len(curr) != 1 :
            temp = []
            for i in range(0,len(curr) - 1) :
                temp.append((curr[i]+curr[i+1])%10)
            curr = temp
        return curr[0]