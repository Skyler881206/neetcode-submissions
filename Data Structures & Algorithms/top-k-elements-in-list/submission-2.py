class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in nums:
            count_value = hash_table.get(i, 0) + 1
            hash_table[i] = count_value

        frequency_hash_table = {}
        for i in hash_table.keys():
            if frequency_hash_table.get(hash_table[i], 0) == 0:
                frequency_hash_table[hash_table[i]] = [i]
            else:
                frequency_hash_table[hash_table[i]].append(i)
        
        sorting_result = []
        for i in sorted(frequency_hash_table.keys(), reverse=True):
            sorting_result += frequency_hash_table[i]
        return [int(x) for x in sorting_result[:k]]