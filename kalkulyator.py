def Kalk(a,b,c):
    resultat=0
    try:
        a = float(a)
        b = str(b)
        c = float(c)
    except ValueError:
        print("Это не число")
    else: 
        if b=='+':
            resultat=a+c
            return resultat
        elif b=='-':
            resultat=a-c
            return resultat
        elif b=='/':
            resultat=a/c
            return resultat
        elif b=='*':
            resultat=a*c
            return resultat
        elif b =="^" or b=="**":
            resultat=a**c
            return resultat
        else:
            print("Неверно введен оператор")
while True:
    a,c,b=input("Введите два числа и оператор").split()
    print(Kalc(a,b,c))
