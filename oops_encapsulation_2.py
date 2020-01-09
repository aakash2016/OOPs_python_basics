## private methods.
# '_' means it is partially private, you can easily access thid.
# '__' means private.

class exam:
	def __init__(self):
		self.x = 45
		self._y = 12
		self.__z = 55

	def public_method(self):
		print(self.x)
		print(self._y)
		print(self.__z)
		self.__private_method()

	def __private_method(self): ## you want certain entitities to be not modified.
		print('iniside private')

e1 = exam()
e1.public_method()
#e1.__private_method() ## ERROR
## so you need to call private method inside the class.

