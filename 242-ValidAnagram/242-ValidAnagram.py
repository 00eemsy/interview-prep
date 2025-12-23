# Last updated: 12/23/2025, 3:56:07 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s_dict = {}
4        t_dict = {}
5
6        if len(s) != len(t):
7            return False
8
9        for i in range(0, len(s)):
10            # s
11            s_char = s[i]
12            t_char = t[i]
13
14            if s_char in s_dict.keys():
15                s_dict[s_char] += 1
16            else:
17                s_dict[s_char] = 1
18
19            if t_char in t_dict.keys():
20                t_dict[t_char] += 1
21            else:
22                t_dict[t_char] = 1
23
24        # for char in s:
25        #     if char in s_dict.keys():
26        #         s_dict[char] += 1
27        #     else:
28        #         s_dict[char] = 1
29
30        # for char in t:
31        #     if char in t_dict.keys():
32        #         t_dict[char] += 1
33        #     else:
34        #         t_dict[char] = 1
35
36        if s_dict == t_dict:
37            return True
38        else:
39            return False