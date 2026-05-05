#1.Count the number of words in a sentence

'''s=input("enter your sentence:") #s=variable store and input user get input value
words=s.split() #split="i" "love" "python"
print("number words:", len(words)) #len=count words'''

#2.Convert a string to uppercase and lowercase

'''s=input(" enter the string:")
print("upper case:", s.upper())# convert capital letter
print("lower case",  s.lower())#convert  small lettwe'''

#3.Remove all spaces from a string

'''s=input(" enter the string:")
result=s.replace(" ","") #replce=without speace/ remove all spaces from a string.
print("without speace:", result)'''

#4.Find the length of a string without using len().

'''s = input("Enter a string: ")
count = 0

for i in s:
    count = count + 1

print("Length of string:", count)'''

#5.Count how many times a specific character appears in a string.

'''s=input("enter the string:")
ch=input("enter the chacter to count:")
count=0
for i in s:
    if i==ch: #condtion check true or false
        count+=1
print("count the chacter:", count)'''

#6. 6.Print each character of a string on a new   line
s=input("enter the string:")
for i  in s:
    print(i)

 

