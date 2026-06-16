# https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16


class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for c in s:
            if c=='*':
                if res:
                    res.pop()
            elif c=="#":
                if res:
                    res.extend(res)
            elif c=='%':
                res.reverse()
            else:
                res.append(c)
        return ''.join(res)