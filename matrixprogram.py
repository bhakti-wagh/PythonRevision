
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


