#Сортировка слиянием, Шадарова София 14122
try:
    def merge_sort(file):
        if len(file) > 2:
            middle = len(file)//2
            left = file[:middle]
            right = file[middle:]
            merge_sort(left)
            merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    file[k] = left[i]
                    i += 1
                else:
                    file[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                file[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                file[k] = right[j]
                j+=1
                k+=1
    txt = input("Введите название файла: ")
    with open(txt, 'r') as f:
        file = f.readlines()
        sort = []
        for i in range(len(file)):
            sort.append(" ".join(file[i].splitlines()))
        merge_sort(file)
        print("Сортировка слиянием")
        print(str(sort))
except FileNotFoundError:
    print ("Файла не существует")

    
