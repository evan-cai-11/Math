from typing import List

class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end_of_word = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]

        return cur.is_end_of_word

class Solution:
    def __init__(self):
        self.wordDict = None

    def rWordBreak(self, s: str) -> List[str]:
        result = []

        for i in range(len(s)):
            cur = s[:i+1]
            if cur in self.wordDict:
                if i == len(s) - 1:
                    result.append(cur)
                else: 
                    ret = self.rWordBreak(s[i+1:])
                    if len(ret) > 0:
                        result.extend(list(map(lambda x: f"{cur} {x}", ret)))

        return result

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        self.wordDict = set(wordDict)

        return self.rWordBreak(s)
    

sol = Solution()

s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
print(sol.wordBreak(s1, wordDict1))
        