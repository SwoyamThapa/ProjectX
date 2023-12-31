# Main file for the calculator app

import addition
import subtraction
import division
import multiply
import minmax
import modulo
import square
import average

def run(arg, num1, num2):

	addObject = addition.Addition(num1, num2)
	subObject = subtraction.Subtraction(num1, num2)
	divideObject = division.Division(num1,num2)
	multObject = multiply.Multiplication(num1, num2)
	minmaxObject = minmax.Minmax(num1, num2)
	moduloObject = modulo.Modulo(num1, num2)
	squareObject = square.Square(num1, num2)
	avgObject = average.Average(num1, num2)


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

	elif arg == "divide":
		result = divideObject.divide()
		resultPrinted = "The division of numbers is: " + str(result)
	
	elif arg == "modulo":
		result = moduloObject.modulo()
		resultPrinted = "The modulo of numbers is: " + str(result)

	elif arg == "minmax":
		minimum = minmaxObject.min()
		maximum = minmaxObject.max()
		resultPrinted = "The min number is: " + str(minimum) + " and the max number is: " + str(maximum)

	elif arg == "square":
		result = squareObject.square()
		resultPrinted = "Num1 squared num2 is: " + str(result)

	elif arg == "average":
		result = avgObject.average()
		resultPrinted = "The average is: " + str(result)



	return resultPrinted



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
arg = str(input("What do you wanna do? (add, sub, mult, divide, modulo, minmax, square, average): "))

print(run(arg, num1, num2))


