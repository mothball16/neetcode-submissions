class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        goal_length = len(word)
        num_rows = len(board)
        num_cols = len(board[0]) or 0
        NEIGHBORS = ((0, 1), (0, -1), (-1, 0), (1, 0))
        def is_valid(row, col, desired):
            return (
                0 <= row < num_rows
                and 0 <= col < num_cols
                and board[row][col] == desired
            )
        """
        CCBB
        Choices - All elements on the board
        Constraints - Nodes cannot be re-visited. Can't be off the board
        Base Case - Length of the path is the goal length
        Backtrack - Pop this node off the visited stack
        """
        def backtrack(row, col, length):

            # base case
            if length == goal_length:
                return True
            
            if not is_valid(row, col, word[length]):
                return False
            
            # make choice
            temp = board[row][col]
            board[row][col] = "#"
            length += 1

            for neighbor in NEIGHBORS:
                next_row, next_col = row + neighbor[0], col + neighbor[1]

                # backtrack
                if backtrack(next_row, next_col, length):
                    return True
                    
            # undo choice - flip the node back to its original
            board[row][col] = temp
            length -= 1

            return False


        # pruning pass
        # count up all letters
        last_letter = word[-1]
        first_letter = word[0]
        letters = {}
        for row in range(num_rows):
            for ch in board[row]:
                letters[ch] = letters.get(ch, 0) + 1

        # make sure every letter in the word exists
        for ch in word:
            if not letters.get(ch):
                return False

        # use the less-occuring letter as the first letter
        if letters[last_letter] < letters[first_letter]:
            first_letter, last_letter = last_letter, first_letter
            word = word[::-1]
        

        # iterate through each element
        for row in range(num_rows):
            for col in range(num_cols):
                if backtrack(row, col, 0):
                    return True

        return False