class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_pos_dict = {}
        col_pos_dict = {}
        pos_dict = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                if v != '.':
                    if v in row_pos_dict:
                        if i in row_pos_dict[v]:
                            return False
                        else:
                            row_pos_dict[v].add(i)
                    else:
                        row_pos_dict[v] = set([i])

                    if v in col_pos_dict:
                        if j in col_pos_dict[v]:
                            return False
                        else:
                            col_pos_dict[v].add(j)
                    else:
                        col_pos_dict[v] = set([j])

                    if v in pos_dict:
                        for k in range(-2,0):
                            for l in range(-2,3):
                                if i//3==(i+k)//3 and j//3==(j+l)//3 and (i+k,j+l) in pos_dict[v]:
                                    return False
                        pos_dict[v].add((i,j))
                    else:
                        pos_dict[v] = set([(i,j)])

        return True


if __name__ == '__main__':
    s = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]


    board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
    ]

    # board = [
    # [".",".","5",".",".",".",".",".","6"],
    # [".",".",".",".","1","4",".",".","."],
    # [".",".",".",".",".",".",".",".","."],
    # [".",".",".",".",".","9","2",".","."],
    # ["5",".",".",".",".","2",".",".","."],
    # [".",".",".",".",".",".",".","3","."],
    # [".",".",".","5","4",".",".",".","."],
    # ["3",".",".",".",".",".","4","2","."],
    # [".",".",".","2","7",".","6",".","."]]
    print(s.isValidSudoku(board))