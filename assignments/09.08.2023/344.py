class Solution:
    def fun1(self,s,i = 0) :
        if(i < len(s)/2) :
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
            i += 1
            self.fun1(s,i)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.fun1(s)
