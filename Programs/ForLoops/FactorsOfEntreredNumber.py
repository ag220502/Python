#Factors Of Entered Number
n = int(input("Enter Value Of N : "))
print("Factors Of",n," are : ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
