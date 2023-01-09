class Subtraction(list):
    def __init__(*args):
        list.__init__(*args)

    def __sub__(self, second_list):
        result = list(self)
        for i in range(len(list(second_list))):
            while second_list[i] in result:
                result.remove(second_list[i])
        print(f"List {self} minus list {second_list} ---> list {result}")


first_list = Subtraction([3, 5, 1, 4, 3, 7, 9, 9, 0])
second_list = [5, 3, 7]
first_list - second_list
