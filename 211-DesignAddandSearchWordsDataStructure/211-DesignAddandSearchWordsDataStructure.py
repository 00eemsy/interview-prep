# Last updated: 1/25/2026, 1:23:31 PM
1class WordDictionary:
2
3    def __init__(self):
4        self.d = {}
5
6    def addWord(self, word: str) -> None:
7        i = 0
8        curr = self.d
9        
10        while i < len(word):
11            if word[i] not in curr.keys():
12                curr[word[i]] = {}
13            
14            curr = curr[word[i]]
15            i += 1
16
17        curr[None] = True
18
19    def search(self, word: str) -> bool:
20        print('word being searched: ' + str(word))
21        return self.search_helper(word, 0, self.d)
22    
23    def search_helper(self, word, i, curr):
24        while i < len(word):
25            if word[i] == '.':
26                ret = False
27                for key in curr.keys():
28                    if key != None:
29                        ret = ret or self.search_helper(word, i+1, curr[key])
30                    if ret == True:
31                        return True
32                
33                return ret
34            elif word[i] not in curr.keys():
35                return False
36            else:
37                curr = curr[word[i]]
38                i += 1
39
40        print('curr rn: ' + str(curr))
41        if None in curr.keys():
42            return True
43        else:
44            return False
45
46
47# Your WordDictionary object will be instantiated and called as such:
48# obj = WordDictionary()
49# obj.addWord(word)
50# param_2 = obj.search(word)