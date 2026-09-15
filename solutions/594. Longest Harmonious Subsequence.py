class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lib = {}
        count = []
        longest = 0
        for num in nums:
            if num not in lib:
                lib[num] = 1
                count.append(num)
            else:
                lib[num] += 1
        count.sort()
        for i in range(1, len(count)):
            if count[i] - count[i-1] == 1:
                longest = max(longest, lib[count[i]]+lib[count[i-1]])      
        return longest