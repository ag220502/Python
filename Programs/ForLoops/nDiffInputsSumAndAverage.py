#Take N different inputs and print their sum and average
n = int(input("Enter the Number Of Values : "))
sum1 = 0
for i in range(1,n+1):
    inp = int(input("Enter Value",i," : "))
    sum1 = sum1 + inp
print("The Sum Of Inputs are : ",sum1)
avg = sum1/n
print("The Average Of Inputs are : ",avg)
