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
                if (L[i][0]<= R[j][0]) :
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
    def frequencySort(self, s: str) -> str:
        elements = []
        count = []
        for i in s :
            if (i in elements) :
                for j in range(len(elements)) :
                    if (elements[j] == i) :
                        count[j][0] += 1
                        break
            else :
                elements.append(i)
                count.append([1,i])
        self.mergesort(count)
        res = ''
        for k in range(len(count)-1,-1,-1) :
            for l in range(count[k][0]) :
                res += count[k][1]
        return res