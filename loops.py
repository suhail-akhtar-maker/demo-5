for i in range(1,11):
    print(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10)


for i in range (1,6):
    for j in range(1,i+1):
        print('*',end='') 
    print()


for i in range (1,6):
    print(i*'*')


for i in range (6,0,-1):
    print(i*'*')


n=10
for i in range (1,n+1):
    print('+' *(n-i),end='')
    print('*'*(2*i-1))
    

for j in range (1,6):
    for k in range (1,6):
        print('K','J',end=' ')
    print() 


for i in range(1,6):
    for j in range (1,i+1):
        print('*',end='')
    print()    


for i in range(1,6):
    for j in range (1,i+1):
        print(i,'*',end='')
    print(j)    


for i in range(1,6):
    for j in range (1,i+1):
        print(j,'*',end='')
    print(i)        



### question

a=[1,2,3]
b=a[:]
b[0]=99

print(a)