class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1 # change min_heap to max_heap
        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            if max1 != max2:
                heapq.heappush(stones, max1-max2)
        return -heapq.heappop(stones) if stones else 0 # return the negation of the final value