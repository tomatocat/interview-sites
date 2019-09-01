# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.m = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        if self.m:
            self.m.append(min(self.m[-1], x))
        else:
            self.m.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.arr:
            self.arr.pop()
            self.m.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.m[-1]
        return None
