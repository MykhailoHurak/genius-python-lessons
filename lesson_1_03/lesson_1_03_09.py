# while
# if

a = 0
list_1 = []

while len(list_1) <= 11:
    list_1.append(a)
    a = a + 1
    print(list_1)
    if len(list_1) == 6:
        print("Middle of List")