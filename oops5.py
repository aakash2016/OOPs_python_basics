## we see the difference bw class methods, regular methods and static methods.
## regular methods take instance as first argument aka 'self'
class employee:
	num_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):##constructor.
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		employee.num_emps += 1

	##regular method
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):	
		self.pay = int(self.pay * self.raise_amount)

	## new class method/
	@classmethod
	def set_raise_amt(cls, amount):## this is altering the functionality of our method.
		## class is first arg now.
		cls.raise_amount = amount

	@classmethod
	def from_str(cls, strr):
		first, last, pay = strr.split('-')
		return cls(first, last, pay)

emp_1 = employee('aakash', 'agrawal', 500)
emp_2 = employee('test', 'agrawal', 5000)
emp_1.set_raise_amt(1.099)

print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

str_1 = 'aakash-agrawal-5454'
str_2 = 'test-agrawal-454'
emp_3 = employee.from_str(str_1)
print(emp_3.pay)




