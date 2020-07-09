## Program to provide various data types used in python
## Captured basic, immutable and mutable data types for reference
## Day-3 Question 6 from LetsUpgrade AI ML 

# Basic Data Types
a = 10
b = 0.2456
c = 3+2j
d = False

# Immutable data types
st = "SampleStr"
tu = (1, 2, 3)

# Mutable Data types
li = ['a', 'b', 'c']
se = {1, 2, 3}
di = {
    1 : "abc",
    2 : "xyz",
    3 : "def",
}

print("\nBasic Data Types: \n\t", "a = ", type(a), "\n\t b = ", type(b), "\n\t c = ", type(c), "\n\t d = ", type(d))
print("\nImmutable Data Types: \n\t", "st = ", type(st), "\n\t tu = ", type(tu))
print("\nMutable Data Types: \n\t", "li = ", type(li), "\n\t se = ", type(se), "\n\t di = ", type(di))
