class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations :
            if (i == '+') :
                if (len(scores)>=2) :
                    score1 = scores[-1]
                    score2 = scores[-2]
                    scores.append(score1+score2)
            elif (i == 'D') :
                if (scores) :
                    score1 = scores[-1]
                    scores.append(score1*2)
            elif (i == 'C') :
                if (scores) :
                    scores.pop()
            else :
                scores.append(int(i))
        return sum(scores)