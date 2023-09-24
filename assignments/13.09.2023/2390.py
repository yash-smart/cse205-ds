class Solution:
    def removeStars(self, s: str) -> str:
        lst1 = []
        n = len(s)
        count = 0
        return_string = ''
        for i in range(n-1,-1,-1) :
            if (count == 0) or s[i] == '*' :
                if (s[i] != '*') :
                    lst1.append(s[i])
                if (s[i] == '*') :
                    count += 1
            else :
                count -= 1
        while lst1 :
            return_string += lst1.pop()
        return return_string