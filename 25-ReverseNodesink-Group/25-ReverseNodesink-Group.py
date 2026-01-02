# Last updated: 1/1/2026, 5:37:06 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Stack:
7    def __init__(self):
8        self.stack = []
9        self.height = 0
10
11    def push(self, n):
12        self.stack.insert(0, n)
13        self.height += 1
14
15    def pop(self):
16        temp = self.stack[0]
17
18        self.stack.pop(0)
19        self.height -= 1
20
21        return temp
22
23class Solution:
24    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
25        if k == 1:
26            return head
27
28        s = Stack()
29        curr = head
30        prev = None
31        newHead = None
32
33        while curr != None:
34            print('curr: ' + str(curr.val) + ', s.height: ' + str(s.height))
35            if s.height < k-1:
36                s.push(curr)
37                curr = curr.next
38            else:
39                n1 = curr
40                temp = n1
41                curr = curr.next
42
43                while s.height > 0:
44                    n2 = s.pop()
45                    n1.next = n2
46                    n1 = n2
47
48                print('n1 at end of k: ' + str(n1.val) + ', prev: ' + str(prev))
49
50                # some sort of connection to next k group
51                n1.next = None
52                if prev == None:
53                    newHead = temp
54                else:
55                    prev.next = temp
56                prev = n1
57
58        if s.height > 0: # rm leftovers from stack
59            while s.height > 0:
60                n1 = s.pop()
61
62            if prev:
63                print('n1 at end of k: ' + str(n1.val) + ', prev: ' + str(prev))
64                prev.next = n1
65
66        return newHead