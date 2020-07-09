## Program to swap two numbers with the help of temporary variable
## Day-3 Question 3 from LetsUpgrade AI ML 

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print("Before swap\n\t a = ", a, ", b =", b)
tmp = a
a = b
b = tmp
print("After swap\n\t a = ", a, ", b =", b)