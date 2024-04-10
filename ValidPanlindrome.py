class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([letter.lower() for letter in s if letter.isalnum() ])
        
        return new_s[:int(len(new_s)/2)] == new_s[int(len(new_s)/2)+len(new_s) % 2 : ][::-1]
        
