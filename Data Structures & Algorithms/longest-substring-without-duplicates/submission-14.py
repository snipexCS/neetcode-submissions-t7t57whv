class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        counter = {}
        left = 0
        for right in range(len(s)):
            if s[right] in counter:
                left = max(counter[s[right]] + 1 , left)
            counter[s[right]] = right
            longest = max(longest,right-left+1)
        return longest


            
        