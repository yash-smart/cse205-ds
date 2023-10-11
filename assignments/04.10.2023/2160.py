class Solution:
    def merge_sort(self,arr) :
        length = len(arr)
        if (length>1) :
            mid = length//2
            L = arr[:mid]
            R = arr[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i=j=k=0
            while (i<len(L)) and (j<len(R)) :
                if (L[i]<=R[j]) :
                    arr[k] = L[i]
                    i += 1
                else :
                    arr[k] = R[j]
                    j+= 1
                k += 1
            while (i < len(L)) :
                arr[k] = L[i]
                i += 1
                k += 1
            while (j < len(R)) :
                arr[k] = R[j]
                j += 1
                k += 1
    def minimumSum(self, num: int) -> int:
        nums = []
        for i in str(num) :
            nums.append(int(i))
        self.merge_sort(nums)
        return (nums[0]*10+nums[-1]) + (nums[1]*10+nums[-2])