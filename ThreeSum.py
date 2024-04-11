class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)
        Threesum = []

        for i, num in enumerate(nums):            
            if num > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, Threesum)
        
        return Threesum
            
    def twoSum(self, numbers: List[int], idx, res) -> List[int]:
        
        l,r = idx+1, len(numbers) - 1
        
        while (l < r):
            sum = numbers[l] + numbers[r] + numbers[idx]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                res.append([numbers[idx], numbers[l], numbers[r]])
                l += 1
                r -= 1
                while l < r and numbers[l] == numbers[l - 1]:
                    l += 1
