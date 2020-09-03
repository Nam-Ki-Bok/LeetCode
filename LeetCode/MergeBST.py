from typing import List


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def make_sort_list(self, root):
		_list = []

		def in_order(root):
			if not root:
				return

			else:
				in_order(root.left)
				_list.append(root.val)
				in_order(root.right)

		in_order(root)
		return _list

	def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
		a = self.make_sort_list(root1)
		b = self.make_sort_list(root2)
		merge = []
		a_idx, b_idx = 0, 0

		while a_idx < len(a) and b_idx < len(b):
			if a[a_idx] >= b[b_idx]:
				merge.append(b[b_idx])
				b_idx += 1
			else:
				merge.append(a[a_idx])
				a_idx += 1

		while a_idx < len(a):
			merge.append(a[a_idx])
			a_idx += 1
		while b_idx < len(b):
			merge.append(b[b_idx])
			b_idx += 1

		return merge


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

test = Solution()
print(test.getAllElements(root1, root2))