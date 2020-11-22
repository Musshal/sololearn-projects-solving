# project solver: musshal

class Juice:
	def __Init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
	def __str__(self):
		return (self.name + ' ('+str(self.capacity)+'L)')
	def __add__(self, other):
		self.name += '&' + other.name
		self.capacity += other.capacity
		return Juice(self.name, self.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
