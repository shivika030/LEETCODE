class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[{} for _ in range(9)]
        col=[{}for _ in range(9)]
        boxes={}

        for i in range (9):
            for j in range(9):
                num= board[i][j]

                if num == ".":
                    continue

                box=(i//3,j//3)

                if num in rows[i]:
                    return False

                if num in col[j]:
                    return False

                if box not in boxes:
                    boxes[box]={}

                if num in boxes[box]:
                    return False

                rows[i][num]=1
                col[j][num]=1
                boxes[box][num]=1  

        return True              
