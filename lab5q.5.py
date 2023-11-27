#Lcm of two numbers:
a=int(input("enter the no:"))
b =int(input("enter the no:"))
maxnum=max(a,b)
while True:
    if maxnum%a==0 and maxnum%b==0 :
        break
    maxnum+=1
print(f'the LCM of the two numbers{a}and {b} = {maxnum}')
