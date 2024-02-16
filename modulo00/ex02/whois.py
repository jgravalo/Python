import sys

if len(sys.argv) < 2:
    print
elif len(sys.argv) > 2:
    print ("AssertionError: more than one argument are provided")
elif type(sys.argv[1]) != "<class 'int'>":
    print ("AssertionError: argument is not an integer")
elif int(sys.argv[1]) == 0: 
    print ("I'm Zero.")
elif int(sys.argv[1]) % 2 == 0:
    print ("I'm Even.")
elif int(sys.argv[1]) % 2 == 1:
    print ("I'm Odd.")
