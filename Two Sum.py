class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            difference = target - num
            try:
                if map[difference] != i:
                    return [i,map[difference]]
            except Exception as e:
                print("trying another number")