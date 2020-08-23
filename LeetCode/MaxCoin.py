from typing import List
from collections import deque

class Solution:
	def maxCoins(self, piles: List[int]) -> int:
		answer = 0
		queue = deque()
		queue.extend(sorted(piles))

		while queue:
			queue.pop()
			answer += queue.pop()
			queue.popleft()

		return answer


test = Solution()
piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]

print(test.maxCoins(piles))