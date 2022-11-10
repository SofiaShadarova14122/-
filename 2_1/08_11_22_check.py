import random


def permut1():
    a, b, c = input().split()
    a, b, c = b, c, a
    return(a, b, c)


def sum21():
    a, b = input().split()
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('Ошибка! Пожалуйста, введите числа')
        sum21()
    else:
        print(a + b)


def sum22():
    n = int(input('Ведите количество чисел'))
    try:
        array = [float(i) for i in input(f'Введите {n} чисел через запятую и пробел: ').split(', ')]
        return sum(array)
    except ValueError:
        print('Ошибка! Пожалуйста, введите числа')
        return sum22()


def power31():
    a = random.randint(0, 100)
    print('Число', a, 'в степени 5 =', a ** 5)


def power32():
    a = random.randint(0, 100)
    print('Число', a, 'в степени 5 =', a * a * a * a * a)


def fibonachi4():
    chisla = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    proverka = int(input('введите число от 0 до 250:'))
    if proverka in chisla:
        print('Число относится к числам фибоначи')
    else:
        print('Число не относится к числам фибоначи')


def month5():
    a = int(input('Число месяца:'))
    if a == 1 or a == 2 or a == 12:
        print('Зима')
    elif a == 3 or a == 4 or a == 5:
        print('Весна')
    elif a == 6 or a == 7 or a == 8:
        print('Лето')
    elif a == 9 or a == 10 or a == 11:
        print('Осень')
    else:
        print('Ошибка!')

    seasons = {'Winter': (1, 2, 12),
               'Sping': (3, 4, 5),
               'Summer': (6, 7, 8),
               'Autumn': (9, 10, 11)}

    for key in seasons.keys():
        if a in seasons[key]:
            print('Второй способ:', key)
        else:
            print(' ')


def chet6():
    ch = 0
    sum_ch = 0
    un = 0
    sum_un = 0
    n = int(input(''))
    for i in range(1, n+1):
        if i % 2 == 0:
            ch += 1
            sum_ch += i
        else:
            un += 1
            sum_un += i
    print('четных всего', ch, '\nих сумма', sum_ch, '\nнечетных всего', un, '\nих сумма', sum_un)


def divider7():
    i = 1
    s = 1
    a = int(input())
    while i <= a // 2:
        if a % i == 0:
            s += 1
        i += 1
    print(a, s)


def three8():
    n, m = input().split()
    n = int(n)
    m = int(m)
    j = n
    k = n
    for i in range(n, m):
        for j in range(n, m):
            for k in range(n, m):
                if i**2 + j**2 == k**2:
                    print(i, j, k)


def check9():
    s = 0
    n, m = input().split()
    for a in range(n, m):
        s = 0
        i = a
        while i > 0:
            s = i % 10
            i = i // 10
            if a % s != 0:
                i = 0
        if a % s == 0:
            print(a)

def inverse12():
    b = []
    a = [2, 3, 4, 12, 5, 0, 39, 6]
    for i in (len(a)-1, -1, -1):
        b.append(a[i])
    print(b)


num = input('Введите номер задания')
decision = ['1', '2.1', '2.2', '3.1', '3.2', '4', '5', '6', '7', '8', '9', '12']
#if num in decision:
