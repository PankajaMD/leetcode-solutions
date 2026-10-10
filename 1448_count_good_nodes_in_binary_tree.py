# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root, -sys.maxsize - 1)
    def count_good_nodes(self, node: TreeNode, max_so_far: int) -> int:
        if node is None:
            return 0

        count = 0
        if node.val >= max_so_far:
            count = 1  # Current node is a good node
            max_so_far = node.val  # Update the maximum value along the path

        # Count good nodes in the left and right subtrees
        count += self.count_good_nodes(node.left, max_so_far)
        count += self.count_good_nodes(node.right, max_so_far)

        return count
