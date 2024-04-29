class Solution:
    def trap(self, height: List[int]) -> int:

        # Tetris approach
        # 1. Remove leading & trailing 0s in the array, and count the no of 0s in between
        # 2. iterate through array such that if height[i] = 0 if height[i] == 0 else height[i] - 1
        # 3. Repeat this process max(height) times
        # TC = O(n*max(height)) ie. worstcase max(height) > n thus TC = (n**2)
        # A small enhancement can be made if the starting array has no 0s in it then we can
        # first perform steps 2 & 3. 
        '''
        max_h = max(height)

        amt = 0

        while(height.count(0) == 0):
            for i,h in enumerate(height):
                height[i] = 0 if h == 0 else h - 1

        for idx in range(max_h):
            l,r = 0, len(height) - 1
            while(height[l] == 0 and l<r):
                l += 1
            while(height[r] == 0 and l<r):
                r -= 1
            
            amt += len([ 0 for x in range(l,r) if height[x] == 0])

            for i,h in enumerate(height):
                height[i] = 0 if h == 0 else h - 1
            height =  height[l:r+1]

        return amt
        '''

        # Approach: DP

        n = len(height)
        left = [height[0]]
        right = [0]*n

        right[n-1] = height[n-1]

        max_vol = 0

        for i in range(1,n):
            left.append(max(left[i-1],height[i]))

        for i in reversed(range(n-1)):
            right[i] = max(right[i+1],height[i])

        for i in range(n):
            max_vol += min(left[i],right[i]) - height[i]

        return max_vol
            
                    
                        

