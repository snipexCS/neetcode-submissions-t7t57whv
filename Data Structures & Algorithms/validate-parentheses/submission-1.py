class Solution:
    def isValid(self, s: str) -> bool:
        diction = {
    ")": "(",
    "]": "[",
    "}": "{"
}
        stack = []

        

        for char in s:
            if char not  in diction:
                stack.append(char)
            else:
                if not stack or diction[char] != stack[-1]:
                    return False
                stack.pop()
            
            
        
        return len(stack) == 0


        