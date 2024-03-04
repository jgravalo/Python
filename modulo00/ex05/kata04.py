kata = (0, 4, 132.42222, 10000, 12345.67)

def error():
	print("bad format")
	exit()

def num(x):
	if type(x).__name__ != "int" or x < 0 or x > 100:
		error()
	module = ""
	if x < 10:
		module = "0"
	module += str(x)
	return module

module = num(kata[0])
ex = num(kata[1])
if type(kata[2]).__name__ != "float":
	error()
if type(kata[3]).__name__ != "int":
	error()
if type(kata[4]).__name__ != "float":
	error()
print("module_{}, ex_{} : {:.2f}, {:.2e}, {:.2e}".format(module, ex, kata[2], kata[3], kata[4]))