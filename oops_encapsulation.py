## Encapsulation.. 
## In OOP you can restrict access to methods and variabls,
# This will prevent the data from being modified by accident.

## __ means you have made that attribute as private.
class speed:
	def __init__(self):
		self.speed = 10
		self.__new_speed = 45 ## private attribute/

	## GETTER
	def get_new_speed(self): ## returning private value with the help of public fn.
		return self.__new_speed

	## SETTER
	def set_new_speed(self, new_speed):	
		self.__new_speed = new_speed

s = speed()
print(s.speed)
#print(s.__new_speed) ##ERROR, i CANNOT ACCESS THIS PRIVATE VALUE.
## BUT, WE CAN MODIFY IT.
#s.__new_speed = 12
#print(s.__new_speed)
s.set_new_speed(55)
print(s.get_new_speed())

## remember -- you cannot access private outside the class.
