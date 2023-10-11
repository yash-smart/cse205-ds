class Solution:
    def merge_sort(self,list) :
        if (len(list)>1) :
            mid = len(list) // 2
            L = list[:mid]
            R = list[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i = j = k = 0
            while i<len(L) and j<len(R) :
                if(L[i]<=R[j]) :
                    list[k] = L[i]
                    i+=1
                else :
                    list[k] = R[j]
                    j += 1
                k+= 1
            while (i<len(L)) :
                list[k] = L[i]
                i += 1
                k+= 1
            while (j<len(R)) :
                list[k] = R[j]
                j += 1
                k+= 1
    def majorityElement(self, nums: List[int]) -> int:
        self.merge_sort(nums)
        n = len(nums)
        curr = nums[0]
        count = 0
        for i in range(0,n) :
            if (nums[i] == curr) :
                count += 1
                if (count > n//2) :
                    return nums[i]
            else :
                if (count > n//2) :
                    return nums[i]
                else :
                    count = 1
                    curr = nums[i]
        