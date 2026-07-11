# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valueToindex = {val:i for i, val in enumerate(inorder)}

        def dfs(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            
            root = TreeNode(preorder[pl])
            index = valueToindex[preorder[pl]]
            left_size = index - il
            root.left = dfs(pl + 1, pl + left_size, il, index - 1)
            root.right = dfs(pl + left_size + 1, pr, index + 1, ir)
            return root
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)