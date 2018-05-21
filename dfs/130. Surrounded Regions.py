"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not(board and board[0]):
            return
        
        row = len(board)
        col = len(board[0])
        def sink(i,j):
            print(board)
            if 0<=i<row and 0<=j<col and board[i][j] == 'O':
                board[i][j] = '1'
                list(map(sink,(i+1,i,i-1,i),(j,j+1,j,j-1)))
        for i in range(row):
            sink(i,0)
            sink(i,col-1)
        for j in range(col):
            sink(0,j)
            sink(row-1,j)

        print(board)    
        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return
        
if __name__ == '__main__':
    s = Solution()
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    s.solve(board)
    print(board)     
                