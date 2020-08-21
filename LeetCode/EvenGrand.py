from collections import deque
import null


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def sumEvenGrandparent(self, root: TreeNode) -> int:
		def DFS(node, parent, grand, answer):
			if not node:
				return 0

			if grand and grand.val % 2 == 0:
				answer.append(node.val)
			DFS(node.left, node, parent, answer)
			DFS(node.right, node, parent, answer)

		answer = []
		DFS(root, None, None, answer)
		return sum(answer)



