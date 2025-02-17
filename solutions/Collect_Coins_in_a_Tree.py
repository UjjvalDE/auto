class Solution:
    def collectCoins(self, root: TreeNode) -> List[List[int]]:
        def dfs(node):
            if not node:
                return
            res.append([node.val, node.left, node.right])
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return [[child for parent in res for child in (parent[1:] or [])] for _ in res]