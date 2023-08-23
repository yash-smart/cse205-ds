class Solution:
    def __init__(self):
        self.original_list = []
        self.permutations = []
    def calculate_permutations(self, processed, to_be_processed):
        if len(to_be_processed) <= 1:
            new_permutation = []
            new_permutation.extend(processed)
            new_permutation.extend(to_be_processed)
            self.permutations.append(new_permutation)
        else:
            for i in range(len(to_be_processed)):
                current_element = to_be_processed[i]
                to_be_processed2 = to_be_processed.copy()
                to_be_processed2.remove(current_element)
                new_permutation = []
                new_permutation.extend(processed)
                new_permutation.append(current_element)
                self.calculate_permutations(new_permutation, to_be_processed2)
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.original_list = nums
        self.calculate_permutations([], nums)
        return self.permutations