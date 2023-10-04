class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1 :
            flag = False
            flag2 = False
            for j in nums2 :
                if (flag == False) :
                    if (i == j) :
                        flag = True
                else :
                    if (j>i) :
                        result.append(j)
                        flag2 = True
                        break
            if (flag2 == False) :
                result.append(-1)
        return result