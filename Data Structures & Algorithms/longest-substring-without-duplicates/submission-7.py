class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        longest = 0
        left = 0

        for right in range(len(s)):
            if s[right] in counter and counter[s[right]] >= left:
                left = counter[s[right]] + 1

            counter[s[right]] = right
            longest = max(longest,right - left + 1 )
        
        return longest



            
        