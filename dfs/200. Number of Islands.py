"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
     def numIslands(self, grid):
         """
         :type grid: List[List[str]]
         :rtype: int
         """
        def sink(i,j):
            if 0<=i<M and 0<=j<N:
                grid[i][j] = '0'
                map(sink,(i+1,i,i-1,i),(j,j+1,j,j-1))
            return True
        M = len(grid)
        N = len(grid[0])

        return sum(grid[i][j]=='1' and sink(i,j) for i in range(M) for j in range(N))

        