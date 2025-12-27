# Last updated: 12/27/2025, 10:22:39 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        # check if one is None (but not both)
10        bothFlag = True
11        atLeastOneFlag = False
12
13        if p == None:
14            bothFlag = not bothFlag
15            atLeastOneFlag = True
16        if q == None:
17            bothFlag = not bothFlag
18            atLeastOneFlag = True
19        
20        if bothFlag == False: # one is None
21            return False
22        elif atLeastOneFlag == True:
23            return True
24        elif atLeastOneFlag == False and p.val != q.val:
25            return False # check if have vals, but don't match
26        else: # same curr vals
27            l = self.isSameTree(p.left, q.left)
28            r = self.isSameTree(p.right, q.right)
29
30            return l and r