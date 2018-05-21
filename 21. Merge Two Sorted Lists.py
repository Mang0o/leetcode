# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_node(head):
    print(head.val)
    if head.next:
        print_node(head.next) 

class Solution:
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        if l1:
            if l2:
                if l1.val <= l2.val:
                    head = l1 
                    l1 = l1.next
                else:
                    head = l2
                    l2 = l2.next
            else:
                return l1
        else:
            return l2

        cur = head
        while(l1 and l2):
            if l1.val <= l2.val:
                cur.next = l1 
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return head

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        curr
        while l1 or l2:
            node = [l2,l1][l1.val<=l2.val] if l1 and l2 else l1 or l2
            curr.next = node
            curr = curr.next
            if node==l1:
                l1 = l1.next
            else:
                l2 = l2.next
        return dummy.next
           

        


if __name__ == '__main__':
    head = ListNode(0)
    head2 = ListNode(1)
    cur = head
    for i in range(2,10,2):
        cur.next = ListNode(i)
        cur = cur.next
    cur = head2
    for i in range(3,10,2):
        cur.next = ListNode(i)
        cur = cur.next

    print_node(head)
    print('===================')
    print_node(head2)
    print('===================')
    s = Solution()
    print_node(s.mergeTwoLists(head,head2))