"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        height = [0]*len(matrix[0])
        ret = 0
        for i in range(0,len(matrix)):
            for j in range(len(matrix[i])):
                height[j] = 0 if matrix[i][j] == '0' else height[j]+int(matrix[i][j])
            ret = max(self.maxRecOfArray(height),ret)
        return ret
    
    
    def maxRecOfArray(self,heights):
        ret = 0
        stack = list()
        for i in range(len(heights)):
            if stack and heights[stack[-1]] >= heights[i]:
                while(stack and heights[stack[-1]] >= heights[i]):
                    index = stack.pop()
                    if heights[index] > heights[i]:
                        start = -1 if not stack else stack[-1]
                        ret = max(heights[index]*(i-start-1),ret)
            stack.append(i)
        while(stack):
            index = stack.pop()
            start = -1 if not stack else stack[-1]
            ret = max(heights[index]*(len(heights)-start-1),ret)
        return ret