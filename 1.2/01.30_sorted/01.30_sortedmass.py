f=open("Сортировка.txt","r")
a=[]
a=f.readline().split()
print(a)
f.close()
a=list(map(int,a))
n=len(a)
k=0
max_1=1
while k<n:
    for i in range(k, n):
        if a[i]>a[max_1]:
            max_1=i
    a[k],a[max_1]=a[max_1],a[k]
    k+=1
    max_1=k
print(a)
        

        
    
    
