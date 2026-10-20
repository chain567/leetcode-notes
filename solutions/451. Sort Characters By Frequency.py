class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) # or use a for-loop to count
        max_heap = [(-freq, ele) for ele, freq in count.items()]
        heapq.heapify(max_heap)
        ans = ''

        while max_heap:
            c, ele = heapq.heappop(max_heap)
            while c < 0: # since it is a min_heap, so the freq/c is added as negative values. min(c) is the max(freq)
                ans+= ele
                c += 1
        return ans