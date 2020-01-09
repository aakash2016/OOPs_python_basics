## Error Handling
## Errors = bugs. process of removing = debugging.
## 1. Complile time error, because of mistake in syntax. << -- we havent executed any line of code.
## 2. Runtime error, because of lack of memory, division by 0. << -- hard to track down. <<-- here some lines will be executed.
## 3. Logical error, becuase of wrong error and wrong formats.

## Exception is runtime error which can be handled by the programmer.
x=5
y=0
res = None

try:
	res=x/y
except Exception as e:
	print('error in code', e)
	print(type(e))
else:                         ## No exceptions, -- run this code.
	print('inside else')
finally:		## always run this code.
	print('inside finally')
print(res)

## RAising exception/
class tea:
	def __init__(self, temperature):
		self.__temperature = temperature

	def drink_tea(self):
		if self.__temperature > 85:
			print('hot') 
		elif self.__temperature < 65:
			print('cold')
		else:
			print('good')
cup = tea(66)
cup.drink_tea()

## user defined exception.
class teaexception(Exception):## we inherit base class exception.
	def __init__(self, msg):
		self.msg = msg

class cofee:
	def __init__(self, temperature):
		self.__temperature = temperature

	def drink_cofee(self):
		if self.__temperature > 85:
			raise teaexception('hot') 
		elif self.__temperature < 65:
			print('cold')
		else:
			print('good')
cup = cofee(100)
cup.drink_cofee()
