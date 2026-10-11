# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndex = 0
        self.inorderIndexMap = {}
        
        for i in range(len(inorder)):
            self.inorderIndexMap[inorder[i]] = i
        
        return self.arrayToTree(preorder, 0, len(preorder) - 1)
    
    def arrayToTree(self, preorder: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        rootValue = preorder[self.preorderIndex]
        self.preorderIndex += 1
        
        root = TreeNode(rootValue)
        root.left = self.arrayToTree(preorder, left, self.inorderIndexMap[rootValue] - 1)
        root.right = self.arrayToTree(preorder, self.inorderIndexMap[rootValue] + 1, right)
        
        return root
        
