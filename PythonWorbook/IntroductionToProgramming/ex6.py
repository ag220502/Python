'''
Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a
meal ordered at a restaurant from the user. Then your program will compute the tax
and tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the
values are displayed using two decimal places.
'''
print("="*40)
cost = float(input("Enter the cost of meal : "))
print("="*40)
tax = (cost * 5)/100

tip = (cost * 18)/100

print("="*40)
print("          Tax And Tip")
print("="*40)
print(" Cost Of Meal :",cost)
print(" Tax Amount   :",tax)
print(" Tip Amount   :",tip)
print("="*40)
print(" Total Amount :",(cost+tax+tip))
