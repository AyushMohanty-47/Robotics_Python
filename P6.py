m=int(input("Enter no. of rows for each matrix: "))
n=int(input("Enter no. of columns for each matrix: "))

A=[]
print("Enter elements of Matrix A: ")
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)

B=[]
print("Enter elements of Matrix B: ")
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)

C=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Resultant Matrix: ")
for row in C:
    print(row)