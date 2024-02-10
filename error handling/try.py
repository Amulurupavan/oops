a = int(input("enter number:"))
b = int(input("enter number:"))

print("GM")
print(a+b)
try:
    print(a/b)   #risky code
except:
    print(a/1)   #handling code
print("GA")
print("GE")