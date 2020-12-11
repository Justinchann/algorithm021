# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     root = stack.pop()
        #     res.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        #     if root.left:
        #         stack.append(root.left)
        # return res

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return res