#1) Check if the 3rd last character of a string is a vowel

"""
s = input("Enter a string: ")

if len(s) >= 3:
    ch = s[-3].lower()
    if ch in "aeiou":
        print("3rd last character is a vowel")
    else:
        print("3rd last character is not a vowel")
else:
    print("String is too short")"""
#2) Check if the first and last digit of a 5-digit number are same

'''
num = input("Enter a 5-digit number: ")

if len(num) == 5:
    if num[0] == num[-1]:
        print("First and last digits are same")
    else:
        print("First and last digits are not same")
else:
    print("Not a 5-digit number")'''

#3) Income Tax Calculation (Indian rules – basic example)

'''
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Income Tax =", tax)'''

#4) Calculate Percentage and Grade (5 Subjects)

'''
total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of subject {i}: "))
    total += marks

percentage = total / 5
print("Percentage =", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Fail")'''

#5) Celsius to Fahrenheit Conversion

'''
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)'''

#6) Surface Area of a Triangle (Heron’s Formula)

'''
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Surface area of triangle =", area)'''

#7) Print Day Based on Number
'''
day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input")'''

#8) Voting Eligibility Check

'''
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")'''

#9) Count of Characters in a String

'''

s = input("Enter a string: ")
print("Number of characters =", len(s))'''

#10) Check if Triangle is Equilateral

'''
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a == b == c:
    print("Equilateral Triangle")
else:
    print("Not an Equilateral Triangle")



