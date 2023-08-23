class Solution:

    def __init__(self):
        self.combinations = []

    def next_char(self, current_str:str, n:int, op: int, cl:int):
        if op == n and cl == n:
            self.combinations.append(current_str)
        else:
            if op < n:
                self.next_char(current_str+'(', n, op+1, cl)
            if cl < n and cl < op:
                self.next_char(current_str+')', n, op, cl+1)

    def generateParenthesis(self, n: int) -> list[str]:
        self.next_char('', n, 0, 0)
        return self.combinations