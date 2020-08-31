class Solution:
	def minOperations(self, n: int) -> int:
		arr = [(2 * i) + 1 for i in range(n)]
		goal_num = n
		answer = 0

		for num in arr:
			if num < goal_num:
				answer += goal_num - num
			else:
				break

		return answer


test = Solution()
n = 512521
print(test.minOperations(n))
