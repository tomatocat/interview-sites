# https://leetcode.com/problems/word-search/

class Solution(object):
    def search(self, board, word, row, col):
        # Check for duplicates or out of bounds
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        
        # Check if first letter of word matches, and whether we are done
        if word[0] != board[row][col]:
            return False
        if len(word) == 1:
            return True
        
        # Mark current position as visited, slice word
        tmp, board[row][col] = board[row][col], '0' 
        word = word[1:]
        
        # Search all four directions, if false then un-mark visitation
        if self.search(board, word, row + 1, col) \
            or self.search(board, word, row - 1, col) \
            or self.search(board, word, row, col + 1) \
            or self.search(board, word, row, col - 1):
            return True
        else:
            board[row][col] = tmp
        
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        if len(word) > rows*cols:
            return False
        for row in range(rows):
            for col in range(cols):
                if self.search(board, word, row, col):
                    return True
        return False       
