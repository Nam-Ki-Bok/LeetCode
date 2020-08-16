from typing import List


class Solution:
	def shuffle(self, nums: List[int], n: int) -> List[int]:
		answer = []
		list_a = nums[:n]
		list_b = nums[n:]

		for a, b in zip(list_a, list_b):
			answer.append(a)
			answer.append(b)

		return answer


test = Solution()
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(test.shuffle(nums, n))
