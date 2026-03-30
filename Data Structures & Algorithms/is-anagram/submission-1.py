class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1 
        
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                counter[char] +=1
        
        for char in counter:
            if counter[char] != 0:
                return False
        
        return True
        