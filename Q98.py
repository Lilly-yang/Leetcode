# Definition for a binary tree node.
from fcntl import F_SEAL_SEAL
from xmlrpc.client import FastParser


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def Recursion(node, node_range):
            if node.left is not None:
                if node.left.val > node_range[0] and node.left.val < node_range[-1]:
                    if node.left.val < node.val:
                        if node.val < node_range[-1]:
                            if Recursion(node.left, [node_range[0], node.val]) is not None:
                                return False
                        else:
                            if Recursion(node.left, node_range) is not None:
                                return False
                    else:
                        return False
                else:
                    return False
            
            if node.right is not None:
                if node.right.val > node_range[0] and node.right.val < node_range[-1]:
                    if node.right.val > node.val:
                        if node.val > node_range[0]:
                            if Recursion(node.right, [node.val, node_range[-1]]) is not None:
                                return False
                        else:
                            if Recursion(node.right) is not None:
                                return False
                    else:
                        return False
                else:
                    return False

        if Recursion(root, [float('-inf'), float('inf')]) is not None:
            return False
        else:
            return True

root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
# root = TreeNode(2, TreeNode(1), TreeNode(3))
sol = Solution()
print(sol.isValidBST(root))