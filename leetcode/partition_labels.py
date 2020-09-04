# https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_index, i = dict(), 0
        start_p, end_p, res = 0, -1, []
        
        # Populate map of letter to last_index
        while i < len(S):
            last_index[S[i]] = i
            i += 1
            
        # Sweep through string and update partitions
        i = 0
        while i < len(S):
            last = last_index[S[i]]
            if last == len(S):
                res.append(last - start_p + 1)
                break
            if last > end_p:
                end_p = last
            if i == end_p:
                length = end_p - start_p + 1
                start_p = end_p + 1
                end_p = i
                res.append(length)
            i += 1
        
        return res    
    
