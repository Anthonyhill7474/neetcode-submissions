# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def check(node):
            if p.val < node.val and q.val < node.val:
                return check(node.left)
            elif p.val > node.val and q.val > node.val:
                return check(node.right)
            
            return node
        return check(root)