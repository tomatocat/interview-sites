# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Priority-first search (i, j, value)
        pq = [(0, 0, matrix[0][0])]
        seen = set()
        seen.add((0, 0))
        while k > 1:
            (i, j, x) = pq.pop()
            print(x)
            if i+1 < len(matrix) and j+1 < len(matrix) and not (i+1, j+1) in seen:
                seen.add((i+1, j+1))
                pq.append((i+1,j+1,matrix[i+1][j+1]))
            if i+1 < len(matrix) and not (i+1, j) in seen:
                seen.add((i+1,j))
                pq.append((i+1,j,matrix[i+1][j]))
            if j+1 < len(matrix) and not (i, j+1) in seen:
                seen.add((i,j+1))
                pq.append((i,j+1,matrix[i][j+1]))
            pq.sort(key= lambda t : t[2], reverse=True)
            k = k - 1
        return pq.pop()[2] # End is smallest value
    
