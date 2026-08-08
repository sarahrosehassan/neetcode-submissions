from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set up three groups of bags: one per row, one per column, one per 3x3 box
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # walk very cell (r,c) on the board

        for r in range (len(board[0])):
            for c in range (len(board[0])):
                value = board[r][c]
                # skip blanks
                if value == '.':
                    continue

                box_id = (r // 3, c // 3)# find which 3x3 box this cell is in
                # if value is is already in its row's, column's or box's bag return False

                if value in rows[r] or value in cols[c] or value in boxes[box_id]:
                    return False
                # else no dupicate and add to designated set

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_id].add(value)

        # board is valid if there are no duplicates
        return True
        