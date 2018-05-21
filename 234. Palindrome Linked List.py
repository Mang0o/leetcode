"""Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            if head:
                cur = head.next
                head.next = None
                while(cur):
                    tmp = cur
                    cur = cur.next
                    tmp.next = head
                    head = tmp
            return head
        
        s = head
        f = head
        while(f and f.next):
            s = s.next
            f = f.next.next
        leftEnd = s
        if(f): #奇数个，让右边小，遍历比较的时候以小的为标准
            s = s.next
        s = reverse(s)
        rightHead = s
        f = head
        while(s):
            if s.val != f.val:
                if leftEnd:
                    reverse(rightHead)
                return False
            s = s.next
            f = f.next
        reverse(rightHead)
        return True

def print_node(head):
    print(head.val)
    if head.next:
        print_node(head.next) 

if __name__ == '__main__':
    
    head = ListNode(0)
    cur = head
    for i in range(2,10,2):
        cur.next = ListNode(i)
        cur = cur.next
    print_node(head)
    s = Solution()
    print(s.isPalindrome(head))
            
        
        
