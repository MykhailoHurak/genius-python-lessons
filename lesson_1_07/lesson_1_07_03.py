class A(object):
    """Class A"""
    name_a = "Name A"
    is_main_class = True

    def hello(self):
        print("Hello from class A")

class B(A):
    """Class B"""
    name_b = "Name B"
    is_main_class = False

    # def hello(self):
    #     print("Hello from class A")

class C(B):
    """Class C"""
    name_c = "Name C"

test_exempliar = C()

print(test_exempliar.name_a)
print(test_exempliar.name_b)
print(test_exempliar.name_c)

print(test_exempliar.is_main_class)

print(test_exempliar.hello())