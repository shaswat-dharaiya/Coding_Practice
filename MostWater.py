class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force
        # max_amt = -1
        # for i, x in enumerate(height):
        #     for j, y in enumerate(height):
        #         if i != j:
        #             amt = min(x,y) * abs((j-i))
        #             max_amt = max(max_amt, amt)
        
        # return max_amt

        max_amt = -1
        l, r = 0, len(height) - 1
        while (l<r):
            width = r-l
            amt = min(height[l], height[r]) * width
            max_amt = max(max_amt, amt)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_amt