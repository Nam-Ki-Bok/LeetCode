from typing import List
import collections


class Solution:
	def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
		output = []

		idx_dict = collections.defaultdict(list)

		for idx, i in enumerate(groupSizes):
			idx_dict[i].append(idx)

		for key in idx_dict:
			for i in range(0, len(idx_dict[key]), key):
				output.append(idx_dict[key][i:i + key])

		return output


test = Solution()
groupSizes = [1, 2, 2, 1, 3, 2, 3, 3, 2]
print(test.groupThePeople(groupSizes))