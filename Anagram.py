class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Approach 1 - with Hash Table
        # s_dict, t_dict = {}, {}

        # for s_char in s:
        #     if s_char not in s_dict:
        #         s_dict[s_char] = 1
        #     else:
        #         s_dict[s_char] += 1
        
        # for t_char in t:
        #     if t_char not in t_dict:
        #         t_dict[t_char] = 1
        #     else:
        #         t_dict[t_char] += 1

        # for t_char, t_count in t_dict.items():
        #     if t_char not in s_dict or s_dict[t_char] != t_count:
        #         return False
        
        # for s_char, s_count in s_dict.items():
        #     if s_char not in t_dict or t_dict[s_char] != s_count:
        #         return False
        
        # return True

        # Approach 2 - With Set
        set_of_s = set(s)
        if len(s) != len(t):
            return False
        for i in set_of_s:
            if s.count(i) != t.count(i):
                return False
           
        return True