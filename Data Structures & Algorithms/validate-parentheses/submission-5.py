class Solution:
    def isValid(self, s: str) -> bool:
        diction = {
    ")": "(",
    "]": "[",
    "}": "{"
}
        stack = []

        

        for char in s:
            if char not in diction:
                stack.append(char)
            else:
                if not stack or stack[-1] != diction[char]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0

        