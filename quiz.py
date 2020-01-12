## QUIZ
# Q1..
def outerFunction():
        global a
        a = 20
        def innerFunction():
            global a
            a = 30
            print('a =', a)  

a = 10
outerFunction()
print('a =', a)

# Q2..
class Foo:
	def printLine(self, line='Python'):
		print(line)
      
o1 = Foo()
o1.printLine('Java')

# Q3..
class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
      
	def __sub__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x,y)
            
p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1-p2
print(result.x, result.y)

