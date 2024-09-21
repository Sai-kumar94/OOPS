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
OB=B()#B class constructor will be called
OC=C()#A class constructor will be called
