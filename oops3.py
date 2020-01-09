##using init
class employee:
	def __init__(self, first, last, pay):##constructor.
	## the name __init__ IS RESERVED in py. its a special functional method. 
	## when we create methods within a class, they receive instance as the first arg. automatically.
	## we call this instance self.
	## self is the instance/object being created,
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	##new method
	def fullname(self): ##instace method.
		return '{} {}'.format(self.first, self.last)

emp_1 = employee('aakash', 'agrawal', 500)
emp_2 = employee('test', 'agrawal', 5000)
print(emp_1.fullname()) ## you need parentheses because it is a method and not any attribute/
## REUSABILITY..
print(emp_2.fullname())

###
print(emp_1.fullname())## you call method in an instance. we dont pass the self.
print(employee.fullname(emp_1))## both do same thing.
