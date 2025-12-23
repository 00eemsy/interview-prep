# Last updated: 12/23/2025, 3:57:03 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        mapDict = {}
4        returnArr = []
5        
6        for s in strs:
7            tempCountingArr = [0] * 26
8
9            for char in s:
10                index = ord(char) - ord('a')
11
12                tempCountingArr[index] += 1
13
14            if tuple(tempCountingArr) in mapDict.keys():
15                returnArr[mapDict[tuple(tempCountingArr)]].append(s)
16            else:
17                mapDict[tuple(tempCountingArr)] = len(returnArr)
18                returnArr.append([s])
19
20        return returnArr