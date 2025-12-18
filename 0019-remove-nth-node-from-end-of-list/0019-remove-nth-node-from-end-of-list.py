# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if list is None: return list1
        ji =ki=head
        count=i=m=0
        hea=ji
        while ji:
            count+=1
            ji=ji.next
        # if m>count:return -1
        if count== n:return head.next
        n=count-n
        while ki:
            if m==n-1:
                ki.next=ki.next.next
                return hea
            else:
                m+=1
                ki=ki.next
        return hea