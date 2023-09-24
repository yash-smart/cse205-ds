class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = sum(accounts[0])
        for i in range(1,len(accounts)) :
            sum1 = sum(accounts[i])
            if (sum1 > max) :
                max = sum1
        return max