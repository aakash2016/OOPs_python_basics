## Super() in python. -->> a proxy that allows you to refer to parent class.
class Parent:
	def __init__(self, name):
		print('parent __init__', name)

class Parent2:
	def __init__(self, name):
		print('parent2 __init__', name)
	
class Child:
	def __init__(self):
		print('child __init__')
		Parent.__init__(self, 'aakash') ## wo super()

class Chill(Parent):
	def __init__(self):
		print('chill __init__')
		super().__init__('aakash') ## with super() the class Parent is called.

c1 = Child()
c2 = Chill()
## method resolution order.
print(Chill.__mro__) ## gives the sequence of how classes are called.

class Chill2(Parent2, Parent):
	def __init__(self):
		print('chill2 __init__')
		super().__init__('aakash') ## with super() both Parent classes are called. But 1st only arguments op is shown.

c3 = Chill2()	
print(Chill2.__mro__)  
