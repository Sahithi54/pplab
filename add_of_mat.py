M1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
M2=[[10,11,12],
        [13,14,15],
        [16,17,18]]
M3=[[0,0,0],
        [0,0,0],
        [0,0,0]]
matrix_length=len(M1)
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k]=M1[i][k]+M2[i][k]
print(M3)
