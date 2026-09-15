class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        lib = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        s = s.strip()
        if s == "":
            return 0
        neg = 1
        result = []
        check = [2, 1, 4, 7, 3, 6, 8]
        start = 0
        exist = False
        if not s[0].isdigit():
            if s[0] == '-':
                neg = -1
                start = 1
            elif s[0] == '+':
                neg = 1
                start = 1
            else:
                return 0
        for t in s[start:]:
            if t.isdigit():
                if t != "0":
                    exist = True
                    result.append(t)
                elif exist and t == "0":
                    result.append(t)

                print(result)
                if len(result) > 10:
                    if neg == 1:
                        return 2147483647
                    else:
                        return -2147483648
            else:
                break
        res = "".join(result)
        if len(res) == 10 and res > "2147483647":
            if neg == 1:
                return 2147483647
            else:
                return -2147483648
        else:
            if not res:
                return 0
            ans = 0
            for j in range(len(res)-1, -1, -1):
                ans += lib[res[j]] * 10 ** (len(res)-1-j)
            return ans * neg