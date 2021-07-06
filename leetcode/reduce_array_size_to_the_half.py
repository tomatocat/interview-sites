
# https://leetcode.com/problems/reduce-array-size-to-the-half/
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Input is not sorted
        # Use a pq -> use dictionary and then sort it
        freqs = dict()
        for n in arr: # freq table O(n)
            if freqs.get(n) == None:
                freqs[n] = 1
            else:
                freqs[n] = freqs.get(n) + 1
        target, count = len(arr) // 2, 0
        arr2 = sorted(freqs, key = freqs.get, reverse=True) # O(nlogn)
        for key in arr2: # O(n)
            target -= freqs[key]
            count += 1
            if target <= 0:
                break
        return count
        
