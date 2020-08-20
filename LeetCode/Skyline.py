from typing import List


class Solution:
	def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
		left_sky = [max(val) for val in grid]
		up_sky = [max(val) for val in zip(*grid)]

		increase = []
		for i in range(len(left_sky)):
			tmp = []
			for j in range(len(up_sky)):
				tmp.append(min(left_sky[i], up_sky[j]))
			increase.append(tmp)

		answer = 0
		for origin, up in zip(grid, increase):
			answer += sum(up) - sum(origin)

		return answer


test = Solution()
grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(test.maxIncreaseKeepingSkyline(grid))