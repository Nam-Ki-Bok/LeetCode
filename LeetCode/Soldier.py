from typing import List
from itertools import combinations


class Solution:
	def solution1(self, rating: List[int]) -> int:
		answer = 0
		for cur in combinations(rating, 3):
			if cur[0] < cur[1] and cur[1] < cur[2]:
				answer += 1
			elif cur[0] > cur[1] and cur[1] > cur[2]:
				answer += 1

		return answer

	def solution2(self, rating: List[int]) -> int:
		answer = 0
		for i in range(len(rating) - 2):
			for j in range(i + 1, len(rating) - 1):
				for k in range(j + 1, len(rating)):
					if rating[i] > rating[j] > rating[k]:
						answer += 1
					elif rating[i] < rating[j] < rating[k]:
						answer += 1

		return answer


test = Solution()
rating = [2, 5, 3, 4, 1]
rating = [i for i in range(1, 1000)]

print(test.solution1(rating))
