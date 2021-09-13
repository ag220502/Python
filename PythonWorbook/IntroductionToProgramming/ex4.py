'''
Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user
in feet. Display the area of the field in acres.
'''
print("="*45)
width = float(input("Enter Width Of The Fields In Feets   : "))
length = float(input("Enter Length Of The Fields In Feets  : "))
print("="*45)
area = width * length
acArea = 43560/area
print("="*45)
print("== Length Of Fields :",length,"feet.")
print("== Width Of Fields  :",width,"feet.")
print("== Area Of Fields   :",area,"sq. feet")
print("== Area Of Fields   :",acArea,"acres.")
print("="*45)
