class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        else:
            leftmax = self.maxDepth(root.left)
            rightmax = self.maxDepth(root.right)
            return max(leftmax, rightmax) + 1
