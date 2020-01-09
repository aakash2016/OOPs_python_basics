## class variables..
class employee:
	num_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):##constructor.
	## the name __init__ IS RESERVED in py. its a special functional method. 
	## when we create methods within a class, they receive instance as the first arg. automatically.
	## we call this instance self.
	## self is the instance/object being created,
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		employee.num_emps += 1

	##new method
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		#self.pay = int(self.pay * employee.raise_amount) 
		## we have to access the class variables from class
		## but we can also access them from the instances.	
		self.pay = int(self.pay * self.raise_amount)

emp_1 = employee('aakash', 'agrawal', 500)
emp_2 = employee('test', 'agrawal', 5000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

## so you can access the class variables from both class and instances.
print(emp_1.raise_amount)
print(employee.raise_amount)

## printing the namespace of the emplooyee -->> __dict__
#print(emp_1.__dict__)## you wont get the raise amount in this. 
#print(employee.__dict__) ## class contains the raise amount attribute.

##
employee.raise_amount =1.05
print(emp_1.raise_amount)
print(employee.raise_amount)

emp_1.raise_amount =1.05# would change only for the employee1.
print(emp_1.__dict__)## you get the raise amount in this. 

print(employee.num_emps)

