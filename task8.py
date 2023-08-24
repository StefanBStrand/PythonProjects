# Building a basic calculator:

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)  # int function will be looking for a whole number. Cant use decimal points by using this.
#  To make a calculator that takes decimal point numbers, use float instead of int

print(result)

#  By default, when we get input from a user, Python will convert it into a string