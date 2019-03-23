class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        b = board[:]
        b.append([0]*len(b[0])) 
        b.insert(0,[0]*len(b[0]))
        b = [x + [0] for x in b]
        b = [[0] + x for x in b]
                
        for i in range(len(board)):
            for j in range(len(board[i])): 
                neighbors = [b[i][j], b[i][j+1], b[i][j+2], b[i+1][j], b[i+1][j+2],\
                b[i+2][j], b[i+2][j+1], b[i+2][j+2]]
                n_sum = sum(neighbors)
                
                if board[i][j] == 0:
                    if n_sum == 3:
                        board[i][j] = 1
                else:
                    if n_sum < 2 or n_sum > 3:
                        board[i][j] = 0
                