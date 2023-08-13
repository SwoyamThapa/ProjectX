# Module to check if which number is minimum or maximum

class Minmax:

	def __init__(self, num1, num2):

		self.num1 = num1
		self.num2 = num2

	def min(self):

		minimum = self.num1

		if self.num1 > self.num2:
			minimum = self.num2

		return minimum

	def max(self):

		maximum = self.num1

		if self.num2 > self.num1:
			maximum = self.num2

		return maximum

