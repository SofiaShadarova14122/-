#Шадарова София 14122
#Первое задание: умножить каждый элемент на два
S=[1,2,3,4,5,6]
print('Строка до:  ', S)
Sx2=list(map(lambda x:x*2, S))
print('Строка после:  ', Sx2)
print(' ')
#Второе задание: произведение по-элементно элементов из трех коллекций
A=[5, 6, 8, -3, 12, 57]
B=[56, 7, 89, 0, 5, 43]
C=[89, 8, 4, 3, 54, 10]
Pr=[A*B*C for A,B,C in zip(A,B,C)]
print(list(Pr))
print(' ')
#Третье задание: длина каждого элемента в коллекции
spisok=['Крош', 'Ежик', 'Бараш', 'Нюша', 'Капатыч', 'Пин', 'Совунья', 'Лосяш']
dlina=list(map(lambda x: len(str(x)), spisok))
print(dlina)
print(' ')
#Четвертое задание: только четные элементы
S=[1,2,3,4,5,6]
result=list(filter(lambda x: not int(x)%2, S))
print(' ')
#Пятое задание: непустые
Sp = ['', 'Ежик', 'Пин', '', 'Совунья', '', 'Лосяш', '', 'Кар-карыч']
Tr = list(filter(lambda x: x != '', Sp))
print(Tr)
print(' ')
#Шестое задание: упаковка тройками
A=[5, 6, 8, -3, 12, 57]
B=[56, 7, 89, 0, 5, 43]
C=[89, 8, 4, 3, 54, 10]
Pr=zip(A, B, C)
print(list(Pr))
print(' ')
#Седьмое задание: упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.
A = [3, 5, 6, 77, 4, 34, 91, 67, 815]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Bx2 = list(map(lambda x: 2*x, B))
Itog = zip(A,Bx2)
print(list(Itog))