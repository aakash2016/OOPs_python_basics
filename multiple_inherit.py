## Multiple inheritance.
## inherit functionalit of 2 classes.
class polygon:
	##def __init__(self): because we will not create any object of polygon.
	__width = None## private attribute
	__height = None

	## SETTER
	def set_value(self, width, height):
		self.__width = width
		self.__height = height## private only restricted to polygon class not to child class

	def get_height(self):
		return self.__height

	def get_width(self):
		return self.__width	

class shape:
	__color = None
	
	def set_color(self, color):
		self.__color = color
	
	def get_color(self):
		return self.__color 

class square(polygon, shape): # sub class
# square is a derived class of polygon,
	## WE INHERITED ALL THE FUNCTIONALITIES OF POLYGON.
	def area(self):
		return self.get_height()*self.get_width()

s1 = square()
s1.set_value(12,15)
s1.set_color('blue')
print(s1.area(), s1.get_color())
