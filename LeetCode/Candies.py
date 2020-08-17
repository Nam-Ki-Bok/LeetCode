from typing import List


class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		answer = []
		max_val = max(candies)

		for val in candies:
			if val + extraCandies >= max_val:
				answer.append(True)
			else:
				answer.append(False)

		return answer


test = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(test.kidsWithCandies(candies, extraCandies))