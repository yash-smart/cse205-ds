class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        max_ending = 0
        for i in range(len(nums)):
            max_ending += nums[i]
            if(max_subarray<max_ending) :
                max_subarray = max_ending
            if(max_ending < 0) :
                max_ending = 0
        return max_subarray
        