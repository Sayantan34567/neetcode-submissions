class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_freq = {key: 0 for key in s}
        t_freq = {key: 0 for key in t}
        for i in range(len(s)):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1
        if s_freq == t_freq:
            return True
        else:
            return False
        
