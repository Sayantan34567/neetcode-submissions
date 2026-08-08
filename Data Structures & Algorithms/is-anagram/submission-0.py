class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_freq = {key: 0 for key in s}
        t_freq = {key: 0 for key in t}
        for letter in s:
            s_freq[letter] += 1
        for letter in t:
            t_freq[letter] += 1
        if s_freq == t_freq:
            return True
        else:
            return False
        
