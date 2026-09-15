class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        lib = {}
        def helper(number: int, i: int) -> int:
            if number == 0:
                return 1
            if i == n and number > 0:
                return 0
            if (i, number)in lib:
                return lib[(i, number)]

            if number >= coins[i]:
                res = helper(number-coins[i], i) + helper(number, i+1)
            else:
                res = helper(number, i+1)
            lib[(i, number)] = res
            return res

        return helper(amount, 0)