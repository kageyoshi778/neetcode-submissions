class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        j = sorted(list(s))
        i = sorted(list(t))
        for a in range(len(j)):
            if j[a] != i[a]:
                return False
        return True