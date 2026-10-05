# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        tail=head
        cnt=1
        while tail.next:
            tail=tail.next
            cnt+=1
        
        nh=head
        k=k%cnt
        if k==0:
            return head
        tail.next=head
        for _ in range(cnt-k):
 
            tail=tail.next
        nh=tail.next
        tail.next=None
        return nh