class Solution:
    def mergesort(self,arr) :
        if (len(arr)>1) :
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i=j=k=0
            while (i<len(L)) and (j<len(R)) :
                if (L[i]<=R[j]) :
                    arr[k] = L[i]
                    i+=1
                else :
                    arr[k] = R[j]
                    j+=1
                k+=1
            while (i<len(L)) :
                arr[k] = L[i]
                i+=1
                k+=1
            while (j<len(R)) :
                arr[k] = R[j]
                j+=1
                k+=1
    def binsearch(self,arr,element) :
        l = 0
        h = len(arr)-1
        while (l<=h) :
            mid = l + (h-l)//2
            if (arr[mid] == element) :
                indexes = []
                curr = mid
                while curr>= 0 and (arr[curr] == element) :
                    indexes.append(curr)
                    curr -= 1
                curr = mid+1
                while curr<len(arr) and (arr[curr]==element) :
                    indexes.append(curr)
                    curr+=1
                return indexes
            elif (arr[mid] < element) :
                l = mid +1
            else :
                h = mid-1
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.mergesort(arr1)
        res = []
        index = []
        for i in arr2 :
            indexes = self.binsearch(arr1,i)
            for j in indexes :
                res.append(arr1[j])
                index.append(j)
        for i in range(len(arr1)) :
            if (i not in index) : 
                res.append(arr1[i])
        return res