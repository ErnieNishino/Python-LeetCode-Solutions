class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma = 0
        temp = []
        for i in s:
            if i in temp:
                if ma < len(temp):
                    ma = len(temp)
                temp = temp[temp.index(i)+1:]
            temp.append(i)
        if ma < len(temp):
            ma = len(temp)
        return ma