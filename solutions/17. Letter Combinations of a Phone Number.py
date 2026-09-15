from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lib = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = deque(lib[digits[0]])
        curr_num = len(lib[digits[0]])
        for digit in digits[1:]:
            for num in range(curr_num):
                curr_res = result.popleft()
                for res in lib[digit]:
                    result.append(curr_res+res)
            curr_num *= len(lib[digit])
        return list(result)

                
print(Solution().letterCombinations("23"))