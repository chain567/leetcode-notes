class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        new = sorted(count, key=count.get, reverse=True) # O(nlog(n))
        return new[:k]