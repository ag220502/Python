'''
Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage
people to recycle them. In one particular jurisdiction, drink containers holding
one liter or less have a $0.10 deposit, and drink containers holding more than one
liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a
dollar sign and two digits to the right of the decimal point.
'''
print("="*55)
oneLitre  = int(input("Enter No. Of Containers with one or less than one litre : "))
moreLitre = int(input("Enter No. Of Containers with more than one litre        : "))
print("="*55)

total = (oneLitre * 0.10) + (moreLitre * 0.25)

print("="*45)
print("                Recycle System")
print("="*45)
print("Containers with less than or 1 litre :",oneLitre)
print("Containers with more than 1 litre    :",moreLitre)
print("="*45)
print("Total Amount                         : $",total,sep="")
print("="*45)
