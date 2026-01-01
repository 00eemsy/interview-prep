# Last updated: 1/1/2026, 11:35:19 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        # make s1 hash
4        h1 = {}
5
6        for char in s1:
7            if char in h1:
8                h1[char] += 1
9            else:
10                h1[char] = 1
11        
12        h = h1
13
14        # traverse
15        i = 0
16        j = 0
17        count = 0
18
19        while j < len(s2):
20            if s2[j] not in h.keys() or h[s2[j]] == 0:
21                if count > 0:
22                    if s2[i] in h.keys():
23                        h[s2[i]] += 1
24                        count -= 1
25                    else:
26                        count = 0
27                        h = h1
28                        j += 1
29                else:
30                    j += 1
31
32                i += 1
33            else:
34                h[s2[j]] -= 1
35                count += 1
36
37                if count == len(s1):
38                    return True
39
40                j += 1
41
42        return False