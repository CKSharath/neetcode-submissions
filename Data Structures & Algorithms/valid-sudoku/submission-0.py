class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row():
            for i in range(9):
                seen=set()
                for j in range(9):
                    if board[i][j]=='.':
                        continue
                    elif board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        def col():
            for j in range(9):
                seen=set()
                for i in range(9):
                    if board[i][j]=='.':
                        continue
                    elif board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        def squ():
            for i in range(0,9,3):
                for j in range(0,9,3):
                    seen=set()
                    for r in range(i,i+3):
                        for c in range(j,j+3):
                            if board[r][c]=='.':
                                continue
                            elif board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
            return True
        return row() and col() and squ()
