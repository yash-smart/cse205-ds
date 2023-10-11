class Solution:
    def mergesort(self,lst1) :
        if (len(lst1)>1) :
            mid = len(lst1)//2
            L = lst1[:mid]
            R = lst1[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i=j=k=0
            while (i<len(L)) and (j<len(R)) :
                if (ord(L[i])<=ord(R[j])) :
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
            while j<len(R) :
                lst1[k] = R[j]
                j+=1
                k+=1
    def binarysearch(self,lst1,e) :
        l = 0
        h = len(lst1)-1
        while (l<=h) :
            mid = l + (h-l)//2
            if(lst1[mid]==e) :
                curr = mid
                count = 0
                while (curr>=0) and (lst1[curr] == e) :
                    count += 1
                    curr -=1
                curr = mid+1
                while (curr<len(lst1) and (lst1[curr] == e)) :
                    count += 1
                    curr += 1
                return count
            elif (ord(lst1[mid]) < ord(e)) :
                l = mid+1
            else :
                h = mid-1
        return -1
    def customSortString(self, order: str, s: str) -> str:
        lst1 = [i for i in s]
        self.mergesort(lst1)
        res = ''
        for i in order :
            count = self.binarysearch(lst1,i)
            if (count != -1) :
                for j in range(count) :
                    res += i
        for k in lst1 :
            if (k not in order) :
                res += k
        return res