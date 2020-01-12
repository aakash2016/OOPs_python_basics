## Operator Overloading..
class Py:
	def __init__(self, pages):
		self.pages = pages

	##__add__ is a special function to override.
	def __add__(self, other):#self = b1 and other = b2
		return self.pages + other.pages

	def __mul__(self, other):
		return self.pages * other.pages

	def __gt__(self, other):
		return self.pages > other.pages

class cpp:
	def __init__(self, pages):
		self.pages = pages


b1 = Py(55)
b2 = Py(12)

print(b1 +b2) #b1.__add(b2)
print(b1 *b2)
print(b1 <b2)

c1 = cpp(54)
print(b1 +c1) ## here Py has that special fn/
#print(c1 +b1) will give error..
print(b1 >c1)
