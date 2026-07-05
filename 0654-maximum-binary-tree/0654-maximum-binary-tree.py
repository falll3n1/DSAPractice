# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []   # decreasing by value, bottom = largest
        for num in nums:
            node = TreeNode(num)
            # Q1: everything smaller is dominated by num and sits to its left
            #     -> last (largest) popped becomes num's LEFT child, chain and all
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            # Q2: whoever remains is larger + to the left -> num is their RIGHT child
            if stack:
                stack[-1].right = node
            # Q3: push num; it's now the smallest -> invariant restored
            stack.append(node)

        return stack[0]  

        # if not nums:return None

        # i = nums.index(max(nums))
        # root = TreeNode(nums[i])
        # root.left = self.constructMaximumBinaryTree(nums[:i])
        # root.right = self.constructMaximumBinaryTree(nums[i+1:])

        # return root