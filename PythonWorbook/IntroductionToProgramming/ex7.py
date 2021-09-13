'''Exercise 7: Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and then displays
the sum of all of the integers from 1 to n. The sum of the first n positive integers
can be computed using the formula:
sum = (n)(n + 1)/ 2
'''
print("="*20)
n = int(input("Enter Value Of N : "))
print("="*20)
tSum = (n*(n+1))/2
print("="*20)
print("Value Of n : ",n)
print("Total Sum  : ",(int)(tSum))
print("="*20)
