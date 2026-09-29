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

quantity=eval(input("Enter quantity of product:"))
price=eval(input("Enter product price"))

subtotal=0
amt=price*quantity
subtotal+=amt

print("Amount:",amt)
print("Subtotal:",subtotal)

