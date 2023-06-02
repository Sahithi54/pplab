M1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
M2=[[9,8,7],
        [6,5,4],
        [3,2,1]]
M3=[[0,0,0],
        [0,0,0],
        [0,0,0]]
matrix_length=len(M1)
for i in range(len(M1)):
    for k in range(len(M2)):
            M3[i][k]=M1[i][k]*M2[i][k]
print(M3)

