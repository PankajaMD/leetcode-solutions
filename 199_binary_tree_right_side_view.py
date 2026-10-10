# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()
                if i == level_size - 1:
                    result.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)

        return result



