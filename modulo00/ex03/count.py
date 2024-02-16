def text_analyzer(text = "error"):
    if text == "error":
        print("What is the text to analyze?")
        return
    if type(text) != "<type 'str'>":
        print("AssertionError: argument is not a string")
        return
    chars = 0
    upper = 0
    lower = 0
    marks = 0
    spaces = 0
    for x in text:
        if x >= 'A' and x <= 'Z':
            upper += 1
        if x >= 'a' and x <= 'z':
            lower += 1
        if x == '.' or x == ',' or x == '?' or x == '!':
            marks += 1
        if x == ' ':
            spaces += 1
        chars += 1
    print("The text contains "+ str(chars) +" character(s):")
    print("- " + str(upper) + " upper letter(s)")
    print("- " + str(lower) + " lower letter(s)")
    print("- " + str(marks) + " punctuation mark(s)")
    print("- " + str(spaces) + " space(s)")
'''    def doc():
        print("This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.")
    if __name__ == '__doc__':
        sys.exit(main())
'''
