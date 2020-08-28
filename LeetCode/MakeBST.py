from typing import List


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
		root = TreeNode(preorder[0])

		def make_BST(root, val):
			cur_node = root

			while True:
				if val < cur_node.val:
					if cur_node.left:
						cur_node = cur_node.left
					else:
						cur_node.left = TreeNode(val)
						break

				else:
					if cur_node.right:
						cur_node = cur_node.right
					else:
						cur_node.right = TreeNode(val)
						break

		for val in preorder[1:]:
			make_BST(root, val)

		return root


test = Solution()
arr = [8, 5, 1, 7, 10, 12]
print(test.bstFromPreorder(arr).left.right.val)