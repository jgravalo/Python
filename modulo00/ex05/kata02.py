kata = (2019, 9, 25, 3, 30)

def num(x):
	s = ""
	if x < 10:
		s = "0"
	s += str(x)
	return s

day = num(kata[2])
month = num(kata[1])
year = str(kata[0])
hour = num(kata[3])
min = num(kata[4])

print("{}/{}/{} {}:{}".format(day, month, year, hour, min))