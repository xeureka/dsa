# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            lijoch = []
            if node.left: lijoch.extend(dfs(node.left))
            if node.right: lijoch.extend(dfs(node.right))
            if not lijoch:
                ans += node.val
                return [1]
            mine = []
            for depth in lijoch:
                ans += (node.val * (1 << depth))
                mine.append(depth + 1)
            return mine
        dfs(root)
        return ans
