"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = [0]
        if root:
            self.getMaxPathSum(root,ret)

        return ret[0]

    def getMaxPathSum(self,node,result):
        left = right = 0
        if node.left:
            left = self.getMaxPathSum(node.left,result)
        if node.right:
            right = selff.getMaxPathSum(node.right,result)

        result[0] = max(result[0], node.val+max(0,left)+max(0,right))

        return max([node.val,node.val+left,node.val+right])

