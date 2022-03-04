#функция сортировки
def sort_two(a,b):
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c
    
def sort(s):
    if len(s)<2:
        return s
    else:
        middle=len(s)//2
        left=sort(s[:middle])
        right=sort(s[middle:])
        return sort_two(left,right)


from random import randint
print("Программа выполнена методом сортировки слияением")
#Cоздание файла с рандомными числами
while True:
        pi=input("1) Создать файл с рандомно заданными числами\n 2) Завершить программу\n ")
        if pi=="1": 
            n=input("Bведите имя файла: ")
            my = '{}.txt' .format(n)
            try:
                fil=open(my)
            except FileNotFoundError:
                fil=open(my,"w")
            else:
                while True:
                    of=input("\nФайл уже существует. Заменить? 1) Да 2)Нет\n ")
                    if of=="1":
                        file=open(my,"w+")
                        print("Успешно!")
                        break
                    elif of=="2":
                        print("Перезапустите программу")
                    elif (of!="2") and (of!="1"):
                        print("Я запутался, вы где-то неверно ввели..")
                fil.close()
            while True:
                z=input("Количество чисел(не больше 300)")
                try:
                    z = int(z)
                    break
                except ValueError:
                    print("Это строка.. Введите, пожалуйста,число\n")
            while True:
                try:
                    x, y = map(int, input("В каком интервале находятся числа (минимальное и максимальное)").split())
                    break
                except ValueError:
                    print("Я запутался, вы где-то неверно ввели..\n")
            my_file = open(my, "w+")
            for i in range(z):
                p=str(randint(x,y))
                my_file.write(p)
                my_file.write("\n")
            my_file=open(my)
            my_file=my_file.readlines()
            massive=[]
            for line in my_file:
                massive.append(int(line))
                result=sort(massive)
            massive=[]
            for line in my_file:
                massive.append(int(line))
            result=sort(massive)
            n=input("Bведите имя конечного файла: ")
            me = '{}.txt' .format(n)
            try:
                file=open(me)
            except FileNotFoundError:
                file=open(me,"w")
                for num in result:
                    file.write(str(num))
                    file.write("\n")
                file.close()
            else:
                while True:
                    off=input("\nФайл с результатами уже существует. Заменить? 1) Да\n 2)Нет\n ")
                    off=int(off)
                    if off==1:
                        file=open(me,"w+")
                        for num in result:
                            file.write(str(num))
                            file.write("\n")
                        print("Успешно!")
                        break
                    elif off==2:
                        print("Перезапустите программу")
                        break
                file.close()
            break
        elif pi=="2":
            print("Программа завершена")
            break
        elif (pi != "1") and  (pi != "2") :
            print('Я запутался, вы где-то неверно ввели..')
