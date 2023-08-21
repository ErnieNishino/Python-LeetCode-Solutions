class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = dict(Counter(list(s)))
        d_order = sorted(d.items(), key=lambda x: x[1], reverse=False)
        if d_order[0][1] >= 2:
            return -1
        else:
            return s.index(d_order[0][0])