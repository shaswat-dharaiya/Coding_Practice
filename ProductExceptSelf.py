class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # Approach 1 - Space - O(n)
        # nums_left = [1]*n
        # nums_right = [1]*n
        
        # product = [1]*n

        # for i, num in enumerate(nums):
        #     if i > 0:
        #         nums_left[i] = nums[i-1] * nums_left[i -1]
        #         nums_right[n-i-1] = nums[n-i] * nums_right[n-i]
        
        # return [ nums_left[i] * nums_right[i] for i in range(0,n)  ]

        # Approach 2 - Space - O(1)
        answer = [1] * n
        for i in range(n):
            if i > 0:
                answer[i] = nums[i-1] * answer[i-1]
        
        right = 1
        for i in range(n):
            answer[n-i-1] *= right
            right *= nums[n-i-1]
        
        return answer

