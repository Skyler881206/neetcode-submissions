class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        longest_num = 0
        start = 0 # Sliding windows's init pos

        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] >= start:
                start = hash_map[s[i]] + 1 # Change start pos
            
            hash_map[s[i]] = i
            longest_num = max(longest_num, i - start + 1)

        return longest_num