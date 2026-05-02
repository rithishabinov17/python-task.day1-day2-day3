#1. Program to Print Hello World

'''
print("Hello World!")'''

#2. Add, Subtract, Multiply, Divide, Modulus of Two Numbers

'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)'''

#3. Find the Square Root

'''
num = float(input("Enter a number: "))
sqrt = num ** 0.5
print("Square root =", sqrt)'''

#4. Area of a Triangle

'''
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("Area of triangle =", area)'''

#5. Solve Algebraic Formulas

'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("(a + b)^2 =", (a + b) ** 2)
print("(a - b)^2 =", (a - b) ** 2)
print("a^2 - b^2 =", (a ** 2) - (b ** 2))'''

#6. Swap Two Variables

'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)'''

#🔹 Without Using Third Variable
'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping: a =", a, "b =", b)'''

#7. Convert Kilometers to Mi

'''km = float(input("Enter kilometers: "))
miles = km * 0.63
print("Miles =", miles)'''

#8. Convert Celsius to Fahrenheit

'''
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Temperature in Fahrenheit =", fahrenheit)'''

#9. Find Last Digit of a Number

'''num = int(input("Enter a number: "))
print("Last digit =", num % 10)'''

#10. Find Last Two Digits of a Number

'''
num = int(input("Enter a number: "))
print("Last two digits =", num % 100)'''
