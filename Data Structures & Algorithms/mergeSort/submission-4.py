# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(s, m, e):
            left = pairs[s:m+1]
            right = pairs[m+1:e+1]
            i = s
            j = 0
            k = 0
            while j < (len(left)) and k < len(right):
                if left[j].key <= right[k].key:
                    pairs[i] = left[j]
                    j += 1
                else:
                    pairs[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                pairs[i] = left[j]
                i += 1
                j += 1
            while k < len(right):
                pairs[i] = right[k]
                i += 1
                k += 1

        def divide(s, e):
            if s >= e:
                return
            m = (s + e) // 2
            divide(s, m)
            divide(m + 1, e)

            merge(s, m, e)
        
        divide(0, len(pairs) - 1)
        return pairs