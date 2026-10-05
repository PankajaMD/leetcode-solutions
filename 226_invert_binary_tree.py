class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left

        return root
