#Print Even No from 1 to N
n = int(input("Enter Value Of N : "))
for i in range(1,n+1,1):
    if i%2==0:
        print(i,end=" ")
