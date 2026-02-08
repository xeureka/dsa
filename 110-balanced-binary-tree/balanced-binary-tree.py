# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            if abs(left - right) > 1:
                ans = False
            return max(left, right)
        dfs(root)
        return ans