## Abstract Class.
from abc import ABC, abstractmethod
class Shape(ABC): ## now shape is an abstract class.
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Square(Shape):
	def __init__(self, side):
		self.__side = side

	def area(self):
		return self.__side*self.__side

	def perimeter(self):
		return 4*self.__side

# I dont want the user to create an object of parent class.
sq1 = Square(10)
print(sq1.area())
