kata = "The right format"

x = 0
str = ""
while x < 41 - len(kata):
	str += "-"
	x += 1
i = 0
while x < 41 and i < len(kata):
	str += kata[i]
	x += 1
	i += 1
print(str)