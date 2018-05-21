"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self,other):#operator < 
        return self.val < other.val

def print_node(head):
    while head:
        print(head.val,end=' ')
        head = head.next
    print()

def init_list(l):
    if l:
        l = sorted(l)
        curr = head = ListNode(l[0])
        for i in l[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head
    return None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            length = len(lists)
            if length == 2:
                return self.mergeTowLists(lists[0],lists[1])
            else:
                left = self.mergeKLists(lists[:length//2])
                right = self.mergeKLists(lists[length//2:])
            return self.mergeTowLists(left,right)

    def mergeTowLists(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1,list2 = list2,list1
        head = list1
        while list1 and list2:
            tail = None
            while list1 and list1.val <= list2.val:
                tail = list1
                list1 = list1.next
            if tail:
                tail.next = list2
            list1,list2 = list2,list1
        return head


# class Solution(object):
    

    def mergeKLists_v1(self,lists):
        print(123)
        from queue import PriorityQueue
        q = PriorityQueue()
        dummy = cur =  ListNode(0)
        for head in lists:
            if head:
                q.put((head.val,head))
        while not q.empty():
            val,node = q.get()
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val,node))


        return dummy.next


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            length = len(lists)
            left = self.mergeKLists(lists[:length//2])
            right = self.mergeKLists(lists[length//2:])
            return self.mergeTwoLists(left,right)

    def mergeTwoLists(self, l1, l2):
        curr = dummy = ListNode(0)
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
    s = Solution()
    lll = list()
    for i in range(2):
        l1 = init_list([12,4,3,3,4,5,5,6,7,8,9,11111])
        l2 = init_list([12,4,1,22,2,2,2,2,4,160,7,8,9])
        l3 = init_list([9,9,9,55,55,55,222,2,2,2,4,160,7,8,9])
        lll.extend([l1,l2,l3])
    # print(lll)
    # print(1111)
    # r = s.mergeKLists(lll)
    r = s.mergeKLists_v1(lll)

    # r = s.mergeTowLists(l1,l2)

    print_node(r)
    