class Solution:
    def mergeSort(self,arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    def findNonMinOrMax(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        min = nums[0]
        max = nums[len(nums)-1]
        for i in nums :
            if (i != min) and (i!= max):
                return i
        return -1