# Last updated: 12/23/2025, 4:14:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if root is None:
10            return 0
11        else:
12            left = self.maxDepth(root.left) + 1
13            right = self.maxDepth(root.right) + 1
14
15            return max(left, right)