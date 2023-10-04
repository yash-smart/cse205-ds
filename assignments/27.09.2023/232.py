class stack :
    def __init__(self) :
        self.stck = []
    def push(self,item) :
        self.stck.append(item)
    def peek(self) :
        return self.stck[-1]
    def pop(self) :
        return self.stck.pop()
    def size(self) :
        return len(self.stck)
    def is_empty(self) :
        return len(self.stck) == 0
class MyQueue:

    def __init__(self):
        self.stack = stack()
    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        temp = stack()
        n = self.stack.size()
        if (n == 1) :
            return self.stack.pop()
        else :
            while (temp.size() != n-1) :
                temp.push(self.stack.pop())
            return_val = self.stack.pop()
            while (temp.is_empty() == False) :
                self.stack.push(temp.pop()) 
            return return_val

    def peek(self) -> int:
        temp = stack()
        while (self.stack.stck) :
            temp.push(self.stack.pop())
        
        return_val =  temp.peek()
        while (temp.stck) :
            self.stack.push(temp.pop())
        return return_val
    def empty(self) -> bool:
        return self.stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()