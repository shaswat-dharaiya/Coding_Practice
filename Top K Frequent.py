class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
           
        # Approach 1: Bucket Sort
        hash = { num: 0 for num in set(nums)}
        for num in nums:
            hash[num] += 1
        freq_hash = {count: [] for count in set(hash.values())}
        
        for num,count in hash.items():
            freq_hash[count].append(num)

        freq_count = list(reversed(freq_hash.keys()))[:k]
        k_freq = freq_hash[freq_count[0]]

        for count in freq_count[1:]:
            if len(k_freq) < k: 
                k_freq += freq_hash[count]

        return k_freq