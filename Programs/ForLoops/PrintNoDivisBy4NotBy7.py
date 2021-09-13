#Print Nos which can be divided by 4 but not by 7 from 1 to N
n = int(input("Enter Value Of N : "))
for i in range(1,n+1,1):
    if i%4==0 and i%7!=0:
        print(i,end=" ")
