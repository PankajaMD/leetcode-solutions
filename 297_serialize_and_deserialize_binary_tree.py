# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def recserialize(self, root, s):
        if root is None:
            s += "null,"
        else:
            s += str(root.val) + ","
            s = self.recserialize(root.left, s)
            s = self.recserialize(root.right, s)
        return s

    def serialize(self, root):
        """Encodes a tree to a single string."""
        return self.recserialize(root, "")

    def recdeserialize(self, lst):
        if lst[0] == "null":
            lst.pop(0)
            return None

        root = TreeNode(int(lst[0]))
        lst.pop(0)
        root.left = self.recdeserialize(lst)
        root.right = self.recdeserialize(lst)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        strList = data.split(",")
        return self.recdeserialize(strList)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
