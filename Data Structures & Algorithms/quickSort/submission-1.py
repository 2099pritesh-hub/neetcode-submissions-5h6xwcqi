# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
        
    def quickSortHelper(self, arr, l, r):
        if l >= r:
            return arr
        
        pivot = arr[r].key
        i = l

        for j in range(l, r):
            if arr[j].key < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[i], arr[r] = arr[r], arr[i]

        self.quickSortHelper(arr, l, i - 1)
        self.quickSortHelper(arr, i + 1, r)

        return arr