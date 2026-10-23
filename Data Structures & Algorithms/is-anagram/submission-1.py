class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_table = {}

        for i in range(len(s)):
            if s[i] not in count_table.keys():
                count_table[s[i]] = 1
            else:
                count_table[s[i]] += 1
            
            if  t[i] not in count_table.keys():
                count_table[t[i]] = -1
            else:
                count_table[t[i]] -= 1

        if len(set(count_table.values())) > 1:
            return False
        return True