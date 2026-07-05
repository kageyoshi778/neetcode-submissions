'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        strin= ()
        count=0
        m=0
        for i in s:
            if i not in strin:
                count+=1
                strin.add(i)
            else:

                m= max(m,count)
                count=1'''
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len
