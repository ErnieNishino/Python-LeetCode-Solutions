class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp = [1]*(i+1)
            for j in range(i+1):
                if 0 < j < i:
                    temp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(temp)
        return res
