class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_char_legnth = 0 # Init char length
        left = 0
        right = 0
        char_count = {}
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1 # Update char_count, add the right char
            max_freq = max(char_count.values()) # Get the max frequecy char
            
            window_size = right - left + 1
            while window_size - max_freq > k: # If replacement char >= k
                char_count[s[left]] -= 1 # Update the char count, remove the left char
                left += 1 # invalid, shrink the window
                window_size = right - left + 1 # Update window size when shrink window
                
            max_char_legnth = max(max_char_legnth, window_size) # valid, check the freq

        return max_char_legnth