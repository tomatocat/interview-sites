# https://leetcode.com/problems/reshape-the-matrix/
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        mat2 = [item for sublist in mat for item in sublist]
        if len(mat2) != r*c:
            return mat
        res = []
        i = 0
        for row in range(r):
            res2 = []
            for col in range(c):
                res2.append(mat2[i])
                i = i + 1
            res.append(res2[:])
        return res
            
