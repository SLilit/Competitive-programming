# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        if not t1:
            return t2
        return t1

        
        
        def merge(to, tt):
            
            if not to and not tt:
                return None
            
            t = TreeNode(None)
        
            if to and tt:
                t.val = to.val + tt.val
                t.left = merge(to.left, tt.left)
                t.right = merge(to.right, tt.right)
            elif to:
                t.val = to.val 
                t.left = merge(to.left, None)
                t.right = merge(to.right, None)
            elif tt:
                t.val = tt.val
                t.left = merge(None, tt.left)
                t.right = merge(None, tt.right)
        
            return t
        return merge(t1, t2)