# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid  = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

        '''
        
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # advancing pointer into preorder

        def build(left: int, right: int) -> TreeNode | None:
            
            if left > right:
                return None

            # Next preorder value is this subtree's root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Its position in inorder splits left vs. right subtree
            mid = idx_map[root_val]

            # Build LEFT first (preorder lists the whole left subtree next)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
        '''