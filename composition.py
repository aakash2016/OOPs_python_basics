## Abstraction.
## All relation cannot be defined with help of inheritance.
## Composition. (PART OF) <<-- when two classes are highly dependent on each other.
## salary is a part of employee.
## content is a part of container.
class Salary:
	def __init__(self, pay, reward):	
		self.pay = pay
		self.reward = reward

	def annual_salary(self):
		return (self.pay)*12 + self.reward

class Employee:## we will use content(Salary) inside this.
	def __init__(self, name, position, pay, reward):
		self.name = name
		self.position = position
		self.final_salary = Salary(pay, reward) ## initiating salary class inside employee.
	
	def final_sal(self):
		return self.final_salary.annual_salary()

emp1 = Employee('aakash', 'data scientist', 10000, 222)
print(emp1.final_sal()) 
## remember -- if container destroyed then content will be of no use.
