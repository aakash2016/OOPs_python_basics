## the __init__ function is called a constructor or initializer. 
# __init__ method is automatically called when you create new instance of a class. How?
class student:
	def __init__(self):
		self.name = 'aakash'
		print('init is called automatically')

s1 = student() ##here we are calling  a constructor.

## a constructor is a special type of method(function) which is used to initialize the instance members of the class.
## __init__ is a constructor method. these methods are called themselves.
## self -- >> refers to the class instance., self contains memory of the instance.

## CAn we use constructor 2-3 times??
## answer -- whatever will be the last constructor that will be in use. so, you can only use 1 constructor.
class fac:
	def __init__(self):
		print('1st init method')

	def __init__(self):	
		print('2nd init method')

	def display(self):
		print('Hi!')

f1 = fac()
f1.display()
