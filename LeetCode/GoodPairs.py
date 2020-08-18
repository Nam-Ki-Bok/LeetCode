import collections
from typing import List


class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		pair_num = 0
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] == nums[j]:
					pair_num += 1
		return pair_num

		# d = collections.defaultdict(int)
		# for i in nums:
		# 	d[i] += 1
		# return sum(k * (k - 1) // 2 for k in d.values())

		# d = dict()
		# for i in nums:
		# 	try:
		# 		d[i] += 1
		# 	except KeyError:
		# 		d[i] = 1
		# return sum(k * (k - 1) // 2 for k in d.values())


test = Solution()
nums = [3, 3, 3, 3, 3, 3, 3]
print(test.numIdenticalPairs(nums))
