# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy = ListNode(0)
        # dummy.next = head
        # p1 = p2 = dummy
        # for i in range(n):
        #     p1 = p1.next
        # while p1.next:
        #     p1 = p1.next
        #     p2 = p2.next
        # p2.next = p2.next.next
        # return dummy.next

        ''' 先创建一个新的链表
        1.设置前后两个指针，right提前走n步
        2.这样的话，当right遍历到最后一个节点时，left的下一个节点就是需要删除的节点
        '''
        dum = ListNode(0)
        dum.next = head  # 注意此处是dum.next=head，而不是dum=head
        left = dum
        right = dum
        tap = n
        num = 0
        while (tap):
            right = right.next  # ！！！ 注意此处是right.next而不是head.next！！！
            tap -= 1
            num += 1
        print(num)
        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next  ###将left的下一个节点指向left的下下个节点

        return dum.next  # 返回值时候需要注意：是dum.next，而不是dum




