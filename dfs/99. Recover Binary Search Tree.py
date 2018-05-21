"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def get_max(node1,node2):
            return (node1 if node1.val > node2.val else node2) if node1 and node2 else node1 or node2

        def get_min(node1,node2):
            return (node1 if node1.val < node2.val else node2) if node1 and node2 else node1 or node2
        
        self.smallNode = None
        self.bigNode = None
        def dfs(root):
            if root:
                minLeft,maxLeft = dfs(root.left)
                if maxLeft:
                    if maxLeft.val > root.val:
                        self.smallNode = root if (not self.smallNode) or self.smallNode.val > root.val else self.smallNode
                        self.bigNode = maxLeft if (not self.bigNode) or self.bigNode.val < maxLeft.val else self.bigNode

                        # if not self.smallNode:
                        #     self.smallNode = root
                        # else:
                        #     if self.smallNode.val > root.val:
                        #         self.smallNode = root
                        
                        # if not self.bigNode:
                        #     self.bigNode = maxLeft
                        # else:
                        #     if self.bigNode.val < maxLeft.val:
                        #         self.bigNode = maxLeft
                   
                minRight,maxRight = dfs(root.right)
                if minRight:
                    if root.val > minRight.val:
                        self.smallNode = minRight if (not self.smallNode) or self.smallNode.val > minRight.val else self.smallNode
                        self.bigNode = root if (not self.bigNode) or self.bigNode.val < root.val else self.bigNode
                        
                        # if not self.smallNode:
                        #     self.smallNode = minRight
                        # else:
                        #     if self.smallNode.val > minRight.val:
                        #         self.smallNode = minRight
                        
                        # if not self.bigNode:
                        #     self.bigNode = root
                        # else:
                        #     if self.bigNode.val < root.val:
                        #         self.bigNode = root
                return get_min(get_min(minLeft,minRight),root),get_max(get_max(maxLeft,maxRight),root)
            return None,None

        dfs(root)
        if self.smallNode and self.bigNode:
            self.smallNode.val,self.bigNode.val = self.bigNode.val,self.smallNode.val
        return


if __name__ == '__main__':
  





