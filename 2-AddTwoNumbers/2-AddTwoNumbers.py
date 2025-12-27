# Last updated: 12/26/2025, 4:15:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        curr1 = l1
9        curr2 = l2
10
11        tens1 = 0
12        tens2 = 0
13
14        n1 = 0
15        n2 = 0
16
17        while curr1 != None or curr2 != None:
18            if curr1 != None:
19                n1 += curr1.val * (10**tens1)
20
21                tens1 += 1
22                curr1 = curr1.next
23            if curr2 != None:
24                n2 += curr2.val * (10**tens2)
25
26                tens2 += 1
27                curr2 = curr2.next
28
29        val = n1 + n2
30
31        # make into LL
32        # 1st one = root
33        n = val % 10
34
35        root = ListNode(n)
36        curr = root
37
38        val = (val - val%10)//10
39
40        while val > 0:
41            n = val % 10
42
43            curr.next = ListNode(n)
44            curr = curr.next
45
46            val = (val - val%10)//10
47
48        return root
49