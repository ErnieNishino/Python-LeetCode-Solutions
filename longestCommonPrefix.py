class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        check = 1
        for idx, i in enumerate(strs[0]):
            for j in strs[1:]:
                if idx > len(j)-1:
                    check = 0
                    break
                if i == j[idx]:
                    continue
                else:
                    check = 0
                    break
            if check:
                res += i
            else:
                break
        return res