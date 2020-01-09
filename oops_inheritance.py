## OOPS inheritance.
# you dont need to write the same class everytime.
# you can inherit all the properties of a class.
## BASE CLASS(parent class) -->> DERIVED CLASS.(child class).
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

class square(polygon): # sub class
# square is a derived clas s of polygon,
	## WE INHERITED ALL THE FUNCTIONALITIES OF POLYGON.
	def area(self):
		return self.get_height()*self.get_width()

s1 = square()
s1.set_value(12,15)
print(s1.area())
## remember -- for private you always need to do set and get'
