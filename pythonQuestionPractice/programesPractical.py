'''1. Write a Python program to accept
the marks obtained by a student in five
subjects and calculate the total marks,
average marks, and percentage.'''

# answer
'''
math=eval(input("Enter math marks :"))
eng=eval(input("Enter english marks:"))
sci=eval(input("Enter science marks:"))
geo=eval(input("Enter geo marks:"))
python=eval(input("Enter python marks:"))


#total marks
totalMarks=math+eng+sci+geo+python
print(f"Total marks are: {totalMarks}")

#average marks
avg=totalMarks/5
print(f"Average is :{avg}")

#Percentage
per=(totalMarks/500)*100
print(f"Percentage is :{per}")
'''

'''
2. Write a Python program to accept an
employee's basic salary and calculate DA, HRA,
gross salary,tax deduction, and net salary.'''

'''
#answer:
sal=eval(input("Enter basic salary:"))

#DA
da=eval(input("Enter DA:"))
#HRA
hra=eval(input("Enter HRA:"))

#tax
tax=eval(input("Enter tax deducation:"))


#calculate DA
DA=sal*da/100
print(f"DA is :->{DA}")

#HRA
HRA=sal*hra/100
print(f"HRA is :-> {HRA}")

#gross sasl
Gsal=sal+DA+HRA
print(f"Gross salary is :{Gsal}")

#tax
TAX=Gsal*tax/100
print(f"Tax deduction is:{TAX}")

#net sal
NetSal=Gsal-TAX
print(f"Net salary is :{NetSal}")


#formula :  basic = 30000

da = basic * 10 / 100
hra = basic * 20 / 100

gross = basic + da + hra

tax = gross * 5 / 100

net = gross - tax'''


'''
Write a Python program to accept the number of electricity units consumed by a consumer
and calculate the electricity bill
according to different consumption slabs.

0-100-> 5
101-200->10
201-300->15
300>-> 20
'''
'''
units=eval(input("Enter electricity units:"))

if units<=100:
    bill=units*5

elif units<=200:
    bill=(100*5)+((units-100)*10)

elif units<=300:
    bill = (100*5)+(100*10)+((units-200)*15)

else :
    bill=(100*5)+(100*10)+(100*15)+((units-300)*20)



print(f"Electricity bill :{bill}")
'''



'''
. Write a Python program to accept the price and quantity of three products
and calculate the subtotal, discount, GST, and final payable amount.

'''
'''
quantity=eval(input("Enter quantity of product:"))
price=eva
1l(input("Enter product price"))

subtotal=0
amt=price*quantity
subtotal+=amt

print("Amount:",amt)
print("Subtotal:",subtotal)
'''

'''
#checking palindrome using while loop
num=int(input("Enter a number:"))

original =num
rev=0

while num>0:
    digit = num%10
    rev= rev*10+digit
    num= num//10

if original == rev:
    print("Palindrome")
else:
    print("Not palindrome")
'''


'''
#sum and product of number
num=int(input("Enter a number:"))

sum1=0
pro=1

while num>0:

    digit = num%10

    sum1 = sum1 +digit

    pro = pro * digit

    num = num //10

print("Sum of digits :",sum1)
print("Products of digits :",pro)

'''

'''
#numbers of digit , largest digit and smallest digit
num = int(input("Enter a number :"))

count=0
largest =0
smallest =9

while num>0:

    digit = num%10

    count= count +1

    if digit>largest:
        largest = digit

    if digit<smallest:
        smallest = digit

    num = num //10

print("Count is ", count)
print("Largest is ", largest)
print("Smallest is", smallest)
'''

'''
num = int(input("Enter a number:"))

total =0

b=str(num)

power= len(b)

for i in b:
    total = total+int(i)**power

if total == num:
    print("Armstsrong")

else:
    print("not armstrong")

'''

'''
num = int(input("Enter a number:"))

dum = num
total =0


num_len=len(str(num))

while num>0:

    last_digit= num%10

    total = total + last_digit**num_len

    num= num//10
    

if total == dum:
    print("Armstsrong")

else:
    print("not armstrong")

'''


#prime number
'''
num = int(input("Enter a number"))

count=0

for i in range(1,num+1):

    if num%i==0:
        count = count+1

if count ==2:
    print("Prime number")

else :
    print("Not prime number")
'''


'''
seconds= int(input("Enter  seconds:"))

hours = seconds//3600
remaining = seconds %3600

minutes = remaining //60
sec = remaining %60


print("Hours:",hours)
print("Minutes:",minutes)
print("Sec:",sec)

'''

price1=


