"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
def print_node(head):
    print(head.val)
    if head.next:
        print_node(head.next) 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        tmp = head
        while(tmp):
            nums.append(tmp.val)
            tmp = tmp.next
        print(nums)
        def bst(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = bst(nums[0:mid])
            node.right = bst(nums[mid+1:])
            return node
        return bst(nums)
        

if __name__ == '__main__':
    head = ListNode(-10)
    cur = head
    for i in [-3,0,5,9]:
        cur.next = ListNode(i)
        cur = cur.next

    print_node(head)

    s = Solution()
    s.sortedListToBST(head)

        