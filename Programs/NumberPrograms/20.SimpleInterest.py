#Calculate Simple Interest

p = float(input("Enter Principal        : "))
r = float(input("Enter Rate Of Interest : "))
t = float(input("Enter Years            : "))

si = p * r * t / 100

print("="*30)
print("      Simple Interest")
print("="*30)
print(" Principal       :",p)
print(" Rate            :",r)
print(" Years           :",t)
print(" Simple Interest :",si)
print("="*30)
