# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=None, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        def find_node(tree, tree_list, l = [p.val, q.val]):
            if tree.left is not None:
                tree_list.append(tree.left)
                if tree.left.val not in l:
                    tt = find_node(tree.left, tree_list, n)
                    if not tt:
                        pass
                    else:
                        return find_node
                else:
                    return tree_list
                
            if tree.right is not None:
                tree_list.append(tree.right)
                if tree.right.val != n.val:
                    tt = find_node(tree.right, tree_list, n)
                    if not tt:
                        pass
                    else:
                        return tt
                else:
                    return tree_list

            tree_list.pop()
            return False
                
            
        p_tree = [root]
        q_tree = [root]
        
        if root.val == p and root.val == q:
            return root

        if root.val == p and root.
            p_tree = find_node(root, [p_tree,p_tree], [p])
        
        if root != q:
            q_tree = find_node(root, q_tree, q)
            
        for i in range(min(len(p_tree), len(q_tree)), -1):
            if p_tree[i] == q_tree[i]:
                return p_tree[i]

root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7, TreeNode(3), TreeNode(5)), TreeNode(9)))
p = TreeNode(2, TreeNode(0), TreeNode(4))
q = TreeNode(8, TreeNode(7, TreeNode(3), TreeNode(5)), TreeNode(9))

sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))