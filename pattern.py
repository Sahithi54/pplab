n=int(input("enter the number: "))
k=n
for i in range(0,n):
    for j in range(1,i+1):
        print(k,end=" ")
    k=k-1
    print("\n")
