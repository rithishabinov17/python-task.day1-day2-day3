#1) Print numbers from 1 to 10
'''
for i in range(1, 11):
    print(i)'''

#2) Print all even numbers from 1 to 5

'''
for i in range(1, 51):
    if i % 2 == 0:
        print(i)'''

#3) Print all odd numbers from 1 to 50

'''
for i in range(1, 51):
    if i % 2 != 0:
        print(i)'''
#4) Print the multiplication table of a given number

'''
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)'''

#5) Find the sum of numbers from 1 to 100

'''
total = 0
for i in range(1, 101):
    total += i

print("Sum =", total)'''

#6) Print numbers from 10 to 1 in reverse order

'''
for i in range(10, 0, -1):
    print(i)'''
#7) Count numbers between 1 and 100 divisible by 7

'''
count = 0

for i in range(1, 101):
    if i % 7 == 0:
        count += 1

print("Count =", count)'''

#8) Numbers divisible by 3 but not by 5 (1 to 100)
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)'''

#9) Find factorial of a given number
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)'''

#10) Print squares of numbers from 1 to 20

'''
for i in range(1, 21):
    print(i, "square =", i * i)'''


