class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            temp_value = hash_s.get(s[i], 0) + 1
            hash_s[s[i]] = temp_value

            temp_value = hash_t.get(t[i], 0) + 1
            hash_t[t[i]] = temp_value

        for key in hash_s.keys():
            if hash_s.get(key, 0) != hash_t.get(key, 0):
                return False
        return True