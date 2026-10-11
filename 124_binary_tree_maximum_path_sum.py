class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    
    def maxGain(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        leftGain = max(self.maxGain(node.left), 0)
        rightGain = max(self.maxGain(node.right), 0)
        
        priceNewPath = node.val + leftGain + rightGain
        
        self.maxSum = max(self.maxSum, priceNewPath)
        
        return node.val + max(leftGain, rightGain)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.maxGain(root)
        return self.maxSum
