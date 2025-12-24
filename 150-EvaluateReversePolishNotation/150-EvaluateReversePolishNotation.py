# Last updated: 12/23/2025, 4:07:03 PM
1class StackNode:
2    def __init__(self, val):
3        self.val = val
4        self.next = None
5
6class Stack:
7    def __init__(self, top = None):
8        self.top = top
9
10    def push(self, n):
11        n.next = self.top
12        self.top = n
13
14    def pop(self):
15        if self.top == None:
16            return None
17        else:
18            temp = self.top
19            self.top = self.top.next
20
21            temp.next = None
22            return temp.val
23    
24    def printStack(self):
25        curr = self.top
26
27        print('\ncurr stack')
28        while curr != None:
29            print(curr.val)
30            curr = curr.next
31
32class Solution:
33    def evalRPN(self, tokens: List[str]) -> int:
34        s = Stack()
35
36        for t in tokens:
37            if t in ['+', '-', '*', '/']:
38                n1 = int(s.pop())
39                n2 = int(s.pop())
40
41                if t == '+':
42                    s.push(StackNode(n1 + n2))
43                elif t == '-':
44                    s.push(StackNode(n2 - n1))
45                elif t == '*':
46                    s.push(StackNode(n1*n2))
47                else:
48                    s.push(StackNode(n2/n1))
49            else:
50                n = StackNode(int(t))
51                s.push(n)
52
53            # s.printStack()
54
55        retval = s.pop()
56        return int(retval)
57
58        