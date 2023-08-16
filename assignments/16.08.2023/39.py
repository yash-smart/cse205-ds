class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lst1 = []
        candidates.sort()
        self.fun1(candidates, target, 0, [], lst1)
        return lst1
    def fun1(self,nums, target, index, path, lst) :
        if target < 0:
            return  # backtracking
        if target == 0:
            lst.append(path)
            return 
        for i in range(index, len(nums)):
            self.fun1(nums, target-nums[i], i, path+[nums[i]], lst)