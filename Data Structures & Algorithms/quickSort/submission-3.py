# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(l, r):
            if l >= r:
                return
            
            pivot = pairs[r].key
            i = l

            for j in range(l, r):
                if pairs[j].key < pivot:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i += 1
            pairs[i], pairs[r] = pairs[r], pairs[i]

            sort(l, i - 1)
            sort(i + 1, r)
        
        sort(0, len(pairs) - 1)
        return pairs