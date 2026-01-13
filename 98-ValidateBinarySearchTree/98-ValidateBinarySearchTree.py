# Last updated: 1/13/2026, 2:51:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        return self.helper(root, [float(-inf), float(inf)])
10        
11    def helper(self, root, range):
12        bstFlag = True
13
14        l = True
15        r = True
16
17        if root.left:
18            if root.left.val >= root.val:
19                bstFlag = False
20            l = self.helper(root.left, [range[0], root.val])
21        if root.right:
22            if root.right.val <= root.val:
23                bstFlag = False
24            r = self.helper(root.right, [root.val, range[1]])
25        if range[0] >= root.val or range[1] <= root.val:
26            bstFlag = False
27
28        return l and r and bstFlag
29