# Last updated: 12/24/2025, 11:47:12 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def __init__(self):
9        self.max = 0
10
11    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
12        height = self.traverse(root)
13
14        return max(self.max, height - 1)
15
16    def traverse(self, n):
17        print('n: ' + str(n.val))
18        if n.left == None and n.right == None:
19            return 1
20        else:
21            l = 0
22            r = 0
23
24            if n.left != None:
25                l = self.traverse(n.left)
26            if n.right != None:
27                r = self.traverse(n.right)
28
29            if self.max < (l + r):
30                self.max = l + r
31            
32            return max(l,r) + 1