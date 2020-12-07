'''
def add(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiply(a, b):
	return a * b

def division(a, b):
	return a / b
while True:

	a = input('первое число: ')
	b = input('второе число: ')
	c = input('оператор: ')

	if a.isdigit() and b.isdigit():
		a = float(a)
		b = float(b)

		if c == '+':
			print(add(a, b))
		elif c == '-':
			print(subtraction(a, b))
		elif c == '*':
			print(multiply(a, b))
		elif c == '/':
			print(division(a, b))
	else:
		print('вы ввели не число')
'''

while True:
	print(eval(input('введите пример: ')))
	input(9)
