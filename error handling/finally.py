a = int(input("enter number:"))
b = int(input("enter number:"))

print("Good Morning")
print(a+b)
try:
    print(a/b)
except:
    print(a/1)
finally:
    print("Clean-up code")
print("Good Afternoon")
print("Good Evening")