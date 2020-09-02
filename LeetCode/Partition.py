from typing import List


class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		output = []
		idx = 0
		while S:
			find_alpha = S[0]
			for i, val in enumerate(S[::-1]):
				if val == find_alpha:
					idx = len(S) - i - 1
					break

			partition = S[:idx + 1]
			S = S[idx + 1:]

			p_idx = 0
			while p_idx < len(partition):
				add_idx = -1
				for i, S_val in enumerate(S[::-1]):
					if partition[p_idx] == S_val:
						add_idx = len(S) - i - 1
						break

				if add_idx >= 0:
					partition += S[:add_idx + 1]
					S = S[add_idx + 1:]
				p_idx += 1

			output.append(len(partition))
		return output


test = Solution()
# S = "qiejxqfnqceocmy"
S = "ababcbacadefegdehijhklij"
print(test.partitionLabels(S))