print ('Шадарова София, группа 14122, программа по поиску чисел Армстронга')
def kol_vo(n):
    n=str(n)
    return len(n)
def chisla(n):
    n=str(n)
    a=[]
    for i in n:
        a+=[i]
    return a
a_Armst=[]
for n in range(1,10000):
    st=kol_vo(n)
    ch=chisla(n)
    p=0
    if ch!=a_Armst:
        for f in range(st):
            p+=int(ch[f])**st
        if n==p:
            print(n)
            a_Armst+=ch

    
