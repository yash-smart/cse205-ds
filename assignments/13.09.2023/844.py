class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr1 = []
        arr2 = []
        for i in s :
            if (i == '#') :
                if (arr1) :
                    arr1.pop()
            else :
                arr1.append(i)
        for j in t :
            if (j == '#') :
                if (arr2) :
                    arr2.pop()
            else :
                arr2.append(j)
        return arr1 == arr2