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

emp_1 = employee('aakash', 'agrawal', 500)
emp_2 = employee('test', 'agrawal', 5000)
print(emp_1.pay); print(emp_2.pay)
## now we dont need the manual assignments.
## now first, email, pay are all the attributes of our class.

## we can also add some methods manually to our class.
## lets display the full name of an employee.
print('{} {}'.format(emp_1.first, emp_1.last))## but this is a lot of typing.
## goto oops3.py to find the remedy.
