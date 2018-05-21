# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #递归
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = [0,False]
        self.helper(head,num,n,head)
        if num[0] == n:
            if n == 1:
                return None
            else:
                return head.next
        return head

    def helper(self,node,num,n,head):
        if node:
            self.helper(node.next,num,n,head)
        else:
            num[0] = 0
            return
        num[0] += 1
        if num[0] == n:
            num[1] = True
            return
        if num[1]:
            if node.next:
                node.next = node.next.next
            num[1] = False
    #非递归
    def removeNthFromEnd(self,head,n):
        left = right = head
        while (right and n>0):
            right = right.next
            n-=1
        if not right:
            return head.next if n==0 else None

        while(right.next):
            left = left.next
            right = right.next

        left.next = left.next.next
        return head

def print_node(head):
    print(head.val)
    if head.next:
        print_node(head.next)   

if __name__ == '__main__':
    head = ListNode(0)
    cur = head
    for i in range(1,2):
        cur.next = ListNode(i)
        cur = cur.next
    print_node(head)
    print('---------------')
    ret = Solution().removeNthFromEnd(head,5)
    if ret:
        print_node(ret)
    else:
        print(ret)
    print('---------------')
    print_node(head)

