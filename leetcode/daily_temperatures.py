# https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        #[(temp, index)] 
        #current = i
        stack, res, i = [], [0]*len(T), 0
        while i < len(T):
            curr = T[i]
            while stack:
                temp = stack.pop()
                if curr > temp[0]:
                    res[temp[1]] = i - temp[1]
                else:
                    stack.append(temp)
                    break
            stack.append((curr, i))
            i += 1
        return res
