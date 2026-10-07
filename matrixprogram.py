'''
lst=[[1,2,3],[4,5,6],[7,8,9]]

#Diagnoal matrix
for i in range(3):
    for j in range(3):

        if i==j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()


print()
print()
#lower triangle matrix

for i in range(3):
    for j in range(3):
        if i>=j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()


print()

#upper traingle matrix

for i in range(3):
    for j in range(3):
        if i<=j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()



print()
print()
#Transpose matrix

for i in range(3):
    for j in range(3):
        print(lst[j][i], end=" ")

    print()


'''

'''
Accept the elements of a 3 x 3 matrix from the user
2. Display the original matrix
3. Print the diagonal matrix by replacing all non-diagonal elements with zero
4. Print the upper triangular matrix by replacing all elements below the main diagonal
with zero 5. Print the lower triangular matrix by replacing
all elements above the main diagonal with zero'''


lst=[]

for i in range(3):
    row=[]
    for j in range(3):
       num= eval(input("Enter a number"))

       row.append(num)

    lst.append(row)


print(lst)

#diagnoal matrix
for i in range(3):
    for j in range(3):

        if i==j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()


print()
print()
#lower triangle matrix
for i in range(3):
    for j in range(3):
        if i>=j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()


print()

#upper traingle matrix

for i in range(3):
    for j in range(3):
        if i<=j:
            print(lst[i][j],end=" ")

        else:
            print("0",end=" ")

    print()



print()
print()
#Transpose matrix

for i in range(3):
    for j in range(3):
        print(lst[j][i], end=" ")

    print()


    







        
    
