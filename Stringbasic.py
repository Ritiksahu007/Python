a ="stirng in double quote"
b ='string in single quote'
c =""" multi line 
stirng by using 3 quote """

print(a)
print(b)
print(c)

d ="quote inside 'quote'"
print(d)

#strings are array, we can access it be using array indexing it same as char array in java but
#only difference is in python single character is also string not an character
a="Hello World"
print(a[0])

#checking element present or not in a
print('e' in a)
print('\n')

#looping in string
for x in a:
    print(x)

#length of string
print(len(a))

#slicing in string
#start from starting and ending in 6 index but 6th element is excluded
print(a[:6])


#string some methods
print(a.upper())
print(a.isupper())
print(a.lower())

c ="  adding fukat space  "
print(c.strip())
print(c.replace('f','F'))

#string format it is one of important things which we have
#if you want to show any variable to string then use f-string
age = 22
txt = f"my name is ritik and my age is {age}"

print(txt)