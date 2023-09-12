#  Building a basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#  By default, when python gets input from a user, it will convert it into a string.
result = float(num1) + float(num2)  # Float lets us use decimal points in numbers.
print(result)
