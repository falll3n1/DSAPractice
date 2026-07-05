# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node:  return 0
            num = num * 10 + node.val
            if not node.left and not node.right:
                return num                       # this path's finished number, sent UP
            return dfs(node.left, num) + dfs(node.right, num)   # captured and summed
        return dfs(root, 0)


        
        # def dfs(node,  sum ):
        #     if not node : return 0
        #     sum = sum*10 + node.val 
        #     if not node.left and not node.right:
        #         return sum
        #     else:
        #         dfs(node.left, sum) + dfs(node.right, sum)
                
        
        # return dfs(root, 0)

        