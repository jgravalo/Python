import sys

def main():
	if len(sys.argv) != 3:
		print("Error: bad number of arguments")
		exit()
	S = sys.argv[1].split()
	if sys.argv[2].isdigit == False:
		print("Error: bad arguments")
		exit()
	N = int(sys.argv[2])

if __name__ == "__main__":
	main()