# if, elif, else

a = 10
b = 20
c = 30

if a > 50 and b > 10 and c < 50:
    print(a * 2 + b * 3 + c)
elif a + b + c > 45:
    print(a + b + c)
else:
    print("Error!")