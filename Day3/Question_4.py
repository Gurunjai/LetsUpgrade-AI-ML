## Program to swap two numbers without any temporary variables
## Day-3 Question 4 from LetsUpgrade AI ML 

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print("Before swap\n\t a = ", a, ", b = ", b)
a, b = b, a
print("After swap\n\t a = ", a, ", b = ", b)