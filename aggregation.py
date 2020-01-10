##Bank has a employee.
## Library has a book.
## Aggregation -- HAS A, THESE RELATIONSHIPS ARE UNIDIRECTIONAL.
# In aggregation relationship both entities can survive individually.

class Salary:
	def __init__(self, pay, reward):	
		self.pay = pay
		self.reward = reward

	def annual_salary(self):
		return (self.pay)*12 + self.reward

class Employee:
	def __init__(self, name, position, sal):
		self.name = name
		self.position = position
		self.final_salary = sal 
	
	def final_sal(self):
		return self.final_salary.annual_salary()

sal = Salary(1000, 100)
emp1 = Employee('aakash', 'data scientist', sal)#we pass the object of salary.
print(emp1.final_sal()) 

# remember -- Agrregation = weak connection and composition = strong connection.
