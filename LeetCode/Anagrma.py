from collections import Counter


class Solution:
	def minSteps(self, s: str, t: str) -> int:
		check = dict(Counter(s) - Counter(t))
		print(Counter(s))
		print(Counter(t))
		print(check)
		output = 0
		for val in check.values():
			output += val

		return output


test = Solution()
s = 'leetcode'
t = 'practice'
print(test.minSteps(s, t))