class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.fullboard = board
        self.answer = []

        # Build the trie from all words
        root = TrieNode()
        for word in words:
            node = root
            for letter in word:
                if letter in node.children:
                    node = node.children[letter]
                else:
                    newNode = TrieNode()
                    node.children[letter] = newNode
                    node = newNode
            node.word = word

        # Start a backtracking search from every cell that begins some word
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    self.backtracking(row, col, root)

        return self.answer

    def backtracking(self, row: int, col: int, parent: TrieNode) -> None:
        letter = self.fullboard[row][col]
        currNode = parent.children[letter]

        # Found a complete word
        if currNode.word is not None:
            self.answer.append(currNode.word)
            currNode.word = None  # avoid adding duplicates

        # Mark this cell as visited
        self.fullboard[row][col] = '#'

        rowOffset = [-1, 0, 1, 0]
        colOffset = [0, 1, 0, -1]

        for i in range(4):
            newRow = row + rowOffset[i]
            newCol = col + colOffset[i]

            if newRow < 0 or newCol < 0 or newRow >= len(self.fullboard) or newCol >= len(self.fullboard[0]):
                continue

            if self.fullboard[newRow][newCol] in currNode.children:
                self.backtracking(newRow, newCol, currNode)

        # Restore the cell (backtrack)
        self.fullboard[row][col] = letter
