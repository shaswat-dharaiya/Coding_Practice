class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # elif x > 0 and x < 10:
        #     return True
        
        dummy_x = x
        reverse_x = 0
        while(dummy_x > reverse_x):
            reverse_x = reverse_x * 10 + dummy_x % 10
            dummy_x = int(dummy_x / 10)
        

        return reverse_x == dummy_x or dummy_x == int(reverse_x / 10)