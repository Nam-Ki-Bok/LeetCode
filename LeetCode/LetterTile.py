import itertools


class Solution:
	def numTilePossibilities(self, tiles: str) -> int:
		answer = []
		for i in range(1, len(tiles) + 1):
			_set = itertools.combinations(tiles, i)
			for j in _set:
				answer += itertools.permutations(j)

		return len(set(answer))


test = Solution()
tiles = 'CCD'
print(test.numTilePossibilities(tiles))

# {('B',), ('A',)} ^^ [('B',), ('A',)]
# {('A', 'B'), ('A', 'A')} ^^ [('B',), ('A',), ('A', 'B'), ('B', 'A'), ('A', 'A')]
# {('A', 'A', 'B')} ^^ [('B',), ('A',), ('A', 'B'), ('B', 'A'), ('A', 'A'), ('B', 'A', 'A'), ('A', 'A', 'B'), ('A', 'B', 'A')]

# {('D',), ('C',)} ^^ [('D',), ('C',)]
# {('D', 'C'), ('C', 'C'), ('C', 'D')} ^^ [('D',), ('C',), ('D', 'C'), ('C', 'D'), ('C', 'C'), ('D', 'C'), ('C', 'D')]
# {('C', 'D', 'C')} ^^ [('D',), ('C',), ('D', 'C'), ('C', 'D'), ('C', 'C'), ('D', 'C'), ('C', 'D'), ('D', 'C', 'C'), ('C', 'D', 'C'), ('C', 'C', 'D')]

print(list(itertools.combinations('AAB', 2)))
print(list(itertools.combinations('CDC', 2)))