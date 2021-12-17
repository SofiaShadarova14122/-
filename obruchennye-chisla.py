print ('Шадарова София, группа 14122, программа по поиску обрученных чисел')
def OBR(n):
       for n1 in range (1,n):
           sum1=1
           i=2
           while i*i<=n1:
               if n1%i==0:
                   sum1+=i
                   if i*i!=n1:
                       sum1+=n1/i
               i=i+1
           if sum1>n1:
                n2=sum1-1
                sum2=1
                m=2
                while m*m<=n2:
                    if n2%m==0:
                        sum2+=m
                        if m*m!=n2:
                            sum2+=n2/m
                    m+=1
                if sum2==n1+1:
                    print('('+str(n1)+', '+str(n2)+')')
n=10000
OBR(n)
