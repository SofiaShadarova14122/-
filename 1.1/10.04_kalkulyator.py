print ('Это калькулятор, введите число-оператор-число через пробелы')
while True:
    try:
        a,b,c=input().split()
    except ValueError:
        print('Вы ничего не ввели')
    else: 
        z=['+', '-', '*', '/']
        def alg(a,b,c):
            try:
                a = float(a)
                b = str(b)
                c = float(c)
            except ValueError:
                print('Введено не число')
            else: 
                if b=='+':
                    print(a+c)
                elif b=='-':
                    print(a-c)
                elif b=='/':
                    try:
                        print(a/c)
                    except ZeroDivisionError:
                        print("Деление на ноль не производится")
                        return "Error"
                elif b=='*':
                    print(a*c)
                if b not in z:
                    print('Неизвестный оператор') 
        alg(a,b,c)
