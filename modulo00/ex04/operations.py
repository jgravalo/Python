import sys

if len(sys.argv) < 2:
	print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
	exit()
if len(sys.argv) < 3:
	print("AssertionError: too few arguments")
	exit()
if len(sys.argv) > 3:
	print("AssertionError: too many arguments")
	exit()
if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
	print("AssertionError: only integers")
	exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
sum = a + b
dif = a - b
pro = a * b
if b == 0:
	quo = "ERROR (division by zero)"
else:
	quo = a / b
if b == 0:
	res = "ERROR (module by zero)"
else:
	res = a % b
print("Sum:        {}".format(sum))
print("Difference: {}".format(dif))
print("Product:    {}".format(pro))
print("Quocient:   {}".format(quo))
print("Remainder:  {}".format(res))
