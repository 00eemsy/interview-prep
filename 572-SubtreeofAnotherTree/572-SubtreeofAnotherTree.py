# Last updated: 12/30/2025, 10:18:53 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def checkSubtree(self, root, subRoot):
9        print('\nroot: ' + str(root.val) + ', subRoot: ' + str(subRoot.val))
10        # check if both can go left
11        l = False
12        r = False
13
14        if root.left == None and subRoot.left == None:
15            l = True
16        elif root.left and subRoot.left:
17            l = self.checkSubtree(root.left, subRoot.left)
18        
19        # check right
20        if root.right == None and subRoot.right == None:
21            r = True
22        elif root.right and subRoot.right:
23            r = self.checkSubtree(root.right, subRoot.right)
24
25        print('l: ' + str(l) + ', r: ' + str(r))
26
27        return l and r and (root.val == subRoot.val)
28
29    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
30        print('\nroot: ' + str(root.val) + ', subRoot: ' + str(subRoot.val))
31        if root.val == subRoot.val:
32            subFlag = self.checkSubtree(root, subRoot)
33            if subFlag == True:
34                return True
35        
36        # check if both can go left
37        l = False
38        r = False
39
40        if root.left == None and subRoot.left == None:
41            pass
42        elif root.left:
43            l = self.isSubtree(root.left, subRoot)
44        
45        # check right
46        if root.right == None and subRoot.right == None:
47            pass
48        elif root.right:
49            r = self.isSubtree(root.right, subRoot)
50
51        print('l: ' + str(l) + ', r: ' + str(r))
52
53        return l or r