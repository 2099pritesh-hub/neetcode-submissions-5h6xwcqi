class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        minHeap = []
        for n, cnt in freq.items():
            heapq.heappush(minHeap, (cnt, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [cnt for _, cnt in minHeap]