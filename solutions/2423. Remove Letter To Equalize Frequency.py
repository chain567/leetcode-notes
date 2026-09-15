class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        lib = {}
        keys = []
        result = False
        for char in word:
            if char not in lib:
                lib[char] = 1
                keys.append(char)
            else:
                lib[char] += 1

        # only 1 char
        if len(keys) == 1:
            return True
        # all keys appear 1
        elif len(keys) == len(word):
            return True
        else:
            words = list(lib.values())
            max_num = max(words)
            min_num = min(words)

            if min_num == 1 and words.count(1) == 1 and words.count(max_num) == len(keys)-1:
                return True
            elif max_num - min_num == 1 and words.count(max_num) == 1 and words.count(min_num) == len(keys) - 1:
                return True
            else:
                return False