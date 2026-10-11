class Solution:
    def inOrder(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if root is None:
            return arr
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        nums = self.inOrder(root, [])
        return nums[k - 1]
