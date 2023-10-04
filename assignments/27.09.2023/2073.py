class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        index = 0
        n = len(tickets)
        while True :
            if tickets[k] == 0 :
                return time
            if (tickets[index] != 0) :
                tickets[index] -= 1
                time += 1
            if (index == n-1) :
                index = 0
            else :
                index += 1