class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach 1 - Recursion
        # return build_group(strs)

        # Approach 2 - Sorting the letters in the words 

        list_anagram = {}

        for word in strs:
            word_sort = "".join(sorted(word))

            if word_sort in list_anagram: 
                list_anagram[word_sort].append(word)
            else:
                list_anagram[word_sort] = [word]
        
        return [ anagrams for anagrams in list_anagram.values()  ]





# Approach 1 - Recursion
# def build_group(strs: List[str]) -> List[List[str]]:
#     group_anagram = []
#     buffer = []
#     list_anagram = [strs[0]]
#     for i, word in enumerate(strs[1:]):
#         if isAnagram(word,strs[0]):
#             list_anagram.append(word)
#         else:
#             buffer.append(word)
#     if len(buffer) > 0:
#         group_anagram = build_group(buffer)    
#         group_anagram.append(list_anagram)
#     else:
#         group_anagram.append(list_anagram)
    
#     return group_anagram

# def isAnagram(s: str, t: str) -> bool:
#     set_of_s = set(s)
#     if len(s) != len(t):
#         return False
#     for i in set_of_s:
#         if s.count(i) != t.count(i):
#             return False
    
#     return True