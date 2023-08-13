# Main file for the calculator app

import addition
import subtraction
import multiply

def run(arg, num1, num2):

	addObject = addition.Addition(num1, num2)
	subObject = subtraction.Subtraction(num1, num2)
	multObject = multiply.Multiplication(num1, num2)

	result = 0

	resultPrinted = ""

	if arg == "add":
		result = addObject.add()
		resultPrinted = "The added numbers are: " + str(result)

	elif arg == "sub":
		result = subObject.subtract()
		resultPrinted = "The subtracted numbers are: " + str(result)

	elif arg == "mult":
		result = multObject.multiply()
		resultPrinted = "The multiplied numbers are: " + str(result)

	return resultPrinted



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
arg = str(input("What do you wanna do? (add, sub, mult): "))

print(run(arg, num1, num2))


