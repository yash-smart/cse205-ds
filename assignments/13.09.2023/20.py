class stack :
    def __init__(self) :
        self.stack = []
    def push(self,val) :
        self.stack.append(val)
    def top(self) :
        return self.stack[-1]
    def pop(self) :
        return self.stack.pop()
class Solution:
    def isValid(self, s: str) -> bool:
        stck = stack()
        for i in s :
            if i in ('(','{','[') :
                stck.push(i)
            elif i == ')' :
                if stck.stack and (stck.top() == '(') :
                    stck.pop()
                else :
                    return False
            elif i == '}' :
                if stck.stack and (stck.top() == '{') :
                    stck.pop()
                else :
                    return False
            elif i == ']' :
                if stck.stack and (stck.top() == '[') :
                    stck.pop()
                else :
                    return False
            else :
                return False
        if (len(stck.stack) == 0) :
            return True
        else :
            return False