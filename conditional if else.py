'''
num=eval(input("Enter a number:"))

if num==num[::-1]:
    print("it's a palindrome")

else:
    print("not a palindrome")
'''

'''
x=eval(input("Enter 1st string:"))

y=eval(input("Enter 2nd string:"))


if len(x)==len(y):
    concat=x+y
    print(concat)
else:
    print(len(x))
    print(len(y))
'''
'''

x='ABC'
y='ABCd'

low=0
high=len(y)-1

mid=(low+high)//2

if id(x)==id(y):
    print("middle element of second collection :",x[mid])
else:
    print("1st item of 1st collection: ",x[0],id(x))

'''

'''
x='abcdefghijkl'

low=0
high=len(x)-1

mid=(low+high)//2

if len(x)>10 and (ord(x[0])+ord(x[-1]))%5==0:
    print("first character:",ord(x[0]))
    print("midle character:",ord(x[mid]))
    print("last character:",ord(x[-1]))

else:
    print(x)
    print(x)
    print(x)

'''
'''
a=["hello",123,"123"]

low=0
high=len(a)-1

mid=(low+high)//2

if isinstance(a[mid],str):
    print(a)
else:
    print(a[mid])
'''




'''
x="abcd"

if len(x)>=2:
    new_string=x[-1]+x[1:-1]+x[0]

    print(new_string)

else:
    print(x)
'''

'''
num=eval(input("Enter a number:"))

if num%7==0 and num%5!=0:
    print("Actual value is:",num)
else:
    print(num*4)
'''

'''
val1=eval(input("Enter a value:"))
val2=eval(input("Enter a value2:"))

if id(val1)==id(val2):
    print("address of values:",id(val1))
else:
    print("1st value address:",id(val1))
    print("2nd value address:",id(val2))
'''

'''
chara=eval(input("Enter character:"))

if not chara.isalnum():
    print(chara*3)

else:
    print(chara*5)


'''






'''
val1=eval(input("Enter 1st value:"))
val2=eval(input("Enter 2nd value:"))

if id(val1)==id(val2):
    print(val2[-1])
else:
    print(val1[0])
'''


'''
char="Haehvk"

low=0
high=len(char)-1

mid=(low+high)//2

if len(char)>=3 and char[mid] in 'aeiouAEIOU' and ord(char[0])%2==0:
    print(chr(ord(char[mid])-1))
    print(char*5)

else:
    print(char*3)
    
'''


