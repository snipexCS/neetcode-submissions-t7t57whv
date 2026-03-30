class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size = []
        res = ""

        for s in strs:
            size.append(len(s))
        
        for sz in size:
            res+=str(sz)
            res+=','
        
        res +='#'

        for char in strs:
            res+=char
        return res



        



            

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size = []
        res = []
        i = 0

        while s[i] != '#':
            cur = ''
            while s[i] != ',':
                cur += s[i]
                i+=1
            size.append(int(cur))
            i+=1
        i+=1

        for sz in size:
            res.append(s[i:i + sz])
            i+=sz
        return res
            
               






        
