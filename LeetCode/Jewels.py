import collections


class Solution:
	def numJewelsInStones(self, J: str, S: str) -> int:
		answer = 0
		cnt = collections.Counter(S)
		for val in J:
			answer += cnt[val]

		return answer


test = Solution()
J = 'z'
S = 'ZZ'
print(test.numJewelsInStones(J, S))