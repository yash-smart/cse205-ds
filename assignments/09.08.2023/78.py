class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def fun1(i,curr) :
            if i>= len(nums) :
                subsets.append(curr.copy())
                return
            curr.append(nums[i])
            fun1(i+1,curr)
            curr.pop()
            fun1(i+1,curr)
        fun1(0,[])
        return subsets