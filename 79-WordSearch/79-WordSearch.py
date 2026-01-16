# Last updated: 1/16/2026, 11:12:22 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        def helper(curr, i, j, visited):
4            # print('curr: ' + str(curr))
5            if curr == word:
6                # print('tis the word!')
7                return True
8            elif len(curr) >= len(word) or curr[-1] != word[len(curr)-1]:
9                # print('getting stuck hereee')
10                return False
11            else:
12                flag = False
13
14                if i-1 >= 0 and (i-1, j) not in visited.keys():
15                    visited[(i-1, j)] = True
16                    flag = flag or helper(curr + board[i-1][j], i-1, j, visited)
17                    del visited[(i-1, j)]
18                if i+1 < len(board) and (i+1, j) not in visited.keys():
19                    visited[(i+1, j)] = True
20                    flag = flag or helper(curr + board[i+1][j], i+1, j, visited)
21                    del visited[(i+1, j)]
22                if j-1 >= 0 and (i, j-1) not in visited.keys():
23                    visited[(i, j-1)] = True
24                    flag = flag or helper(curr + board[i][j-1], i, j-1, visited)
25                    del visited[(i, j-1)]
26                if j+1 < len(board[i]) and (i, j+1) not in visited.keys():
27                    visited[(i, j+1)] = True
28                    flag = flag or helper(curr + board[i][j+1], i, j+1, visited)
29                    del visited[(i, j+1)]
30                return flag
31        
32        
33        
34        for i in range(len(board)):
35            for j in range(len(board[i])):
36                if board[i][j] == word[0]:
37                    found = helper(word[0], i , j, {(i, j): True})
38
39                    if found:
40                        return True
41
42        return False