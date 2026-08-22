class Solution:
    def isValid(self, s: str) -> bool:
        '''s1= len(s)//2
        i= len(s)//2
        while True:
            if s[s1] != s[i]:
                return False
            s1 -= 1
            i +=1 
        return True
''' 
        stack =[]
        hmap= { ")":"(","}":"{","]":"["}
        for c in s:
            if c in hmap:
                if stack and stack[-1] == hmap[c]:
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(c)
        return True if not stack else False