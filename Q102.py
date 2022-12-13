# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        
        preorder_traversal = [[]]
        preorder_traversal[-1].append(root.val)
        children = [root.left, root.right]
        while not all(v is None for v in children):
            preorder_traversal.append([])
            child_temp = []
            for child in children:
                if child is not None:
                    preorder_traversal[-1].append(child.val)
                    child_temp.extend([child.left, child.right])
            children = child_temp

        return preorder_traversal

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.levelOrder(root))