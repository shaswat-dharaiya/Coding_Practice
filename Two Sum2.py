class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = { num:i for i, num in enumerate(numbers) }
        for i, num in enumerate(numbers):
            other_num = target - num
            
            if other_num in hash and hash[other_num] != i:
                return [i+1,hash[other_num]+1]