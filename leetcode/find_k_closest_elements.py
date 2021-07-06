# https://leetcode.com/problems/find-k-closest-elements/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = 0
        while i < len(arr) and arr[i] < x:
            i = i + 1
        # i must be at an index geq k now
        # 2 pointer approach
        res = []
        left = i - 1 # less than k
        right = i
        while len(res) < k:
            if left >= 0:
                if right < len(arr): # compare both indices
                    if (arr[right]-x) < (x - arr[left]):
                        res.append(arr[right])
                        right = right + 1
                    else:
                        res.insert(0, arr[left])
                        left = left - 1
                else: # left only
                    res.insert(0, arr[left])
                    left = left - 1
            else: # right only
                res.append(arr[right])
                right = right + 1
        return res
        
