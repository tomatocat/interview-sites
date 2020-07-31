# https://leetcode.com/problems/word-break-ii/

class Solution(object):
    
    def help(self, s, wordSet, memo):
        if not s: # empty string
            return ""
        # go through every index
        result = []
        if s in wordSet:
            result.append(s)
        for i in range(1, len(s)):
            if s[:i] in wordSet:
                # Make split
                split = s[i:]
                if split in memo:
                    rest = memo[split]
                else:
                    rest = self.help(s[i:], wordSet, memo)
                if rest:
                    for x in rest:
                        result.append(s[:i] + " " + x)
        memo[s] = result
        return result
            
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.help(s, set(wordDict), dict())
