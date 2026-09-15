class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != ".":
                    if curr not in row[i]:
                        row[i].append(curr)
                    else:
                        return False
                    if curr not in column[j]:
                        column[j].append(curr)
                    else:
                        return False
                    curr_box = i // 3 + 3 * (j // 3)
                    if curr not in box[curr_box]:
                        box[curr_box].append(curr)
                    else:
                        return False
        return True