# if, elif, else

string_1 = ["HTML+CSS", "JavaScript", "Python", 1, 2, 3]

if "HTML+CSS" in string_1 and 4 in string_1:
    print("1st condition is True")
elif "JavaScript" in string_1 and 1 in string_1:
    print("2nd condition is True")
elif "Python" in string_1 and 2 in string_1:
    print("3rd condition is True")
else:
    print("Error! All conditions are wrong")

# Якщо всі умови будуть вірні, то виконається лише перше умова, інші ні.