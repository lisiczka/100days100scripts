# Simple calculator function.

def calc(operation, a, b):
	if operation == "add":
		print(a, "+", b,)
		return a + b

	elif operation == "sub":
		print(a, "-", b)
		return a - b

	elif operation == "multi":
		print(a, "*", b)
		return a * b

	elif operation == "div":
		if b != 0:
			print(a, "/", b)
			return a / b
		else:
			print("Error. Division by 0 is not acceptable.")

	else:
		print('Error. Wrong operation name.')



print("Result:", calc("add", 2, 4))

