class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        a, b = len(board), len(board[0])

        def dfs(i, j, n):
            if board[i][j] != word[n]:
                return False
            if n == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            if i > 0 and dfs(i - 1, j, n + 1):
                # board[i][j] = tmp
                return True
            if j < b - 1 and dfs(i, j + 1, n + 1):
                # board[i][j] = tmp
                return True
            if i < a - 1 and dfs(i + 1, j, n + 1):
                # board[i][j] = tmp
                return True
            if j > 0 and dfs(i, j - 1, n + 1):
                # board[i][j] = tmp
                return True
            board[i][j] = tmp
            return False
            

        for i in range(a):
            for j in range(b):
                if dfs(i, j, 0):
                    return True
        return False
        