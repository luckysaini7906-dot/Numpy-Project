# Structured Of Matrix calculator
# 1. Addition Matrix
# 2. Subtraction Matrix
# 3. Multiplication Matrix
# 4. Transpose Matrix
# 5. Determenate Matrix
# 6. Inverse Matrix
# 7. Eigvalues And Eigvactores
# 8. Exit

import numpy as np

# Welcome To Matrix Calculator

print("\n --- Welcome To Matrix Calculator --- \n")

rows=int(input("\nEnter The Number Of Rows : "))
colu=int(input("\nEnter The Number Of Coloum : "))

# Creating Matrix
print("\n Enter The Element Of Matrix - A : ")

A=np.array([list(map(float,input().split())) for _ in range(rows)])

print("\n Enter The Element Of Matrix - B : ")

B=np.array([list(map(float,input().split())) for _ in range(rows)])

while True:
    print("======= MENU =======\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinate Matrix")
    print("6. Inverse")
    print("7. Eigvalues & Eigvactors")
    print("8. Exit")

    Choice=int(input("\n Enter Your choice : "))
    if Choice==1:
        print("\n Addition : ")
        print(A+B)

    elif Choice==2:
        print("\n Subtraction : ")
        print(A-B)

    elif Choice==3:
        if A.shape[1]==B.shape[0]:
            print("Multiplication : ")
            print(np.dot(A,B))

        else:
            print("\n Multiplication Is Not Possible]")

    elif Choice==4:
        print("\n Transpose Of A Matrix : ")
        print(np.transpose(A))
        print("\n Transpose OF Matrix B : ")
        print(np.transpose(B))
        

    elif Choice==5:
        if rows==colu:
            print("\n Determinate Of A Matrix : ")
            print(np.linalg.det(A))
            print("\n Determinate Of B Matrix : ")
            print(np.linalg.det(B))
        else:
            print("Determinate Only For Squire Matrix")

    elif Choice==6:
        if rows==colu:
            determinate=np.linalg.det(A)
            if determinate!=0:
                print("\n Inverse Of Matrix : ")
                print(np.linalg.inv(A))
            else:
                print("Inverse does Not Exist")
        else:
            print("Inverse Only For Squire Matrix")

    elif Choice==7:
        if rows==colu:
            eigvalues,eigvactor=np.linalg.eig(A)
            print("\nEigvalues")   
            print(eigvalues)     
            print("\nEigvactors")
            print(eigvactor)

    elif Choice==8:
        print("\n Thanks For Using Matrix Calculator")
        break
    else:
        print("Invalid Choice")

