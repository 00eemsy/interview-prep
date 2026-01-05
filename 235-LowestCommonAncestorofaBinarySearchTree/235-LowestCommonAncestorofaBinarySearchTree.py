# Last updated: 1/5/2026, 3:56:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        next = None
11
12        if root.val < p.val and root.val < q.val:
13            next = root.right
14        elif root.val > p.val and root.val > q.val:
15            next = root.left
16        else:
17            return root
18
19        return self.lowestCommonAncestor(next, p, q)