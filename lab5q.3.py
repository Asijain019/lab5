N=int(input("enter the value:"))
for i in range(N):
    for j in range(i+1):
        print('.',end="")
    print() 

# answer for b part:
N=int(input("enter the value:"))
for i in range(N):
    for j in range(i,N):
        print(' ',end="")
    for j in range(i+1):
        print(".",end="")
    print()
    
#answer for c part:
N= int(input("enter the value:"))
for i in range(N):
    for j in range(i,N):
        print(" ",end='')
    for j in range(i):
        print('.',end='')
    for j in range(i+1):
        print('.',end='')
    print()        