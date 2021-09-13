'''
Exercise 3: Area of a Room
(Solved, 13 Lines) Write a program that asks the user to enter the width and length
of a room. Once these values have been read, your program should compute and display
the area of the room. The length and the width will be entered as floating-point
numbers. Include units in your prompt and output message; either feet or meters,
depending on which unit you are more comfortable working with.
'''

width = float(input("Enter Width Of The Room In meters   : "))
length = float(input("Enter Length Of The Room In meters  : "))
area = width * length
print("="*40)
print("== Length Of Room :",length,"m.")
print("== Width Of Room  :",width,"m.")
print("== Area Of Room   :",area,"sq. m.")
print("="*40)
