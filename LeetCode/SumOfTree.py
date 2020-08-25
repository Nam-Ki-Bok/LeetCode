from typing import List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def bstToGst(self, root: TreeNode) -> TreeNode:
		global _sum
		_sum = 0

		def post_order(cur_node):
			global _sum
			if not cur_node:
				return
			else:
				post_order(cur_node.right)
				_sum += cur_node.val
				cur_node.val = _sum
				post_order(cur_node.left)

		post_order(root)
		return root


# tree = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
