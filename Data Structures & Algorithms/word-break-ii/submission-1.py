class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word = set(wordDict)
        def backtrack(index):
            if index == len(s):
                res.append(" ".join(cur))
                return
            for j in range(index,len(s)):
                w = s[index:j + 1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()

        cur = []
        res = []
        backtrack(0)
        return res
        