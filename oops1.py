##Python OOPs
## lets create a company employee class
class employee:
	pass

emp_1 = employee() ## unique instance of employee class.
emp_2 = employee()

print(emp_1)
print(emp_2) ##different location in memory

#instance variable contain data unique to each variable.
## manually creating instace variables.
emp_1.first = 'aakash'
emp_1.last = 'agrawal'
emp_1.pay = 2000

emp_2.first = 'test'
emp_2.last = 'agrawal'
emp_2.pay = 20000

print(emp_1.pay) ##you need to manually set variable every time/
## there is no benefit of using clases/
## go to oops2.py


