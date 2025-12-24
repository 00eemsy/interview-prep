# Last updated: 12/23/2025, 4:12:53 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        curr = head
10        s = set()
11
12        while curr is not None:
13            length = len(s)
14            s.add(curr)
15            if len(s) == length:
16                return True
17
18            curr = curr.next
19
20        return False