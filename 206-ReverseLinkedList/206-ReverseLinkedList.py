# Last updated: 12/23/2025, 4:11:23 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head is None:
9            return head
10        
11        curr = head.next
12        prev = head
13
14        while curr is not None:
15            nextFlag = curr.next
16
17            curr.next = head
18            prev.next = nextFlag
19
20            head = curr
21            curr = nextFlag
22
23        return head