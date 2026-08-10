import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def quickSelect(l, r):
            pivotIndex = random.randint(l, r)
            numFreq[pivotIndex], numFreq[r] = numFreq[r], numFreq[pivotIndex]

            pivot = numFreq[r][0]
            i = l
            for j in range(l, r):
                if numFreq[j][0] < pivot:
                    numFreq[i], numFreq[j] = numFreq[j], numFreq[i]
                    i += 1
            numFreq[r], numFreq[i] = numFreq[i], numFreq[r]

            if i < k:
                return quickSelect(i + 1, r)
            elif i > k:
                return quickSelect(l, i - 1)
            else:
                return numFreq[i:]
        
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        numFreq = [(cnt, num) for num, cnt in freq.items()]
        k = len(numFreq) - k
        topK = quickSelect(0, len(numFreq) - 1)
        return [num for cnt, num in topK]