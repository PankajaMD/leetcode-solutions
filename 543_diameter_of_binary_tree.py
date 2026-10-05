class Solution:
    def __init__(self):
        self.max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_height(root)
        return self.max_diameter
    def get_height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
