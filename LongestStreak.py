class Solution:
    def longestConsecutive(self, nums):
        streak = 0
        unique_num = set(nums)

        for num in unique_num:
            if num - 1 not in unique_num:
                current_num = num
                current_streak = 1

                while current_num + 1 in unique_num:
                    current_num += 1
                    current_streak += 1

                streak = max(streak, current_streak)

        return streak