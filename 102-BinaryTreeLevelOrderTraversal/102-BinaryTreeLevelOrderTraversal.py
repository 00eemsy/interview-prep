# Last updated: 1/6/2026, 1:08:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        d = {}
10        q = []
11
12        if root:
13            q.insert(0, [root, 0])
14
15        while len(q) > 0:
16            n = q.pop()
17
18            # add to dict
19            if n[1] not in d.keys():
20                d[n[1]] = [n[0].val]
21            else:
22                d[n[1]].append(n[0].val) #FIXME??
23            
24            if n[0].left:
25                q.insert(0, [n[0].left, n[1] + 1])
26            if n[0].right:
27                q.insert(0, [n[0].right, n[1] + 1])
28
29        ret = []
30
31        for key in d.keys():
32            ret.append(d[key])
33
34        return ret