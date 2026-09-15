class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lib = {}
        max_num = "A"
        for num in nums:
            if num not in lib:
                lib[num] = 1
                if max_num == "A":
                    max_num = num
            else:
                lib[num] += 1
                if lib[max_num] < lib[num]:
                    max_num = num
        
        return max_num
        