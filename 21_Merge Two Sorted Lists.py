# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        AC:
        1.先同时l1和l2公共长度的放到链表l3中（* l1 and l2 * 而不是 l1 or l2 或者 l1.next or l2.next）
        2.如果有l1或l2多余的长度，则把其剩余部分放到l3中
        * 3.NOTE:注意链表的输出--->首先创建一个链表dummy，将其头结点赋值给s，赋值之后一定要加上一句“ s = s.next ”!!!
                 否则只会一直在同一个节点上赋值。
        4. 注意最终返回值是返回dummy.next
        '''
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        s = dummy  # *
        while l1 and l2:
            if l1.val > l2.val:
                s.next = l2
                l2 = l2.next
            else:
                s.next = l1
                l1 = l1.next
            s = s.next  # *
        while l1:
            s.next = l1
            l1 = l1.next
            s = s.next  # *
        while l2:
            s.next = l2
            l2 = l2.next
            s = s.next  # *
        return dummy.next  # *


        # if l1==None and l2==None:
        #     return None
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # dummy = ListNode(0)
        # s = dummy
        # while l1 and l2:
        #     if l1.val > l2.val:
        #         s.next = l2
        #         l2 = l2.next
        #     else:
        #         s.next = l1
        #         l1 = l1.next
        #     s = s.next
        # if l1:
        #     while l1:
        #         s.next = l1
        #         l1 = l1.next
        #         s = s.next
        # if l2:
        #     while l2:
        #         s.next = l2
        #         l2 = l2.next
        #         s = s.next
        # return dummy.next



