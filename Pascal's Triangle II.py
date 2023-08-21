class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = [[1]]
        for i in range(1, rowIndex + 1):
            res = [1] * (i + 1)
            for j in range(i + 1):
                if 0 < j < i:
                    res[j] = temp[i - 1][j - 1] + temp[i - 1][j]
            temp.append(res)
        return temp[rowIndex]
