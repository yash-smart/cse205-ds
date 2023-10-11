class Solution:
    def mergesort(self,array) :
        if len(array) > 1:
            mid = len(array)//2
            L = array[:mid]
            R = array[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i=j=k=0
            while i<len(L) and j < len(R) :
                if L[i] <= R[j] :
                    array[k] = L[i]
                    i = i+1
                else :
                    array[k] = R[j]
                    j = j+1
                k = k+1
            while i<len(L) :
                array[k] = L[i]
                i = i+1
                k = k+1
            while j<len(R) :
                array[k] = R[j]
                j = j+1
                k = k+1
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        self.mergesort(arr)
        curr = arr[0]
        min = arr[1]-arr[0]
        res = []
        for i in range(1,len(arr)) :
            e = arr[i]
            if (e - curr) < min :
                min = e-curr
            curr = e
        curr = arr[0]
        for i in range(1,len(arr)) :
            e = arr[i]
            if (e - curr) == min :
                res.append([curr,e])
            curr = e
        return res