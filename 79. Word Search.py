"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0 or len(word)==0:
            return False

        pos_dict = {}#dict of set
        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                if letter in pos_dict:
                    pos_dict[letter].add((i,j))
                else:
                    pos_dict[letter] = set([(i,j)])
        if word[0] not in pos_dict:
            return False
        used_points = set([])
        result = [False]
        for pos in pos_dict[word[0]]:
            self.find_word_in_set(pos_dict,word[1:],result,pos,len(board),len(board[0]),used_points)
        return result[0]

    def find_word_in_set(self,pos_dict,word,result,cur_pos,m,n,used_points):
        if not result[0]:
            if len(word)==0:
                result[0] = True
                return
            if word[0] not in pos_dict:
                return
            used_points.add(cur_pos)
            neighbors = self.neighborhood(cur_pos[0],cur_pos[1],m,n)
            for pos in neighbors:
                if pos in pos_dict[word[0]] and pos not in used_points:
                    self.find_word_in_set(pos_dict,word[1:],result,pos,m,n,used_points)
            used_points.remove(cur_pos)

    def neighborhood(self,i,j,m,n):
        neighbors = []
        if i - 1 >=0:
            neighbors.append((i-1,j))
        if j - 1 >=0:
            neighbors.append((i,j-1))
        if i+1 < m:
            neighbors.append((i+1,j))
        if j+1 < n:
            neighbors.append((i,j+1))
        return neighbors

if __name__ == '__main__':
    s = Solution()

    board = \
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

    word = "ABCB"
    print(s.exist(board,word))

