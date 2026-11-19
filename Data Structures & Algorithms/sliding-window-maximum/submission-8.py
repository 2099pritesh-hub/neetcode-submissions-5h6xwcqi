class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        output.append(-heap[0][0])

        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            while heap[0][1] < l:
                heapq.heappop(heap)
            output.append(-heap[0][0])
        return output