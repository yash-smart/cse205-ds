class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indexes = [i for i in range(n)]
        indexes = indexes*2
        result = []
        for i in range(n) :
            for j in indexes[i+1::] :
                if (nums[j]>nums[i]) :
                    result.append(nums[j])
                    break
            else :
                result.append(-1)
        return result