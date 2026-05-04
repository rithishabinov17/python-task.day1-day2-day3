#1. Square Star Pattern

'''for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
    
#2. Right Triangle Star Pattern
    
    for i in range(5):
     for j in range(i + 1):
        print("*", end=" ")
    print()
    
#3. Reverse Triangle Pattern
    
    for i in range(5, 0, -1):
     for j in range(i):
        print("*", end=" ")
    print()
    
#4. Pyramid Pattern

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

 #5. Inverted Pyramid

n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

#6. Diamond Pattern

n = 5

# upper part
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))

# lower part
for i in range(n - 1):
    print(" " * (i + 1) + "* " * (n - i - 1))

#7. Number Pattern (Triangle)

    for i in range(1, 6):
     for j in range(1, i + 1):
        print(j, end=" ")
    print()

#8. Alphabet Pattern

    for i in range(65, 70):
     for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()'''

#🦋 1. Butterfly Pattern

'''n = 5

# upper half
for i in range(1, n+1):
    print("* " * i + "  " * (2*(n-i)) + "* " * i)

# lower half
for i in range(n, 0, -1):
    print("* " * i + "  " * (2*(n-i)) + "* " * i)'''

#Heart Pattern

'''for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
#3. Name Pattern

'''name = "ABIRAMI"
for i in range(len(name)):
    for j in range(i + 1):
        print(name[j], end=" ")
    print()'''

#4. Diamond + Number Mix

'''n = 5

# upper half
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# lower half
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()'''

#interview question pattern

#1. Right Triangle Star Pattern

'''n = 5

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()'''

#2. Reverse Triangle Pattern

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#3. Pyramid Pattern (Very Important)

n = 5

for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))


#4. Inverted Pyramid

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

#5. Number Triangle (Interview Favorite)

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#6. Floyd’s Triangle (Very Important)


n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#7. Alphabet Pattern

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()    

    

    
