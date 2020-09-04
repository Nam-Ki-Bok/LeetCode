class CustomStack:

	def __init__(self, maxSize: int):
		self.my_maxsize = maxSize
		self.my_stack = []

	def push(self, x: int) -> None:
		if len(self.my_stack) < self.my_maxsize:
			self.my_stack.append(x)

	def pop(self) -> int:
		if self.my_stack:
			return self.my_stack.pop()
		else:
			return -1

	def increment(self, k: int, val: int) -> None:
		idx = 0
		while idx < min(k, self.my_maxsize):
			try:
				self.my_stack[idx] += val
			except IndexError:
				break
			idx += 1


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)