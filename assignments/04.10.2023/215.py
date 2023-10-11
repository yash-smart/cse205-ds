class Solution:
    def mergesort(self,lst1) :
        if (len(lst1) > 1) :
            mid = len(lst1)//2
            L = lst1[:mid]
            R = lst1[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i=j=k=0
            while (i<len(L)) and (j<len(R)) :
                if (L[i]<= R[j]) :
                    lst1[k] = L[i]
                    i+=1
                else :
                    lst1[k] = R[j]
                    j+=1
                k+=1
            while (i<len(L)) :
                lst1[k] = L[i]
                i+=1
                k+=1
            while (j<len(R)) :
                lst1[k] = R[j]
                j+=1
                k+=1
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.mergesort(nums)
        curr = -1
        for i in range(k-1) :
            curr -= 1
        return nums[curr]