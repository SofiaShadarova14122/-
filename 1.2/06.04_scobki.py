v = list(input("Введите выражение на проверку: "))
vr = []
for i in range(len(v)):
    if v[i] == '(' or v[i] == '{' or v[i] == '[':
        vr.append(v[i])
        continue
    if (v[i] == ')' or v[i] == '}' or v[i] == ']') and ((vr[-1]+v[i] == '()') or (vr[-1]+v[i] == '{}') or (vr[-1]+v[i] == '[]')):
            vr.pop()
    else:
        print('Закрыты не все скобки!')
        exit()
if vr == []:
    print('Скобки рассталены верно:)')
else:
    print('Закрыты не все скобки!')
