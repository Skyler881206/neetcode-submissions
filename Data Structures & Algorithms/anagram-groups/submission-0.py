class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {} # Init result
        for words in strs:
            hash_array = {} # Init Contain array
            for word in words:
                word_count = hash_array.get(word, 0) + 1
                hash_array[word] = word_count

            key = tuple(sorted(hash_array.items()))

            if key not in result:
                result[key] = [words]
                continue
            result[key].append(words)

        return list(result.values())