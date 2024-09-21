class A:
    a=10
    def __init__(self):
        print('__init__ of A class')
class B(A):
    b=20
    def __init__(self):
        print('__init__ of B class')
class C(A):
    pass
class D(B):
    pass
class E(C,D):
    pass
print(E.mro())

#parent classes with different parents

#parent classes with same parents

class A:
    a=10
    def __init__(self):
        print('__init__ of A class')
class B(A):
    b=20
    def __init__(self):
        print('__init__ of B class')
class C(A):
    pass
class D(B,C):
    pass
print(D.mro())#D------>B--------->C--------->A-------->Object










