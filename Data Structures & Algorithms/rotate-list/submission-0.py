# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp=head
        c=1
        while temp.next:
            temp=temp.next
            c+=1
        k=k%c
        if k == 0:
            return head
        t=head
        for i in range(c-k-1):
            t=t.next
        nh=t.next
        t.next=None
        temp.next=head
        return nh
