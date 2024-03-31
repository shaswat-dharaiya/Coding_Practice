class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums_dict = {}
        for num in nums:
            
        # Approach 1
        #     try:
        #         nums_dict[num] += 1
        #         return True
        #     except Exception as e:
        #         nums_dict[num] = 1
        
        # return False

        # Approach 2
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                return True
        
        return False