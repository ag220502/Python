#Factorial Of Entered Number
n = int(input("Enter Value Of N : "))
fac = 1
for i in range(1,n+1):
    fac = fac * i
print("Factorial Of ",n," Is :",fac)
