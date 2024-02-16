import sys

if len(sys.argv) < 2:
    exit()
res = sys.argv[1]
x = 1
for x in sys.argv:
    res += x
print(res)
