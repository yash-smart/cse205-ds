class Solution:
    def mergesort(self,array) :
        if (len(array)>1) :
            mid = len(array)//2
            L = array[:mid]
            R = array[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i = j = k = 0
            while (i<len(L)) and (j<len(R)) :
                if (L[i]<=R[j]) :
                    array[k] = L[i]
                    i+=1
                else :
                    array[k] = R[j]
                    j+=1
                k+=1
            while (i<len(L)) :
                array[k] = L[i]
                i+=1
                k+=1
            while (j<len(R)) :
                array[k] = R[j]
                j+=1
                k+=1
    def arrayPairSum(self, nums: List[int]) -> int:
        self.mergesort(nums)
        sum = 0
        while (nums) :
            nums.pop()
            sum += nums.pop()
        return sum