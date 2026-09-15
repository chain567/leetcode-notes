class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                arr.append(s[i])
            else:
                if not arr:
                    return False
                else:
                    curr = arr.pop()
                    if curr == '(' and s[i] != ')':
                        return False
                    elif curr == '{' and s[i] != '}':
                        return False
                    elif curr == '[' and s[i] != ']':
                        return False
        return True and arr == []